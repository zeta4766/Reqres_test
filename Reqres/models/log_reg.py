from typing import List
from pydantic import BaseModel, Field


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
