from http import HTTPStatus

import pytest

from base.api.api_requests import get_api
from models.resource import ResponseData, ResponseDataList
from settings import base_settings
from utils.data_generators import random_number


@pytest.mark.parametrize("id_resource", random_number(1, 12, 3))
def test_single_resource(id_resource):
    status_code, text = get_api(base_settings.resource_url(id_resource))
    assert status_code == HTTPStatus.OK
    ResponseData.model_validate(text)


def test_list_resource():
    status_code, text = get_api(base_settings.resource_url())
    assert status_code == HTTPStatus.OK
    ResponseDataList.model_validate(text)


@pytest.mark.parametrize("id_resource", random_number(13, 100, 3))
def test_single_resource_not_found(id_resource):
    status_code, text = get_api(base_settings.resource_url(id_resource))
    assert status_code == HTTPStatus.NOT_FOUND
    assert text == {}
