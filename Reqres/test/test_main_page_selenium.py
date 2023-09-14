import json

import pytest
from selenium import webdriver

from Reqres.base.api.api_requests import get_api, post_api
from Reqres.pages.main_page import MainPage
from Reqres.utils.compare_dicts import compare_dicts
from Reqres.utils.dictionary_endpoints import api_method


@pytest.fixture
def page():
    page = MainPage(driver=webdriver.Chrome())
    yield page
    page.driver.quit()


@pytest.mark.parametrize('test_name, method', [
    ('list_users', 'get'),
    ('single_user', 'get'),
    ('single_user_not_found', 'get'),
    ('resource_list', 'get'),
    ('single_resource', 'get'),
    ('single_resource_not_found', 'get'),
    ('delayed_response', 'get'),
    ('delete_user', 'delete')
])
@pytest.mark.usefixtures("page")
def test_get_delete(page, test_name, method):
    page.endpoint_click(test_name)
    href = page.href_by_name(test_name)
    api = api_method(method)
    status_code, text = api(href)
    assert str(status_code) == page.response_code()
    if method != 'delete':
        assert json.loads(json.dumps(text)) == json.loads(page.out_response())

@pytest.mark.parametrize('test_name, method', [
    ('create_user', 'post'),
    ('register_successful', 'post'),
    ('register_unsuccessful', 'post'),
    ('login_successful', 'post'),
    ('login_unsuccessful', 'post'),
    ('update_user_put', 'put'),
    ('update_user_patch', 'patch')
])
@pytest.mark.usefixtures("page")
def test_post_put_patch(page, test_name, method):
    page.endpoint_click(test_name)
    href = page.href_by_name(test_name)
    body = page.json_data_for_request_body(test_name)
    api = api_method(method)
    status_code, text = api(href, body)
    assert str(status_code) == page.response_code()

    dict_api = json.loads(json.dumps(text))
    dict_ui = json.loads(page.out_response())

    assert compare_dicts(dict_api, dict_ui)
