#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 11:11:29 2025

@author: olesya
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 19:46:31 2025

@author: olesya
"""

import pandas as pd
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest



notes=pd.read_csv('notes.csv', sep=',', skiprows=1)



dbkf=pd.read_csv('dbkf.csv', sep=',', skiprows=1)


euvsds=pd.read_csv('euvsds.csv', sep=',', skiprows=1)

# --- technique columns ---

technique_cols = [
    "Appeal_to_Authority","Appeal_to_Fear-Prejudice","Appeal_to_Hypocrisy","Appeal_to_Popularity",
    "Appeal_to_Time","Appeal_to_Values","Causal_Oversimplification","Consequential_Oversimplification",
    "Conversation_Killer","Doubt","Exaggeration-Minimisation","False_Dilemma-No_Choice","Flag_Waving",
    "Guilt_by_Association","Loaded_Language","Name_Calling-Labeling","Obfuscation-Vagueness-Confusion",
    "Questioning_the_Reputation","Red_Herring","Repetition","Slogans","Straw_Man","Whataboutism"
]

results = []

for col in technique_cols:
    # Notes vs DBKF
    count = [notes[col].sum(), dbkf[col].sum()]
    nobs = [len(notes), len(dbkf)]
    stat_nd, p_nd = proportions_ztest(count, nobs, alternative='larger')  # one-sided: notes > dbkf

    # Notes vs EUVSDS
    count = [notes[col].sum(), euvsds[col].sum()]
    nobs = [len(notes), len(euvsds)]
    stat_ne, p_ne = proportions_ztest(count, nobs, alternative='larger')  # one-sided: notes > euvsds

    results.append({
        "Technique": col,
        "Notes_vs_DBKF_Statistic": stat_nd,
        "Notes_vs_DBKF_pvalue": p_nd,
        "Notes_vs_EUVSDS_Statistic": stat_ne,
        "Notes_vs_EUVSDS_pvalue": p_ne
    })

results_df = pd.DataFrame(results).set_index("Technique")
print(results_df)