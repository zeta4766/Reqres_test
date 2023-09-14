from Reqres.base.api.api_requests import *


def endpoints_info(endpoint_name='') -> int:
    endpoints = ['list_users',
                 'single_user',
                 'single_user_not_found',
                 'resource_list',
                 'single_resource',
                 'single_resource_not_found',
                 'create_user',
                 'update_user_put',
                 'update_user_patch',
                 'delete_user',
                 'register_successful',
                 'register_unsuccessful',
                 'login_successful',
                 'login_unsuccessful',
                 'delayed_response'
                 ]
    if endpoint_name:
        return endpoints.index(endpoint_name)


def api_method(key):
    dict_methods = {
        'post': post_api,
        'put': put_api,
        'patch': patch_api,
        'delete': delete_api,
        'get': get_api
    }
    return dict_methods[key]
