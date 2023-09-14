def compare_dicts(dict_api, dict_ui):
    keys_to_ignore = ['createdAt', 'updatedAt', 'token', 'id']
    filtered_dict_api = {key: dict_api[key] for key in dict_api if key not in keys_to_ignore}
    filtered_dict_ui = {key: dict_ui[key] for key in dict_ui if key not in keys_to_ignore}
    return dict_api.keys() == dict_ui.keys() and filtered_dict_ui == filtered_dict_api
