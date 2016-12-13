from storage.internetarchive.shared import make_request

base_url = "http://web.archive.org/save/"


def save(url):
    """
    Test whether or not a page exists in the internet archive
    :param url: A URL stripped of querystrings
    :return: True if this in the internet archive, false if otherwise
    """
    resp = make_request("{0}{1}?cemmento".format(base_url, url))

    if resp.status_code != 404:
        return True
    else:
        return False
