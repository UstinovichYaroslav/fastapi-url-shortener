import random
import string

from fastapi import status
from fastapi.testclient import TestClient

from main import app
from schemas.short_url import ShortUrlCreate


def test_create_short_url(auth_client: TestClient) -> None:
    url = app.url_path_for("create_short_url")
    short_url_create = ShortUrlCreate(
        slug="".join(
            random.choices(
                string.ascii_letters,
                k=10,
            ),
        ),
        description="A short url",
        target_url="https://example.com",
    )
    data: dict[str, str] = short_url_create.model_dump(mode="json")
    response = auth_client.post(url=url, json=data)
    assert response.status_code == status.HTTP_201_CREATED, response.text
    response_data = response.json()
    received_values = ShortUrlCreate(**response_data)
    assert received_values == short_url_create, response_data


def test_created_short_url_already_exists(
    auth_client: TestClient,
    short_url: ShortUrlCreate,
) -> None:
    short_url = ShortUrlCreate(**short_url.model_dump())
    url = app.url_path_for("create_short_url")
    data = short_url.model_dump(mode="json")
    response = auth_client.post(url=url, json=data)
    assert response.status_code == status.HTTP_409_CONFLICT, response.text
    response_data = response.json()
    expected_detail = f"Short URL with slug={short_url.slug!r} already exists."
    assert response_data["detail"] == expected_detail
