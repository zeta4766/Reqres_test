import json
import unittest
from http import HTTPStatus

from unicodedata import name

from Reqres.base.api.users_api import get_api, post_api
from Reqres.settings import base_settings
import requests
from Reqres.models.user import *


class TestUser(unittest.TestCase):
    def test_single_user(self):
        status_code, text = get_api(base_settings.user_url(2))
        self.assertEqual(status_code, HTTPStatus.OK)
        UserModel.model_validate(text)

    def test_single_user_not_found(self):
        status_code, text = get_api(base_settings.user_url(23))
        self.assertEqual(status_code, HTTPStatus.NOT_FOUND)
        assert json.loads(text) == {}

    def test_list_users(self):
        status_code, text = get_api(base_settings.user_url(), params={'page': 2, 'per_page': 1})
        self.assertEqual(status_code, HTTPStatus.OK)
        ExampleListModel.model_validate(text)

    def test_create_user(self):
        model = CreateUserData()
        status_code, text = post_api(base_settings.user_url(), model)
        self.assertEqual(status_code, HTTPStatus.CREATED)
        CreatedUser.model_validate(text)

    