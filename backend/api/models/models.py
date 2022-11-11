import os
from opensearchpy import OpenSearch
from interfaces import interfaces
from typing import List

# Connect to opensearch
open_search_client = OpenSearch(
        timeout = 30, 
        hosts = [{'host': os.getenv('OPENSEARCH_HOST'), 'port': os.getenv('OPENSEARCH_PORT')}],
        http_compress = True, 
        http_auth = (os.getenv('OPENSEARCH_USER'), os.getenv('OPENSEARCH_PASSWORD')),
        use_ssl = False, 
        verify_cers = False,
)

def get_results_from_vector(vector: List[float]) -> interfaces.ISearchResult:
    open_search_query = {
        'size': 24, 
        # Fields than will be sended as response
        '_source': ['url', 'thumbnail', 'title', 'tags'],
        # Filter
        "query": {
            "bool": {
                'must': [
                    {'knn': {
                        "vector": {
                            "vector": vector,
                            "k": 24
                        }
                    }}
                ]
            }
        }
    }

    response = open_search_client.search(
        index = 'videos',
        body = open_search_query,
        request_timeout = 64
    )

    videos = [x['_source'] for x in response['hits']['hits']]
    return videos
