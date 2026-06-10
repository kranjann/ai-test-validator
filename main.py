from services.requirement_loader import RequirementLoader
from services.tc_generator import TestCaseGenerator

loader = RequirementLoader()
generator = TestCaseGenerator()

requirements = loader.load_all_requirements()

for requirement in requirements:

    generated = generator.generate(requirement)

    print()
    print(generated)