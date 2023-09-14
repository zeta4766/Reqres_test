import unittest
from http import HTTPStatus

from Reqres.base.api.users_api import post_api
from Reqres.models.log_reg import *
from Reqres.settings import base_settings


class TestUser(unittest.TestCase):
    def test_registration_successful(self):
        model = RegisterInputUserModel()
        status_code, text = post_api(base_settings.register_url, model)
        self.assertEqual(status_code, HTTPStatus.OK)
        RegisterSuccessUserModel.model_validate(text)

    def test_registration_unsuccessful(self):
        model = RegisterInputUserModel()
        model.email = None
        status_code, text = post_api(base_settings.register_url, model)
        self.assertEqual(status_code, HTTPStatus.BAD_REQUEST)
        LogRegErrorUserModel.model_validate(text)

    def test_login_successful(self):
        model = LoginInputModel()
        status_code, text = post_api(base_settings.register_url, model)
        self.assertEqual(status_code, HTTPStatus.OK)
        LoginSuccessfulModel.model_validate(text)

    def test_login_unsuccessful(self):
        model = LoginInputModel()
        model.email = None
        status_code, text = post_api(base_settings.register_url, model)
        self.assertEqual(status_code, HTTPStatus.BAD_REQUEST)
        LogRegErrorUserModel.model_validate(text)
