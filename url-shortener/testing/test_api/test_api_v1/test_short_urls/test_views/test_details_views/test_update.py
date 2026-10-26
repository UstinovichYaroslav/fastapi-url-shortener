import pytest
from _pytest.fixtures import SubRequest
from fastapi import status
from fastapi.testclient import TestClient
from pydantic import AnyHttpUrl

from api.api_v1.short_urls.crud import storage
from main import app
from schemas.short_url import ShortUrl, ShortUrlUpdate
from testing.conftest import create_short_url_random_slug


@pytest.mark.apitest
class TestUpdate:
    @pytest.fixture()
    def short_url(self, request: SubRequest):
        url, description = request.param
        short_url = create_short_url_random_slug(url, description)
        yield short_url
        storage.delete(short_url)

    @pytest.mark.parametrize(
        "short_url, new_description, new_url",
        [
            pytest.param(
                ("https://exemple.com", "old-description"),
                "new-description",
                "https://exemple.com",
                id="old-description-to-new-description",
            ),
            pytest.param(
                ("https://exemple.com", "old-description"),
                "old-description",
                "https://exemple.com",
                id="old-url-to-new-url",
            ),
        ],
        indirect=["short_url"],
    )
    def test_update_short_url_details(
        self,
        short_url: ShortUrl,
        auth_client: TestClient,
        new_description: str,
        new_url: str | AnyHttpUrl,
    ) -> None:
        url = app.url_path_for(
            "update_short_url_details",
            slug=short_url.slug,
        )
        update = ShortUrlUpdate(
            target_url=new_url,
            description=new_description,
        )
        response = auth_client.put(url, json=update.model_dump(mode="json"))
        assert response.status_code == status.HTTP_200_OK, response.text
        short_url_db = storage.get_by_slug(slug=short_url.slug)
        new_data = ShortUrlUpdate(
            target_url=short_url_db.target_url,
            description=short_url_db.description,
        )
        assert new_data == update
