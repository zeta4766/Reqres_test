from pydantic import BaseModel, HttpUrl, Field


class SupportModel(BaseModel):
    url: HttpUrl
    text: str


class DataModel(BaseModel):
    id: int = Field(..., gt=0)
    email: str
    first_name: str
    last_name: str
    avatar: HttpUrl


class ExampleModel(BaseModel):
    data: DataModel
    support: SupportModel
