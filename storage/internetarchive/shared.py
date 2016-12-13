import requests


def make_request(url):
    return requests.request('GET', url)
