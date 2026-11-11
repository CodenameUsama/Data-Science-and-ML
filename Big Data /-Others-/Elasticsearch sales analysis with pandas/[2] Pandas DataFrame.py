from elasticsearch import Elasticsearch
import pandas as pd

# Connect to Elasticsearch
es = Elasticsearch('http://localhost:9200')

# Index name
index_name = 'amazon_sales'

# Query to get all documents 
response = es.search(
    index=index_name,
    body={
        'query': {
            'match_all': {}
        },
        'size': 251
    }
)

# Extract _source (actual doc content)
records = [doc['_source'] for doc in response['hits']['hits']]

# Load into DataFrame
df = pd.DataFrame(records)

# Show DataFrame
print(df.head(25))