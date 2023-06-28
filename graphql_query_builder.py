import os
import openai
from dotenv import load_dotenv
import pandas as pd
import re


class QueryBuilder:
    def __init__(self, openai_key):
        openai.api_key = openai_key

    def query_chatgpt_role(self, persona, query):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            # temperature=0.1,
            messages=[{"role": "system",
                       "content": persona},
                      {"role": "user",
                       "content": query}])
        return completion

    def unpack_res(self, r):
        return r['choices'][0]['message']['content']
