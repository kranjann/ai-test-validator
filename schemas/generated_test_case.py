from pydantic import BaseModel


class GeneratedTestCase(BaseModel):
    requirement_id: str
    test_cases: list[str]