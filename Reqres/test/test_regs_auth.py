import unittest
from http import HTTPStatus

import pytest

from Reqres.base.api.api_requests import post_api
from Reqres.models.log_reg import *
from Reqres.settings import base_settings
from Reqres.utils.data_generators import random_string, random_email


def test_registration_successful():
    model = RegisterInputUserModel()
    status_code, text = post_api(base_settings.register_url, model)
    assert status_code == HTTPStatus.OK
    RegisterSuccessUserModel.model_validate(text)


@pytest.mark.parametrize('email, password', [
    (random_email(), ''),
    ('', random_string())
])
def test_registration_unsuccessful(email, password):
    model = RegisterInputUserModel()
    model.email, model.password = email, password
    status_code, text = post_api(base_settings.register_url, model)
    assert status_code == HTTPStatus.BAD_REQUEST
    LogRegErrorUserModel.model_validate(text)


def test_login_successful():
    model = LoginInputModel()
    status_code, text = post_api(base_settings.register_url, model)
    assert status_code == HTTPStatus.OK
    LoginSuccessfulModel.model_validate(text)


@pytest.mark.parametrize('email, password', [
    (random_email(), ''),
    ('', random_string()),
    (random_email(), random_string())
])
def test_login_unsuccessful(email, password):
    model = LoginInputModel()
    model.email, model.password = email, password
    status_code, text = post_api(base_settings.register_url, model)
    assert status_code == HTTPStatus.BAD_REQUEST
    LogRegErrorUserModel.model_validate(text)
