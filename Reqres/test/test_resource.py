import unittest
from http import HTTPStatus

from Reqres.base.api.users_api import get_api
from Reqres.models.user import ResponseData, ResponseDataList
from Reqres.settings import base_settings


class ResourceUser(unittest.TestCase):

    def test_single_resource(self):
        status_code, text = get_api(base_settings.resource_url(2))
        self.assertEqual(status_code, HTTPStatus.OK)
        ResponseData.model_validate(text)

    def test_list_resource(self):
        status_code, text = get_api(base_settings.resource_url())
        self.assertEqual(status_code, HTTPStatus.OK)
        ResponseDataList.model_validate(text)

    def test_single_resource_not_found(self):
        status_code, text = get_api(base_settings.resource_url(23))
        self.assertEqual(status_code, HTTPStatus.NOT_FOUND)
        assert text == {}