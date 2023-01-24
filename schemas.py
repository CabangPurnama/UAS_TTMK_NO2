from pydantic import BaseModel

# Create ToDo Schema (Pydantic Model)
class CreateCars(BaseModel):
    nama: str
    price: int

# Complete ToDo Schema (Pydantic Model)
class Cars(BaseModel):
    id: int
    nama: str
    price: int

    class Config:
        orm_mode = True