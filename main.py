from services.requirement_loader import RequirementLoader
from services.tc_generator import TestCaseGenerator
from services.evaluator import Evaluator

loader = RequirementLoader()
generator = TestCaseGenerator()
evaluator = Evaluator()

requirements = loader.load_all_requirements()

for requirement in requirements:

    generated = generator.generate(
        requirement
    )

    evaluation = evaluator.evaluate(
        requirement,
        generated
    )

    print()
    print(f"Requirement: {requirement.requirement_id}")
    print(evaluation)