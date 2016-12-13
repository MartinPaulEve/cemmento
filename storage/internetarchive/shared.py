import requests


def make_request(url):
    """
    Make a request to a remote location
    :param url: The URL to fetch
    :return: A response object
    """
    return requests.request('GET', url)
