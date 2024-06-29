from pydantic import BaseModel, Field
from typing import List

class ChildrenInfo(BaseModel):
    sex: str
    age: int = Field(gt=0, le=100)
    interests: List[str]