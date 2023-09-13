import json
from Reqres.settings import base_settings
import requests
from Reqres.models.user import *


def test_user():
    r = requests.get(base_settings.user_url(2))
    text = json.loads(r.content)
    print(text)
    try:
        assert ExampleModel.model_validate(text)
    except Exception as e:
        print("JSON некорректен или не соответствует модели данных.")
        print(f"Ошибка: {str(e)}")
        assert False

def test_users_list():
    r = requests.get(base_settings.user_url(), params={'page':2, 'per_page':1})
    text = json.loads(r.content)
