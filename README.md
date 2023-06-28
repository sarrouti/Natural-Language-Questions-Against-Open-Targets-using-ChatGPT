# Natural-Language-Questions-Against-Open-Targets-using-ChatGPT
Natural Language Questions Against Open Targets using ChatGPT




### Installation:
pip install -r requirements.txt

### Running Tests:
	a. "main.py" is the file that you will need to run the pipeline.
	b. Please make sure to give the openai apikey in main.py
		apikey = "api_key"
	
### PROMPTS:
The current pipeline can answer the following promopts:
        ## PROMPT_1:
        This prompt can be used to convert natural language questions asking to find the top n diseases
        associated with a given gene name:
        e.g., what are the top 5 diseases associated with gene PD-1?
        
        ## PROMPT_2:
        This prompt can be used to convert natural language questions asking to find
        the targets of a given drug name:
        e.g., What are the targets of vorinostat?
        
        ## PROMPT_3:
        This prompt can be used to convert natural language questions asking to find
        drugs that are used to treat a given disease:
        e.g., Find drugs that are used for treating ulcerative colitis?
        
        ## PROMPT_4:
        This prompt can be used to convert natural language questions asking to find
        targets that are associated with a given disease:
        e.g., Find targets associated with the disease ulcerative colitis.
        
        ## PROMPT_5:
        This prompt can be used to convert natural language questions asking to find
        diseases that are associated with genes targeted by a given drug:
        e.g., Which diseases are associated with the genes targeted by fasudil? 
        
        Which prompt you would like to use?
                    1: prompt_1
                    2: prompt_2
                    3: prompt_3
                    4: prompt_4
                    5: prompt_5   
 
    
