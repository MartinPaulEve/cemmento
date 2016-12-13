from flask import Flask
from storage.internetarchive.query import exists
from storage.internetarchive.store import save
from urllib.parse import urlparse, urlunparse

app = Flask(__name__)


@app.route('/<path:url>')
def proxy_startup(url):
    """
    Proxy entry point
    :param url: The URL to parse
    :return: A redirect to the archived URL
    """
    url = clean_url(url)

    if exists(url):
        # redirect to the correct URL
        return '{0} is in the internet archive'.format(url)
    else:
        if save(url):
            # redirect to the correct URL
            pass
        else:
            return 'Unable to service request for {0}'.format(url)


def clean_url(url):
    """
    Reformat a URL with all querystrings stripped
    :param url: The URL
    :return: A clean URL
    """
    parsed = urlparse(url)
    scheme, netloc, path, params, query, fragment = parsed
    return urlunparse((scheme, netloc, path.split('/')[1], '', '', ''))

if __name__ == '__main__':
    app.run()
