import json

import requests


def get_api(url: str, params=''):
    response = requests.get(url, params=params)
    text = json.loads(response.content)
    return response.status_code, text


def post_api(url: str, payload):
    response = requests.post(url, json=payload.model_dump())
    text = json.loads(response.content)
    return response.status_code, text
