import time
import unittest
from http import HTTPStatus

import pytest

from Reqres.base.api.users_api import *
from Reqres.settings import base_settings
from Reqres.models.user import *


class TestUser(unittest.TestCase):
    def test_single_user(self):
        status_code, text = get_api(base_settings.user_url(2))
        unittest.TestCase.assertEqual(status_code, HTTPStatus.OK)
        UserModel.model_validate(text)

    def test_single_user_not_found(self):
        status_code, text = get_api(base_settings.user_url(23))
        self.assertEqual(status_code, HTTPStatus.NOT_FOUND)
        assert text == {}

    def test_list_users(self):
        status_code, text = get_api(base_settings.user_url(), params={'page': 2, 'per_page': 1})
        self.assertEqual(status_code, HTTPStatus.OK)
        ExampleListModel.model_validate(text)

    def test_create_user(self):
        model = CreateUpdateUserData()
        status_code, text = post_api(base_settings.user_url(), model)
        self.assertEqual(status_code, HTTPStatus.CREATED)
        CreatedUser.model_validate(text)

    def test_update_user_put(self):
        model = CreateUpdateUserData()
        status_code, text = put_api(base_settings.user_url(2), model)
        self.assertEqual(status_code, HTTPStatus.OK)
        UpdatedUser.model_validate(text)

    def test_update_user_patch(self):
        model = CreateUpdateUserData()
        status_code, text = patch_api(base_settings.user_url(2), model)
        self.assertEqual(status_code, HTTPStatus.OK)
        UpdatedUser.model_validate(text)

    def test_delete_user(self):
        status_code = delete_api(base_settings.user_url(2))
        self.assertEqual(status_code, HTTPStatus.NO_CONTENT)


    def test_list_users_delay(self):
        delay = 5
        start_time = time.perf_counter()
        status_code, text = get_api(base_settings.user_url(), params={'delay': delay})
        assert status_code == HTTPStatus.OK
        ExampleListModel.model_validate(text)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        assert elapsed_time == pytest.approx(delay, abs=1)
