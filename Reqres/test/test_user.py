from http import HTTPStatus

import pytest

from Reqres.base.api.api_requests import *
from Reqres.settings import base_settings
from Reqres.models.user import *
from Reqres.utils.data_generators import random_number
from Reqres.utils.measure_execution_time import measure_execution_time


@pytest.mark.parametrize("id_number", random_number(1, 12, 3))
def test_single_user(id_number):
    status_code, text = get_api(base_settings.user_url(id_number))
    assert status_code == HTTPStatus.OK
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
    ExampleListModel.model_validate(text)


def test_create_user():
    model = CreateUpdateUserData()
    status_code, text = post_api(base_settings.user_url(), model)
    assert status_code == HTTPStatus.CREATED
    CreatedUser.model_validate(text)


@pytest.mark.parametrize("id_number", random_number(1, 12, 3))
def test_update_user_put(id_number):
    model = CreateUpdateUserData()
    status_code, text = put_api(base_settings.user_url(id_number), model)
    assert status_code == HTTPStatus.OK
    UpdatedUser.model_validate(text)


@pytest.mark.parametrize("id_number", random_number(1, 12, 3))
def test_update_user_patch(id_number):
    model = CreateUpdateUserData()
    status_code, text = patch_api(base_settings.user_url(id_number), model)
    assert status_code == HTTPStatus.OK
    UpdatedUser.model_validate(text)


@pytest.mark.parametrize("id_number", random_number(1, 12, 3))
def test_delete_user(id_number):
    status_code = delete_api(base_settings.user_url(id_number))
    assert status_code == HTTPStatus.NO_CONTENT


@pytest.mark.parametrize("delay", [1, 3, 5])
def test_list_users_delay(delay):
    status_code, text = get_api(base_settings.user_url(), params={'delay': delay})
    assert status_code == HTTPStatus.OK
    ExampleListModel.model_validate(text)


@pytest.mark.parametrize("delay", [1, 3, 5])
def test_time_list_users_delay(delay):
    time_simple = measure_execution_time(test_list_users)
    time_delay = measure_execution_time(lambda: test_list_users_delay(delay))
    assert time_delay - time_simple - delay < 0.05
