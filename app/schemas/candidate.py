from pydantic import BaseModel
from typing import Optional

class CandidateCreate(BaseModel):
    name: str
    party: Optional[str] = None

class CandidateResponse(BaseModel):
    id: int
    name: str
    party: Optional[str]
    votes: int

    model_config = {
        "from_attributes": True
    }