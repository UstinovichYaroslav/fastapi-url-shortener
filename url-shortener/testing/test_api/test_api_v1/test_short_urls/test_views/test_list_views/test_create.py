import random
import string
from typing import Any

import pytest
from _pytest.fixtures import SubRequest
from fastapi import status
from fastapi.testclient import TestClient

from main import app
from schemas.short_url import ShortUrlCreate
from testing.conftest import create_short_url_random_slug

pytestmark = pytest.mark.apitest


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
        target_url="https://example.com/",
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


class TestCreateInvalid:
    @pytest.fixture(
        params=[
            pytest.param(
                ("h", "string_too_short"),
                id="short_slug",
            ),
            pytest.param(
                ("too_long_slug", "string_too_long"),
                id="long_slug",
            ),
        ]
    )
    def short_url_create_values(
        self, request: SubRequest
    ) -> tuple[dict[str, Any], str]:
        short_url = create_short_url_random_slug()
        data = short_url.model_dump(mode="json")
        slug, error = request.param
        data["slug"] = slug
        return data, error

    def test_invalid_slug(
        self,
        short_url_create_values: tuple[dict[str, Any], str],
        auth_client: TestClient,
    ) -> None:
        url = app.url_path_for("create_short_url")
        create_data, error_type = short_url_create_values
        response = auth_client.post(
            url=url,
            json=create_data,
        )
        assert (
            response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        ), response.text
        response_data = response.json()
        expected_detail = f"{error_type}"
        assert response_data["detail"][0]["type"] == expected_detail
