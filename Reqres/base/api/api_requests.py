import json
import requests


def get_api(url: str, params=''):
    response = requests.get(url, params=params)
    text = json.loads(response.content)
    return response.status_code, text


def post_api(url: str, payload):
    response = requests.post(url, json=payload)
    text = json.loads(response.content)
    return response.status_code, text


def put_api(url: str, payload):
    response = requests.put(url, json=payload)
    text = json.loads(response.content)
    return response.status_code, text


def patch_api(url: str, payload):
    response = requests.patch(url, json=payload)
    text = json.loads(response.content)
    return response.status_code, text


def delete_api(url: str):
    response = requests.delete(url)
    return response.status_code, ''
