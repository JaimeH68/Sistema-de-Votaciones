from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.candidate import CandidateCreate, CandidateResponse
from app.models.candidate import Candidate
from app.models.voter import Voter
from app.db.database import SessionLocal

router = APIRouter(prefix="/candidates", tags=["Candidates"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=CandidateResponse)
def create_candidate(candidate: CandidateCreate, db: Session = Depends(get_db)):
    voter_match = db.query(Voter).filter(Voter.name == candidate.name).first()
    if voter_match:
        raise HTTPException(status_code=400, detail="This user is already registered as a voter.")

    db_candidate = Candidate(**candidate.dict())
    db.add(db_candidate)
    db.commit()
    db.refresh(db_candidate)
    return db_candidate

@router.get("/", response_model=list[CandidateResponse])
def get_candidates(db: Session = Depends(get_db)):
    return db.query(Candidate).all()