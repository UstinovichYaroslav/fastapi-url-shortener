from typing import Annotated

from annotated_types import Len
from pydantic import BaseModel, HttpUrl, AnyHttpUrl


class ShortUrlBase(BaseModel):
    # target_url: HttpUrl
    target_url: AnyHttpUrl
    slug: str


class ShortUrlCreate(ShortUrlBase):
    """
    Модель для создания сокращенной ссылки
    """

    slug: Annotated[
        str,
        Len(min_length=3, max_length=10),
    ]


class ShortUrl(ShortUrlBase):
    """
    Модель сокращенной ссылки
    """
