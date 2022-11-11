from typing import List
from sentence_transformers import SentenceTransformer
transformer_model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

# vectorize: Transform user query into vector representation
def vectorize(criteria: str) -> List[float]:
    vector = transformer_model.encode(criteria)
    return vector.tolist()
