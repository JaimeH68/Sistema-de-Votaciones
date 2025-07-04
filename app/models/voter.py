from sqlalchemy import Column, Integer, String, Boolean
from app.db.database import Base

class Voter(Base):
    __tablename__ = "voters"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    has_voted = Column(Boolean, default=False)