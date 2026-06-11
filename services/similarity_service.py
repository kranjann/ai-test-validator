from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim


class SimilarityService:

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def generate_embedding(self, text: str):

        return self.model.encode(text)

    def calculate_similarity(
        self,
        embedding1,
        embedding2
    ) -> float:

        similarity = cos_sim(
            embedding1,
            embedding2
        )

        return float(similarity)