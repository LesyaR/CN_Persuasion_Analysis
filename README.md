1. Language Distribution statistics.

## Distribution of Languages in CN Dataset (Table 1)

| Language              | Count   | Language                | Count |
|----------------------|--------:|------------------------|------:|
| English              | 1,224,201 | Latvian                | 160 |
| Spanish              | 180,752   | Tamil                  | 157 |
| Japanese             | 155,885   | Afrikaans              | 136 |
| Portuguese           | 111,374   | Somali                 | 109 |
| French               | 96,458    | Ganda (Luganda)        | 88 |
| German               | 52,862    | Zulu                   | 76 |
| Latin                | 27,346    | Basque                 | 72 |
| Turkish              | 18,785    | Marathi                | 68 |
| Polish               | 17,735    | Irish (Gaelic)         | 52 |
| Italian              | 15,418    | Icelandic              | 48 |
| Yoruba               | 14,829    | Ukrainian              | 36 |
| Dutch                | 13,503    | Vietnamese             | 17 |
| Hebrew               | 10,328    | Mongolian              | 14 |
| Welsh                | 6,845     | Azerbaijani            | 12 |
| Danish               | 5,875     | Telugu                 | 10 |
| Esperanto            | 5,318     | Macedonian             | 7 |
| Tswana               | 5,225     | Bengali                | 4 |
| Indonesian           | 5,029     | Gujarati               | 3 |
| Arabic               | 5,014     | Punjabi                | 1 |
| Catalan              | 4,509     | Kazakh                 | 1 |
| Finnish              | 3,891     |                        |    |
| Czech                | 3,846     |                        |    |
| Swedish              | 3,679     |                        |    |
| Tsonga               | 2,356     |                        |    |
| Croatian             | 2,030     |                        |    |
| Southern Sotho       | 1,969     |                        |    |
| Persian              | 1,954     |                        |    |
| Xhosa                | 1,905     |                        |    |
| Slovak               | 1,337     |                        |    |
| Albanian             | 1,273     |                        |    |
| Malay                | 1,167     |                        |    |
| Romanian             | 1,150     |                        |    |
| Norwegian Bokmål     | 1,092     |                        |    |
| Tagalog              | 1,002     |                        |    |
| Thai                 | 980       |                        |    |
| Bosnian              | 917       |                        |    |
| Norwegian Nynorsk    | 896       |                        |    |
| Russian              | 758       |                        |    |
| Hindi                | 752       |                        |    |
| Greek                | 710       |                        |    |
| Korean               | 553       |                        |    |
| Slovenian            | 549       |                        |    |
| Chinese              | 530       |                        |    |
| Shona                | 458       |                        |    |
| Estonian             | 446       |                        |    |
| Māori                | 442       |                        |    |
| Urdu                 | 427       |                        |    |
| Swahili              | 304       |                        |    |
| Lithuanian           | 288       |                        |    |
| Hungarian            | 251       |                        |    |
| Serbian              | 201       |                        |    |
| Unknown              | 200       |                        |    |
| Bulgarian            | 172       |                        |    |

---

## Distribution of Languages in CN Dataset (Table 2)

| Language              | Count   | Language                | Count |
|----------------------|--------:|------------------------|------:|
| English              | 358,152  | Afrikaans              | 945 |
| Spanish              | 76,652   | Vietnamese             | 874 |
| Portuguese           | 46,825   | Chinese (Simplified)   | 794 |
| German               | 26,580   | Tagalog                | 565 |
| French               | 24,015   | Norwegian              | 475 |
| Polish               | 16,867   | Swahili                | 296 |
| Arabic               | 15,226   | Turkish                | 290 |
| Korean               | 11,480   | Thai                   | 277 |
| Ukrainian            | 10,247   | Urdu                   | 272 |
| Greek                | 10,119   | Somali                 | 270 |
| Romanian             | 8,877    | Swedish                | 270 |
| Russian              | 8,754    | Estonian               | 270 |
| Italian              | 7,930    | Slovenian              | 223 |
| Indonesian           | 7,875    | Macedonian             | 208 |
| Catalan              | 4,483    | Japanese               | 165 |
| Lithuanian           | 4,364    | Welsh                  | 162 |
| Bulgarian            | 4,296    | Persian                | 95 |
| Dutch                | 4,114    | Hebrew                 | 70 |
| Latvian              | 3,594    | Marathi                | 36 |
| Hindi                | 3,156    | Telugu                 | 34 |
| Bengali              | 3,081    | Albanian               | 29 |
| Croatian             | 3,059    | Malayalam              | 23 |
| Czech                | 2,865    | Kannada                | 19 |
| Slovak               | 2,562    | Tamil                  | 18 |
| Unknown              | 2,292    | Nepali                 | 12 |
| Chinese (Traditional)| 2,201    | Punjabi                | 9 |
| Hungarian            | 1,874    | Gujarati               | 7 |
| Danish               | 1,818    |                        |    |
| Finnish              | 1,280    |                        |    |



## Reproducing the Analysis

1. **Download the datasets**  
   Download the following datasets:
   - CN  
   - DBKF  
   - EUvsDisinfo
  
   To extract the data for DBKF debunks, run the dbkf_query.rq in the following SPARQL end-point: https://dbkf.ontotext.com/graphdb/sparql
   You can then export the results in the preferred format.

3. **Infer the persuasion techniques**

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
