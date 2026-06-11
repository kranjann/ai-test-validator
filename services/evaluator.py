from schemas.evaluation import EvaluationResult
from schemas.generated_test_case import GeneratedTestCase
from schemas.requirement import Requirement


class Evaluator:

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

        return 0.0

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

        overall_score = coverage_score

        return EvaluationResult(
            similarity_score=similarity_score,
            coverage_score=coverage_score,
            hallucination_detected=False,
            overall_score=overall_score,
            explanation="Coverage evaluation completed"
        )