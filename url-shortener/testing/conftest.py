import random
import string
from os import getenv

import pytest

from api.api_v1.short_urls.crud import storage
from schemas.short_url import ShortUrl, ShortUrlCreate

if getenv("TESTING") != "1":
    pytest.exit(
        "Environment is not ready for testing",
    )


def build_short_url_create(slug: str) -> ShortUrlCreate:
    return ShortUrlCreate(
        slug=slug,
        target_url="https://exemple.com",
        description="ShortUrl description",
    )


def build_short_url_random_slug() -> ShortUrlCreate:
    return build_short_url_create(
        slug="".join(
            random.choices(
                string.ascii_letters,
                k=8,
            ),
        )
    )


def create_short_url(slug: str) -> ShortUrl:
    short_url_in = build_short_url_create(slug)
    return storage.create(short_url_in)


def create_short_url_random_slug() -> ShortUrl:
    short_url_in = build_short_url_random_slug()
    return storage.create(short_url_in)
