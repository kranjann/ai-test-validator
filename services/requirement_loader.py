import json
from pathlib import Path

from schemas.requirement import Requirement


class RequirementLoader:

    def load_requirement(self, file_path: str) -> Requirement:

        with open(file_path, "r") as file:
            data = json.load(file)

        return Requirement(**data)

    def load_all_requirements(self) -> list[Requirement]:

        requirements = []

        requirements_path = Path("data/requirements")

        for file_path in sorted(requirements_path.glob("*.json")):

            requirement = self.load_requirement(str(file_path))

            requirements.append(requirement)

        return requirements