from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from app.db.database import Base

class Vote(Base):
    __tablename__ = "votes"
    id = Column(Integer, primary_key=True, index=True)
    voter_id = Column(Integer, ForeignKey("voters.id"), nullable=False, unique=True)
    candidate_id = Column(Integer, ForeignKey("candidates.id"), nullable=False)
    __table_args__ = (UniqueConstraint("voter_id", name="unique_voter_vote"),)