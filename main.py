# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from graphql_query_builder import QueryBuilder
from ask_open_targets import AskOpenTargets
from utils import extract_values
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(
        """
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
        """
    )
    selected_prompt = input(""" Please input the prompt number: """)
    # create a graphql query using GPT3.5
    apikey = "openai_apikey"
    querybuilder = QueryBuilder(apikey)
    open_target = AskOpenTargets("https://api.platform.opentargets.org/api/v4/graphql")

    # read from file
    with open(f"./prompts/prompt_{selected_prompt}.txt", "r") as f:
        persona = f.read()
    while True:
        question = input("Please input a natural language question: ")
        # print the generated GraphQL query
        chatgpt_response = querybuilder.query_chatgpt_role(persona, question)
        graphql_query = querybuilder.unpack_res(chatgpt_response)
        print(graphql_query)
        # retrieve data from opentargets using the graphql api
        response = open_target.search(graphql_query)

        hits_list = response["data"]["search"]["hits"][0]

        if selected_prompt == "1":
            disease_list = extract_values(hits_list, "disease")
            for i, j in enumerate(disease_list):
                print(f"{i + 1}. {j['name']}")
        elif selected_prompt == "2":
            target_list = extract_values(hits_list, "approvedName")
            for i, j in enumerate(target_list):
                print(f"{i + 1}. {j}")
        elif selected_prompt == "3":
            target_list = extract_values(hits_list, "approvedName")
            for i, j in enumerate(target_list):
                print(f"{i + 1}. {j}")
        elif selected_prompt == "4":
            target_list = extract_values(hits_list, "approvedName")
            for i, j in enumerate(target_list):
                print(f"{i + 1}. {j}")
        elif selected_prompt == "5":
            disease_list = extract_values(hits_list, "disease")
            for i, j in enumerate(disease_list):
                print(f"{i + 1}. {j['name']}")
        else:
            print(response)
