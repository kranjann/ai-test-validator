import re

from schemas.evaluation import EvaluationResult


class EvaluationService:

    def _normalize(self, text: str) -> str:
        """
        Convert different phrasings into a common scenario format.

        Examples:
        "Verify age 18 is accepted"
        "Verify value 18 is accepted"

        Both become:
        "18 accepted"
        """

        text = text.lower()

        numbers = re.findall(r"\d+", text)

        number = numbers[0] if numbers else ""

        if "below" in text:
            return f"below {number} rejected"

        if "above" in text:
            return f"above {number} rejected"

        if "accepted" in text:
            return f"{number} accepted"

        return text

    def evaluate(
        self,
        ground_truth: list[str],
        generated_cases: list[str]
    ) -> EvaluationResult:

        expected_scenarios = {
            self._normalize(test_case)
            for test_case in ground_truth
        }

        generated_scenarios = {
            self._normalize(test_case)
            for test_case in generated_cases
        }

        matched_count = len(
            expected_scenarios.intersection(
                generated_scenarios
            )
        )

        coverage_score = (
            matched_count / len(expected_scenarios) * 100
            if expected_scenarios
            else 0
        )

        return EvaluationResult(
            similarity_score=0.0,
            coverage_score=round(
                coverage_score,
                2
            ),
            hallucination_detected=False,
            overall_score=round(
                coverage_score,
                2
            ),
            explanation=(
                f"Matched {matched_count} "
                f"of {len(expected_scenarios)} "
                f"expected scenarios."
            )
        )