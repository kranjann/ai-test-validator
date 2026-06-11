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

        coverage_score = (
            generated_count / expected_count
        ) * 100

        return min(
            coverage_score,
            100.0
        )

    def calculate_similarity_score(
        self,
        requirement: Requirement,
        generated: GeneratedTestCase
    ) -> float:

        if not generated.test_cases:
            return 0.0

        scores = []

        generated_embeddings = {
            tc: self.similarity_service.generate_embedding(tc)
            for tc in generated.test_cases
        }

        ground_truth_embeddings = {
            tc: self.similarity_service.generate_embedding(tc)
            for tc in requirement.ground_truth
        }

        for generated_tc in generated.test_cases:

            generated_embedding = generated_embeddings[
                generated_tc
            ]

            best_score = 0.0

            for ground_truth_tc in requirement.ground_truth:

                ground_truth_embedding = (
                    ground_truth_embeddings[
                        ground_truth_tc
                    ]
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

        return (
            sum(scores) / len(scores)
        ) * 100

    def detect_hallucination(
        self,
        requirement: Requirement,
        generated: GeneratedTestCase
    ) -> bool:

        if not generated.test_cases:
            return False

        threshold = 0.50

        requirement_embedding = (
            self.similarity_service.generate_embedding(
                requirement.requirement
            )
        )

        for test_case in generated.test_cases:

            test_case_embedding = (
                self.similarity_service.generate_embedding(
                    test_case
                )
            )

            similarity = (
                self.similarity_service.calculate_similarity(
                    requirement_embedding,
                    test_case_embedding
                )
            )

            if similarity < threshold:

                return True

        return False

    def calculate_overall_score(
        self,
        coverage_score: float,
        similarity_score: float,
        hallucination_detected: bool
    ) -> float:

        score = (
            coverage_score +
            similarity_score
        ) / 2

        if hallucination_detected:

            score -= 25

        return max(
            score,
            0.0
        )

    def generate_root_cause(
        self,
        coverage_score: float,
        similarity_score: float,
        hallucination_detected: bool
    ) -> str:

        if coverage_score == 0:

            return (
                "No test cases were generated "
                "for the requirement."
            )

        if hallucination_detected:

            return (
                "Generated output contains "
                "hallucinated test cases "
                "unrelated to the requirement."
            )

        if similarity_score < 70:

            return (
                "Generated test cases do not "
                "closely match the ground truth."
            )

        if coverage_score < 100:

            return (
                "Generated output does not "
                "cover all expected scenarios."
            )

        return (
            "Evaluation completed successfully."
        )

    def evaluate(
        self,
        requirement: Requirement,
        generated: GeneratedTestCase
    ) -> EvaluationResult:

        coverage_score = (
            self.calculate_coverage_score(
                requirement,
                generated
            )
        )

        similarity_score = (
            self.calculate_similarity_score(
                requirement,
                generated
            )
        )

        hallucination_detected = (
            self.detect_hallucination(
                requirement,
                generated
            )
        )

        overall_score = (
            self.calculate_overall_score(
                coverage_score,
                similarity_score,
                hallucination_detected
            )
        )

        root_cause = (
            self.generate_root_cause(
                coverage_score,
                similarity_score,
                hallucination_detected
            )
        )

        return EvaluationResult(
            similarity_score=similarity_score,
            coverage_score=coverage_score,
            hallucination_detected=hallucination_detected,
            overall_score=overall_score,
            explanation=(
                "Coverage, similarity and "
                "hallucination evaluation completed"
            ),
            root_cause=root_cause
        )