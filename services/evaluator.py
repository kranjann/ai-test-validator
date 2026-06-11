from services.similarity_service import SimilarityService

from schemas.evaluation import EvaluationResult
from schemas.generated_test_case import GeneratedTestCase
from schemas.requirement import Requirement


class Evaluator:

    def __init__(self):

        self.similarity_service = SimilarityService()

    def calculate_coverage_score(
        self,
        requirement: Requirement,
        generated: GeneratedTestCase
    ) -> float:

        expected_count = len(
            requirement.ground_truth
        )

        generated_count = len(
            generated.test_cases
        )

        if expected_count == 0:
            return 0.0

        return (
            generated_count / expected_count
        ) * 100

    def calculate_similarity_score(
        self,
        requirement: Requirement,
        generated: GeneratedTestCase
    ) -> float:

        scores = []

        for generated_tc in generated.test_cases:

            generated_embedding = (
                self.similarity_service.generate_embedding(
                    generated_tc
                )
            )

            best_score = 0.0

            for ground_truth_tc in requirement.ground_truth:

                ground_truth_embedding = (
                    self.similarity_service.generate_embedding(
                        ground_truth_tc
                    )
                )

                similarity = (
                    self.similarity_service.calculate_similarity(
                        generated_embedding,
                        ground_truth_embedding
                    )
                )

                best_score = max(
                    best_score,
                    similarity
                )

            scores.append(best_score)

        if not scores:
            return 0.0

        return (
            sum(scores) / len(scores)
        ) * 100

    def evaluate(
        self,
        requirement: Requirement,
        generated: GeneratedTestCase
    ) -> EvaluationResult:

        coverage_score = self.calculate_coverage_score(
            requirement,
            generated
        )

        similarity_score = self.calculate_similarity_score(
            requirement,
            generated
        )

        overall_score = (
            coverage_score + similarity_score
        ) / 2

        return EvaluationResult(
            similarity_score=similarity_score,
            coverage_score=coverage_score,
            hallucination_detected=False,
            overall_score=overall_score,
            explanation="Coverage and similarity evaluation completed"
        )