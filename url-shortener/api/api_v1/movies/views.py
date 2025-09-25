import random
from typing import Annotated

from fastapi import APIRouter, Depends, status, Form

from .crud import MOVIES
from .dependencies import get_movie
from schemas.movie import Movie

router = APIRouter(
    prefix="/movies",
    tags=["Movies"],
)


@router.get(
    "/movies",
    response_model=list[Movie],
)
def read_movies_list():
    return MOVIES


@router.get(
    "/movies/{movie_id}",
    response_model=Movie,
)
def read_movie_details(
    movie: Annotated[
        Movie,
        Depends(get_movie),
    ],
):
    return movie


@router.post(
    "/",
    response_model=Movie,
    status_code=status.HTTP_201_CREATED,
)
def create_movie(
    name: Annotated[str, Form()],
    description: Annotated[str, Form()],
    rating: Annotated[float, Form()],
):
    return Movie(
        id=random.randint(1, 100),
        name=name,
        description=description,
        rating=rating,
    )
