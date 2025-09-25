from fastapi import HTTPException, status

from .crud import MOVIES
from schemas.movie import Movie


def get_movie(
    movie_id: int,
) -> Movie:
    movie: Movie | None = next(
        (movie for movie in MOVIES if movie.id == movie_id),
        None,
    )
    if movie:
        return movie

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Movie {movie_id!r} not found",
    )
