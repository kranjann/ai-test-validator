from schemas.evaluation import EvaluationResult
from schemas.generated_test_case import GeneratedTestCase
from schemas.requirement import Requirement


class Evaluator:

    def evaluate(
        self,
        requirement: Requirement,
        generated: GeneratedTestCase
    ) -> EvaluationResult:

        expected_count = len(
            requirement.ground_truth
        )

        generated_count = len(
            generated.test_cases
        )

        if expected_count == 0:
            coverage_score = 0.0
        else:
            coverage_score = (
                generated_count / expected_count
            ) * 100

        overall_score = coverage_score

        return EvaluationResult(
            similarity_score=0.0,
            coverage_score=coverage_score,
            hallucination_detected=False,
            overall_score=overall_score,
            explanation="Coverage evaluation completed"
        )