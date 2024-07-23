import requests

from definitions import HF_API_TOKEN

API_URL_PREFIX = "https://api-inference.huggingface.co/models/"
headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}


def query(payload, api_url_suffix):
    try:
        response = requests.post(
            API_URL_PREFIX + api_url_suffix,
            headers=headers,
            json=payload
        )
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        return response
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        if response.status_code == 401:
            print("Authentication failed. Check your API token.")
        elif response.status_code == 404:
            print("Model not found. Check the API_URL.")
        # You can add more specific status code checks here
    except requests.exceptions.ConnectionError:
        print("Failed to connect to the server. Check your internet connection.")
    except requests.exceptions.Timeout:
        print("Request timed out. The server took too long to respond.")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred while making the request: {err}")
    return None
