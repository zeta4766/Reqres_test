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
        status_code, text = get_user_api(base_settings.user_url(2))
        self.assertEqual(status_code, HTTPStatus.OK)
        if not UserModel.model_validate(text):
            self.fail()

    def test_single_user_not_found(self):
        r = requests.get(base_settings.user_url(23))
        self.assertEqual(r.status_code, HTTPStatus.NOT_FOUND)
        assert json.loads(r.content) == {}

    def test_list_users(self):
        r = requests.get(base_settings.user_url(), params={'page': 2, 'per_page': 1})
        text = json.loads(r.content)
        self.assertEqual(r.status_code, HTTPStatus.OK)
        if not ExampleListModel.model_validate(text):
            self.fail()
