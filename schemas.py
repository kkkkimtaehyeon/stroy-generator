from pydantic import BaseModel, Field
from typing import List, Optional

class ChildrenInfo(BaseModel):
    sex: str
    age: int = Field(gt=0, le=100)
    interests: List[str]


class StorySource(BaseModel):
    prompt: str
    image_urls: Optional[List[str]]

class Interests(BaseModel):
    interest: str
