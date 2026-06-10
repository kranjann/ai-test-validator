from pydantic import BaseModel
from typing import List


class Requirement(BaseModel):
    requirement_id: str
    requirement: str
    ground_truth: List[str]