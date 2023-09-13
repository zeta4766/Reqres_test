from pydantic import BaseModel
from pydantic_settings import BaseSettings


class TestUser(BaseModel):
    email: str
    password: str


class Settings(BaseSettings):
    base_url: str = "https://reqres.in"
    user_email: str = "eve.holt@reqres.in"
    user_password: str = "cityslicka"

    @property
    def api_url(self) -> str:
        return f'{self.base_url}/api'

    @property
    def api_login(self) -> str:
        return f'{self.api_url}/login'

    def user_url(self, user_id=0) -> str:
        if user_id:
            return f'{self.api_url}/users/{user_id}'
        else:
            return f'{self.api_url}/users'

    def resource_url(self):
        return f'{self.api_url}/unknown'

    def register_url(self):
        return f'{self.api_url}/register'

    @property
    def user(self) -> TestUser:
        return TestUser(
            email=self.user_email,
            password=self.user_password
        )


base_settings = Settings()
