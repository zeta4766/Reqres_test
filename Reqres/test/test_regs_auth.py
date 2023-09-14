import unittest
from http import HTTPStatus

from Reqres.base.api.api_requests import post_api
from Reqres.models.log_reg import *
from Reqres.settings import base_settings


def test_registration_successful():
    model = RegisterInputUserModel()
    status_code, text = post_api(base_settings.register_url, model)
    assert status_code == HTTPStatus.OK
    RegisterSuccessUserModel.model_validate(text)


def test_registration_unsuccessful():
    model = RegisterInputUserModel()
    model.email = None
    status_code, text = post_api(base_settings.register_url, model)
    assert status_code == HTTPStatus.BAD_REQUEST
    LogRegErrorUserModel.model_validate(text)


def test_login_successful():
    model = LoginInputModel()
    status_code, text = post_api(base_settings.register_url, model)
    assert status_code == HTTPStatus.OK
    LoginSuccessfulModel.model_validate(text)


def test_login_unsuccessful():
    model = LoginInputModel()
    model.email = None
    status_code, text = post_api(base_settings.register_url, model)
    assert status_code == HTTPStatus.BAD_REQUEST
    LogRegErrorUserModel.model_validate(text)
