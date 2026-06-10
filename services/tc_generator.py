import re

from schemas.requirement import Requirement
from schemas.generated_test_case import GeneratedTestCase


class TestCaseGenerator:

    def generate(
        self,
        requirement: Requirement
    ) -> GeneratedTestCase:

        test_cases = []

        text = requirement.requirement.lower()

        if "between" in text:

            numbers = re.findall(r"\d+", text)

            if len(numbers) == 2:

                min_value = numbers[0]
                max_value = numbers[1]

                test_cases.extend([
                    f"Verify value {min_value} is accepted",
                    f"Verify value {max_value} is accepted",
                    f"Verify value below {min_value} is rejected",
                    f"Verify value above {max_value} is rejected"
                ])

        return GeneratedTestCase(
            requirement_id=requirement.requirement_id,
            test_cases=test_cases
        )