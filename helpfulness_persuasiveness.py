#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 10:27:19 2025

@author: olesya
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 19:40:03 2025

@author: olesya
"""

import os
import pandas as pd
from scipy.stats import spearmanr, mannwhitneyu
import numpy as np

# ------------------------------------------------------------
# 1. LOAD NOTES AND COMPUTE PERSUASIVENESS
# ------------------------------------------------------------

# List of persuasion technique columns
technique_cols = [
    "Appeal_to_Authority","Appeal_to_Fear-Prejudice","Appeal_to_Hypocrisy",
    "Appeal_to_Popularity", "Appeal_to_Time","Appeal_to_Values",
    "Causal_Oversimplification", "Consequential_Oversimplification",
    "Conversation_Killer", "Doubt","Exaggeration-Minimisation",
    "False_Dilemma-No_Choice", "Flag_Waving","Guilt_by_Association",
    "Loaded_Language", "Name_Calling-Labeling","Obfuscation-Vagueness-Confusion",
    "Questioning_the_Reputation","Red_Herring","Repetition","Slogans",
    "Straw_Man", "Whataboutism"
]

notes=pd.read_csv('../notes.csv', sep=',', skiprows=1)

# Load notes dataframe (already available)
# notes = pd.read_csv("notes.csv")  # if needed

# Persuasiveness = number of techniques used
notes["persuasiveness"] = notes[technique_cols].sum(axis=1)

# ------------------------------------------------------------
# 2. PROCESS RATING FILES IN STREAMING MODE TO COMPUTE AVERAGE HELPFULNESS PER NOTE
# ------------------------------------------------------------

helpfulness_map = {
    "NOT_HELPFUL": 1,
    "SOMEWHAT_HELPFUL": 2,
    "HELPFUL": 3
}

ratings_folder = "rankings"
rating_files = sorted([
    f for f in os.listdir(ratings_folder)
    if f.startswith("ratings") and f.endswith(".tsv")
])

# Dictionary to accumulate helpfulness sums and counts
helpfulness_sum = {}
helpfulness_count = {}

for fname in rating_files:
    fpath = os.path.join(ratings_folder, fname)
    print(f"Processing {fpath}...")

    # Load file chunk
    df = pd.read_csv(fpath, sep="\t")

    # Map categorical helpfulness to numeric
    df["helpfulness_num"] = df["helpfulnessLevel"].map(helpfulness_map)

    # Accumulate sums and counts per note
    for note_id, val in zip(df["noteId"], df["helpfulness_num"]):
        if pd.isna(val):
            continue
        helpfulness_sum[note_id] = helpfulness_sum.get(note_id, 0) + val
        helpfulness_count[note_id] = helpfulness_count.get(note_id, 0) + 1

# Build dataframe
avg_helpfulness = pd.DataFrame({
    "noteId": list(helpfulness_sum.keys()),
    "avg_helpfulness": [
        helpfulness_sum[nid] / helpfulness_count[nid]
        for nid in helpfulness_sum.keys()
    ]
})

# ------------------------------------------------------------
# 3. MERGE NOTES WITH HELPULNESS
# ------------------------------------------------------------

merged = notes.merge(avg_helpfulness, on="noteId", how="inner")

# ------------------------------------------------------------
# 4. TEST 1 — SPEARMAN CORRELATION
# ------------------------------------------------------------

rho, pval = spearmanr(merged["persuasiveness"], merged["avg_helpfulness"])
print("--------------------------------------------------")
print("SPEARMAN CORRELATION: PERSUASIVENESS vs HELPFULNESS")
print(f"Spearman rho = {rho:.4f}, p-value = {pval:.4e}")
print("--------------------------------------------------")

# ------------------------------------------------------------
# 5. TEST 2 — PER-TECHNIQUE MANN-WHITNEY TESTS
# ------------------------------------------------------------

results = []

for tech in technique_cols:
    group1 = merged.loc[merged[tech] == 1, "avg_helpfulness"]
    group0 = merged.loc[merged[tech] == 0, "avg_helpfulness"]

    if len(group1) > 0 and len(group0) > 0:
        stat, p = mannwhitneyu(group1, group0, alternative='two-sided')
        results.append((tech, stat, p))

# Sort by p-value
results = sorted(results, key=lambda x: x[2])

print("--------------------------------------------------")
print("TECHNIQUE-BY-TECHNIQUE MANN–WHITNEY U RESULTS")
for tech, stat, p in results:
    print(f"{tech:35s} U={stat:.1f}, p-value={p:.4e}")
print("--------------------------------------------------")



def cliffs_delta_from_U(U, n1, n0):
    return (2 * U) / (n1 * n0) - 1

tech_results = []

for tech in technique_cols:
    group1 = merged.loc[merged[tech] == 1, "avg_helpfulness"]
    group0 = merged.loc[merged[tech] == 0, "avg_helpfulness"]

    if len(group1) > 0 and len(group0) > 0:
        stat, p = mannwhitneyu(group1, group0, alternative='two-sided')
        delta = cliffs_delta_from_U(stat, len(group1), len(group0))
        tech_results.append((tech, stat, p, delta))

# Sort by effect size magnitude
tech_results = sorted(tech_results, key=lambda x: abs(x[3]), reverse=True)

for tech, U, p, delta in tech_results:
    print(f"{tech:35s} U={U:.1f}, p={p:.2e}, delta={delta:.4f}")
