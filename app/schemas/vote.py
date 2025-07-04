from pydantic import BaseModel

class VoteCreate(BaseModel):
    voter_id: int
    candidate_id: int

class VoteStatistics(BaseModel):
    candidate_id: int
    name: str
    votes: int
    percentage: float

    model_config = {
        "from_attributes": True
    }