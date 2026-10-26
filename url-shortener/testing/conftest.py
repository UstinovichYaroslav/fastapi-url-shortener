import random
import string
from collections.abc import Generator
from os import getenv

import pytest
from pydantic import AnyHttpUrl

from api.api_v1.short_urls.crud import storage
from schemas.short_url import ShortUrl, ShortUrlCreate


@pytest.fixture(scope="session", autouse=True)
def check_testing_env() -> None:
    if getenv("TESTING") != "1":
        pytest.exit(
            "Environment is not ready for testing",
        )


def build_short_url_create(
    slug: str,
    description: str = "ShortUrl description",
    url: str | AnyHttpUrl = "https://exemple.com/",
) -> ShortUrlCreate:
    return ShortUrlCreate(
        slug=slug,
        target_url=url,
        description=description,
    )


def build_short_url_random_slug(
    description: str = "ShortUrl description",
    url: str | AnyHttpUrl = "https://exemple.com/",
) -> ShortUrlCreate:
    return build_short_url_create(
        slug="".join(
            random.choices(
                string.ascii_letters,
                k=8,
            ),
        ),
        description=description,
        url=url,
    )


def create_short_url(
    slug: str,
    description: str = "ShortUrl description",
    url: str | AnyHttpUrl = "https://exemple.com/",
) -> ShortUrl:
    short_url_in = build_short_url_create(slug, description, url)
    return storage.create(short_url_in)


def create_short_url_random_slug(
    url: str | AnyHttpUrl = "https://exemple.com/",
    description: str = "ShortUrl description",
) -> ShortUrl:
    short_url_in = build_short_url_random_slug(description, url)
    return storage.create(short_url_in)


@pytest.fixture()
def short_url() -> Generator[ShortUrl]:
    short_url = create_short_url_random_slug()
    yield short_url
    storage.delete(short_url)
