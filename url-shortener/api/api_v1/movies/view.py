from typing import Annotated

from fastapi import APIRouter, Depends

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
