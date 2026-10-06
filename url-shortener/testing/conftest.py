import random
import string
from collections.abc import Generator
from os import getenv

import pytest

from api.api_v1.short_urls.crud import storage
from schemas.short_url import ShortUrl, ShortUrlCreate

if getenv("TESTING") != "1":
    pytest.exit(
        "Environment is not ready for testing",
    )
def create_and_save_short_url() -> ShortUrl:
    movie_in = ShortUrlCreate(
        slug="".join(
            random.choices(
                string.ascii_letters,
                k=8,
            )
        ),  # noqa: S311
        target_url="https://exemple.com",
        description="Movie description",
    )
    return storage.create(movie_in)


@pytest.fixture
def short_url() -> Generator[ShortUrl]:
    short_url = create_and_save_short_url()
    yield short_url
    storage.delete(short_url)