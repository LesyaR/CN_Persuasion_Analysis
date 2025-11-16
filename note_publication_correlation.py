#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 14:52:08 2025

@author: olesya
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 15:37:19 2025

@author: olesya
"""

import pandas as pd
from scipy.stats import chi2_contingency


notes=pd.read_csv('notes.csv')

# Step 3: Load note statuses
notestatuses = pd.read_csv("notestatuses.tsv")


# Step 1: Load your notes dataframe (replace with your actual loading if needed)
# notes = pd.read_csv("notes.csv")  # example
# Assuming you already have `notes` dataframe

# List of persuasion technique columns
technique_cols = [
    "Appeal_to_Authority","Appeal_to_Fear-Prejudice","Appeal_to_Hypocrisy",
    "Appeal_to_Popularity","Appeal_to_Time","Appeal_to_Values","Causal_Oversimplification",
    "Consequential_Oversimplification","Conversation_Killer","Doubt",
    "Exaggeration-Minimisation","False_Dilemma-No_Choice","Flag_Waving",
    "Guilt_by_Association","Loaded_Language","Name_Calling-Labeling",
    "Obfuscation-Vagueness-Confusion","Questioning_the_Reputation","Red_Herring",
    "Repetition","Slogans","Straw_Man","Whataboutism"
]

# Step 2: Filter notes for the specific classification
filtered_notes = notes[notes['classification'] == 'MISINFORMED_OR_POTENTIALLY_MISLEADING']



# Step 4: Left join notes with note statuses on noteId
merged = filtered_notes.merge(notestatuses[['noteId', 'lockedStatus']], on='noteId', how='left')

# Step 5: Count and remove rows with blank lockedStatus
num_blank = merged['lockedStatus'].isna().sum()
print(f"Number of rows removed due to blank lockedStatus: {num_blank}")

merged = merged.dropna(subset=['lockedStatus'])

# Step 6: Create a column indicating if any persuasion technique is present
merged['has_persuasion'] = merged[technique_cols].sum(axis=1) > 0

# Step 7: Create a contingency table between has_persuasion and lockedStatus
contingency = pd.crosstab(merged['has_persuasion'], merged['lockedStatus'])
print("\nContingency Table:")
print(contingency)

# Step 8: Perform chi-square test
chi2, p, dof, expected = chi2_contingency(contingency)
print(f"\nChi-square statistic: {chi2:.4f}")
print(f"P-value: {p:.4f}")
print(f"Degrees of freedom: {dof}")
print("\nExpected frequencies:")
print(pd.DataFrame(expected, index=contingency.index, columns=contingency.columns))
