from sqlalchemy import Column, Integer, String
from database import Base

# Define To Do class inheriting from Base
class Carsku(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    nama = Column(String(50))
    price = Column(Integer)