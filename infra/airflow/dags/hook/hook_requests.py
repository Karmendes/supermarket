
import requests


def call_api(supermarket):
    endpoint = f'http://api:5000/{supermarket}'
    response = requests.get(endpoint,timeout= 60)
    return response.status_code