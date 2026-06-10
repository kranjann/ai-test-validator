from services.requirement_loader import RequirementLoader

loader = RequirementLoader()

requirements = loader.load_all_requirements()

for requirement in requirements:
    print(requirement)