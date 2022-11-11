from typing import List, TypedDict

# Video 'interface'
class Video(TypedDict):
    url: str
    thumbnail: str
    title: str
    tags: List[str]


# Search results 'interface'
ISearchResult = List[Video]
