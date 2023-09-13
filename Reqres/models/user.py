from typing import List

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


class RegisterInputUserModel(BaseModel):
    email: str = Field(
        alias="email",
        default="eve.holt@reqres.in"
    )
    password: str = Field(
        alias="password",
        default="pistol"
    )


class RegisterSuccessUserModel(BaseModel):
    id: int
    token: str

class LogRegErrorUserModel(BaseModel):
    error: str


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

class LoginInputModel(BaseModel):
    email: str = Field(
        alias="email",
        default="eve.holt@reqres.in"
    )
    password: str = Field(
        alias="password",
        default="cityslicka"
    )

class LoginSuccessfulModel(BaseModel):
    token: str
