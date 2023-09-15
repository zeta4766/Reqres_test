from pydantic import BaseModel, Field
import os
from dotenv import load_dotenv

load_dotenv()


class RegisterInputUserModel(BaseModel):
    email: str = Field(
        alias="email",
        default=os.getenv('DEFAULT_USER_EMAIL')
    )
    password: str = Field(
        alias="password",
        default=os.getenv('DEFAULT_USER_REGISTER_PASSWORD')
    )


class RegisterSuccessUserModel(BaseModel):
    id: int = Field(..., gt=0)
    token: str


class LogRegErrorUserModel(BaseModel):
    error: str


class LoginInputModel(BaseModel):
    email: str = Field(
        alias="email",
        default=os.getenv('DEFAULT_USER_EMAIL')
    )
    password: str = Field(
        alias="password",
        default=os.getenv('DEFAULT_USER_LOGIN_PASSWORD')
    )


class LoginSuccessfulModel(BaseModel):
    token: str
