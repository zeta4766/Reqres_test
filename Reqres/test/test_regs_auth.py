import unittest
from http import HTTPStatus

from Reqres.base.api.users_api import post_api
from Reqres.models.user import RegisterInputUserModel, LogRegErrorUserModel, RegisterSuccessUserModel, \
    LoginSuccessfulModel, LoginInputModel
from Reqres.settings import base_settings


class TestUser(unittest.TestCase):
    def test_registration_successful(self):
        model = RegisterInputUserModel()
        status_code, text = post_api(base_settings.register_url, model)
        self.assertEqual(status_code, HTTPStatus.OK)
        if not RegisterSuccessUserModel.model_validate(text):
            self.fail()

    def test_registration_unsuccessful(self):
        model = RegisterInputUserModel()
        model.email = None
        status_code, text = post_api(base_settings.register_url, model)
        self.assertEqual(status_code, HTTPStatus.BAD_REQUEST)
        if not LogRegErrorUserModel.model_validate(text):
            self.fail()

    def test_login_successful(self):
        model = LoginInputModel()
        status_code, text = post_api(base_settings.register_url, model)
        self.assertEqual(status_code, HTTPStatus.OK)
        if not LoginSuccessfulModel.model_validate(text):
            self.fail()

    def test_login_unsuccessful(self):
        model = LoginInputModel()
        model.email = None
        status_code, text = post_api(base_settings.register_url, model)
        self.assertEqual(status_code, HTTPStatus.BAD_REQUEST)
        if not LogRegErrorUserModel.model_validate(text):
            self.fail()