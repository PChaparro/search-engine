import os
import math
import time
from opensearchpy import OpenSearch
from interfaces import interfaces
from typing import List

# Connect to opensearch
open_search_client = OpenSearch(
    timeout=30,
    hosts=[
        {"host": os.getenv("OPENSEARCH_HOST"), "port": os.getenv("OPENSEARCH_PORT")}
    ],
    http_compress=True,
    http_auth=(os.getenv("OPENSEARCH_USER"), os.getenv("OPENSEARCH_PASSWORD")),
    use_ssl=False,
    verify_cers=False,
)

# Search using the knn algorithm from the user query vector
def get_results_from_vector(vector: List[float]) -> interfaces.ISearchResult:
    # Prepare the query
    open_search_query = {
        "size": 24,
        # Fields than will be sended as response
        "_source": ["url", "thumbnail", "title", "tags"],
        # Filter
        "query": {"bool": {"must": [{"knn": {"vector": {"vector": vector, "k": 24}}}]}},
    }

    # Perform the query on opensearch
    response = open_search_client.search(
        index="videos", body=open_search_query, request_timeout=64
    )

    # Parse results
    videos = [x["_source"] for x in response["hits"]["hits"]]
    return videos


# Get random results (to show when the page loads)
def get_random_videos() -> interfaces.ISearchResult:
    # Prepare the query
    open_search_query = {
        "size": 24,
        # Fields than will be sended as response
        "_source": ["url", "thumbnail", "title", "tags"],
        "query": {
            "function_score": {
                "functions": [{"random_score": {"seed": math.ceil(time.time())}}]
            }
        },
    }

    # Perform the query on opensearch
    response = open_search_client.search(
        index="videos", body=open_search_query, request_timeout=64
    )

    # Parse results
    videos = [x["_source"] for x in response["hits"]["hits"]]
    return videos
