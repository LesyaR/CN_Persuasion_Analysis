Reproducing the analysis

1. Download the four datasets (CN, DBKF,  and EUvsDisinfo). 

2. Infer the persuasion techniques.
a. Go to the GATE Cloud Persuasion API. Create an account, login, and create API keys. Save your api keys in a file named '.env' in the root directory of this repository. The .env file should contain the variable GATE_API_KEY="<YOUR_KEY>".
b. Run the inference script calling the Persuasion API:

python3 infer_api.py
