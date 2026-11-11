from elasticsearch import Elasticsearch
import json
import os

input('**********************************************\nMake sure you have ElasticSearch container\nrunning on docker if you desire to run ES\non local host \n\n|Press ENTER to continue|\n**********************************************\n')

class bcolors:
    HEADER = '\033[95m'
    OKGREEN = '\033[92m'
    OKCYAN = '\033[96m'
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'

def main():
# --- ELASTISEARCH CONNECTION AND AUTHENTIFICATION ---
    ES_HOST = input("Enter Elasticsearch host (e.g., http://localhost:9200): ")
    ES_USER = input("Enter Elasticsearch username (press enter if connecting locally): ")
    ES_PASS = input("Enter Elasticsearch password (press enter if connecting locally): ")
    es = Elasticsearch(ES_HOST, basic_auth=(ES_USER, ES_PASS))

# --- DIRECTORY --- 
    def dir():

        # Get the current working directory
        current_dir = os.getcwd()
        print(bcolors.OKCYAN +"\nCurrent directory:", current_dir)

        # Change to a directory
        while True:
            new_dir = input(bcolors.ENDC + '\nInput directory path where JSON file is located:') 
            try:
                os.chdir(new_dir)
                break
            except FileNotFoundError:
                print(bcolors.WARNING +'Path not found')
                continue
            except OSError:
                print(bcolors.WARNING +'Incorrect syntax. Use X:/Xxxxxx/xxx...')
                continue

        print(bcolors.OKCYAN +"\n[changing directory...]")
        print(bcolors.OKCYAN +"Directory changed to:"+ os.getcwd())

# --- INDEXING AND MAPPING ---
    def index():

        # User selection
        global INDEX_NAME
        INDEX_NAME = input(bcolors.ENDC + '\nInput desired name of Elasticsearch index where your documents will be stored: ')

        # Delete index if it exists 
        if es.indices.exists(index=INDEX_NAME):
            es.indices.delete(index=INDEX_NAME)
            print(f"Deleted existing index: {INDEX_NAME}")

        # Define mapping
        mapping = {
            "mappings": {
                "properties": {
                    "Country": {"type": "keyword"},
                    "Region": {"type": "keyword"},
                    "Happiness_Rank": {"type": "integer"},
                    "Happiness_Score": {"type": "float"},
                    "Economy_(GDP_per_Capita)": {"type": "float"},
                    "Family": {"type": "float"},
                    "Freedom": {"type": "float"},
                    "Generosity": {"type": "float"},
                    "Dystopia_Residual": {"type": "float"},
                    "Healthy_life_expectancy": {"type": "float"},
                    "Perceptions_of_corruption": {"type": "float"},
                    "report_year": {"type": "integer"}, 
                    "Social_support": {"type": "float"},
                }
            }
        }

        # Create index
        es.indices.create(index=INDEX_NAME, body=mapping)
        print(f"Created index: {INDEX_NAME}")

# --- JSON READING ---
    def jsonRead():

        # User prompt
        JSON_FILE = input(bcolors.ENDC + '\nInput name of JSON file you would like to read*(include .json): ') 
        if not os.path.exists(JSON_FILE):
            raise FileNotFoundError(f"File '{JSON_FILE}' not found.")

        # Open file 
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Into es
        for i, doc in enumerate(data):
            es.index(index=INDEX_NAME, id=i+1, document=doc)

    dir()
    index()
    jsonRead()

if __name__ == "__main__":
    main()