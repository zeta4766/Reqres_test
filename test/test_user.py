from http import HTTPStatus

import pytest

from base.api.api_requests import *
from settings import base_settings
from models.user import *
from utils.data_generators import random_number
from utils.measure_execution_time import measure_execution_time


@pytest.mark.parametrize("id_number", random_number(1, 12, 3))
def test_single_user(id_number):
    status_code, text = get_api(base_settings.user_url(id_number))
    assert status_code == HTTPStatus.OK
    assert text['data']['id'] == id_number
    UserModel.model_validate(text)


@pytest.mark.parametrize("id_number", random_number(13, 100, 3))
def test_single_user_not_found(id_number):
    status_code, text = get_api(base_settings.user_url(id_number))
    assert status_code == HTTPStatus.NOT_FOUND
    assert text == {}


@pytest.mark.parametrize("page", [1, 2])
@pytest.mark.parametrize("per_page", random_number(1, 6, 2))
def test_list_users(page, per_page):
    status_code, text = get_api(base_settings.user_url(),
                                params={'page': page, 'per_page': per_page})
    print(page, per_page)
    assert status_code == HTTPStatus.OK
    assert text['page'] == page
    assert text['per_page'] == per_page
    ExampleListModel.model_validate(text)


def test_create_user():
    model = CreateUpdateUserData()
    status_code, text = post_api(base_settings.user_url(), model.model_dump())
    assert status_code == HTTPStatus.CREATED
    assert model.name == text['name']
    assert model.job == text['job']
    CreatedUser.model_validate(text)


@pytest.mark.parametrize("id_number", random_number(1, 12, 3))
def test_update_user_put(id_number):
    model = CreateUpdateUserData()
    status_code, text = put_api(base_settings.user_url(id_number), model.model_dump())
    assert status_code == HTTPStatus.OK
    assert model.name == text['name']
    assert model.job == text['job']
    UpdatedUser.model_validate(text)


@pytest.mark.parametrize("id_number", random_number(1, 12, 3))
def test_update_user_patch(id_number):
    model = CreateUpdateUserData()
    status_code, text = patch_api(base_settings.user_url(id_number), model.model_dump())
    assert status_code == HTTPStatus.OK
    assert model.name == text['name']
    assert model.job == text['job']
    UpdatedUser.model_validate(text)


@pytest.mark.parametrize("id_number", random_number(1, 12, 3))
def test_delete_user(id_number):
    status_code, text = delete_api(base_settings.user_url(id_number))
    assert status_code == HTTPStatus.NO_CONTENT


@pytest.mark.parametrize("delay", [1, 3, 5])
def test_list_users_delay(delay):
    status_code, text = get_api(base_settings.user_url(), params={'delay': delay})
    assert status_code == HTTPStatus.OK
    ExampleListModel.model_validate(text)


@pytest.mark.parametrize("delay", [1, 3, 5])
def test_time_list_users_delay(delay):
    time_simple = measure_execution_time(lambda: test_list_users(1, 6))
    time_delay = measure_execution_time(lambda: test_list_users_delay(delay))
    assert time_delay - time_simple - delay < 0.05
