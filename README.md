## Reproducing the Analysis

1. **Download the datasets**  
   Download the following datasets:
   - CN  
   - DBKF  
   - EUvsDisinfo  

2. **Infer the persuasion techniques**

   a. **Set up the GATE Cloud Persuasion API**  
   - Go to the [GATE Cloud Persuasion API](https://gate.ac.uk/cloud) website.  
   - Create an account, log in, and generate your API keys.  
   - Save your API keys in a file named `.env` in the root directory of this repository.  
     The `.env` file should contain the following variable:  
     ```env
     GATE_API_KEY="<YOUR_KEY>"
     ```

   b. **Run the inference script**  
   Call the Persuasion API using the following command:
   ```bash
   python3 infer_api.py
