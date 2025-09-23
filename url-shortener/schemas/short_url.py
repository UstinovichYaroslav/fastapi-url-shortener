from pydantic import BaseModel, HttpUrl


class ShortUrlBase(BaseModel):
    target_url: HttpUrl
    slug: str


class ShortUrl(ShortUrlBase):
    """
    Модель сокращенной ссылки
    """
