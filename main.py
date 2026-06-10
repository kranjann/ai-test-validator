from services.requirement_loader import RequirementLoader
from services.tc_generator import TestCaseGenerator
from services.evaluation_service import EvaluationService

loader = RequirementLoader()
generator = TestCaseGenerator()
evaluator = EvaluationService()

requirements = loader.load_all_requirements()

for requirement in requirements:

    generated = generator.generate(requirement)

    print()
    print(generated)

    