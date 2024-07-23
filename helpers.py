import requests

from definitions import HF_API_TOKEN

API_URL_PREFIX = "https://api-inference.huggingface.co/models/"
headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}


def query(payload, api_url_suffix):
    response = requests.post(
            API_URL_PREFIX + api_url_suffix,
            headers=headers,
            json=payload
        )
    return response
