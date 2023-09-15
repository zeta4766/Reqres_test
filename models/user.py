from typing import List
from pydantic import BaseModel, HttpUrl, Field

from utils.data_generators import random_string


class SupportModel(BaseModel):
    url: HttpUrl
    text: str


class DataModel(BaseModel):
    id: int = Field(..., gt=0)
    email: str
    first_name: str
    last_name: str
    avatar: HttpUrl


class UserModel(BaseModel):
    data: DataModel
    support: SupportModel


class ExampleListModel(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[DataModel]
    support: SupportModel


class CreateUpdateUserData(BaseModel):
    name: str = Field(
        alias="name",
        default_factory=random_string
    )
    job: str = Field(
        alias="job",
        default_factory=random_string
    )


class CreatedUser(BaseModel):
    name: str
    job: str
    id: str
    createdAt: str


class UpdatedUser(BaseModel):
    name: str
    job: str
    updated_at: str = Field(
        alias="updatedAt",
    )



