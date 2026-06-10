from pydantic import BaseModel


class EvaluationResult(BaseModel):
    similarity_score: float
    coverage_score: float
    hallucination_detected: bool
    overall_score: float