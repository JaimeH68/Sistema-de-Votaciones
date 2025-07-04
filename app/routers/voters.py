from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.voter import VoterCreate, VoterResponse
from app.models.voter import Voter
from app.models.candidate import Candidate
from app.db.database import SessionLocal

router = APIRouter(prefix="/voters", tags=["Voters"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=VoterResponse)
def create_voter(voter: VoterCreate, db: Session = Depends(get_db)):
    if db.query(Voter).filter(Voter.email == voter.email).first():
        raise HTTPException(status_code=400, detail="Email is already registered as a voter.")

    candidate_match = db.query(Candidate).filter(Candidate.name == voter.name).first()
    if candidate_match:
        raise HTTPException(status_code=400, detail="This user is already registered as a candidate.")

    db_voter = Voter(**voter.dict())
    db.add(db_voter)
    db.commit()
    db.refresh(db_voter)
    return db_voter

@router.get("/", response_model=list[VoterResponse])
def get_voters(db: Session = Depends(get_db)):
    return db.query(Voter).all()

@router.get("/{voter_id}", response_model=VoterResponse)
def get_voter(voter_id: int, db: Session = Depends(get_db)):
    voter = db.query(Voter).filter(Voter.id == voter_id).first()
    if not voter:
        raise HTTPException(status_code=404, detail="Voter not found")
    return voter

@router.delete("/{voter_id}")
def delete_voter(voter_id: int, db: Session = Depends(get_db)):
    voter = db.query(Voter).filter(Voter.id == voter_id).first()
    if not voter:
        raise HTTPException(status_code=404, detail="Voter not found")
    db.delete(voter)
    db.commit()
    return {"message": "Voter deleted"}