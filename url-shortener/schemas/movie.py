from pydantic import BaseModel


class MovieBase(BaseModel):
    id: int
    name: str
    description: str
    rating: float


class Movie(MovieBase):
    """
    Модель фильма
    """
