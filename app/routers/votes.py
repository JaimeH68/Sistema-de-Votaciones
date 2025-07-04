from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.schemas.vote import VoteCreate
from app.models.vote import Vote
from app.models.voter import Voter
from app.models.candidate import Candidate
from app.db.database import SessionLocal

router = APIRouter(prefix="/votes", tags=["Votes"])
templates = Jinja2Templates(directory="app/templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", status_code=201)
def submit_vote(vote: VoteCreate, db: Session = Depends(get_db)):
    voter = db.query(Voter).filter(Voter.id == vote.voter_id).first()
    if not voter:
        raise HTTPException(status_code=404, detail="Voter not found")
    if voter.has_voted:
        raise HTTPException(status_code=400, detail="Voter has already voted")

    candidate = db.query(Candidate).filter(Candidate.id == vote.candidate_id).first()
    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")

    new_vote = Vote(**vote.dict())
    db.add(new_vote)

    voter.has_voted = True
    candidate.votes += 1

    db.commit()
    return {"message": "Vote submitted successfully"}

@router.get("/", response_model=list[VoteCreate])
def get_votes(db: Session = Depends(get_db)):
    return db.query(Vote).all()

@router.get("/statistics", response_class=HTMLResponse)
def vote_statistics(request: Request, db: Session = Depends(get_db)):
    total_votes = db.query(Vote).count()
    total_voters = db.query(Voter).count()
    voters_who_voted = db.query(Voter).filter(Voter.has_voted == True).count()
    candidates = db.query(Candidate).all()
    statistics = []
    for c in candidates:
        percentage = (c.votes / total_votes) * 100 if total_votes > 0 else 0
        statistics.append({
            "candidate_id": c.id,
            "name": c.name,
            "votes": c.votes,
            "percentage": round(percentage, 2)
        })
    return templates.TemplateResponse("results.html", {"request": request, "statistics": statistics, "total_voters": total_voters, "voters_who_voted": voters_who_voted})