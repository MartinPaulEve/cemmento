from flask import Flask
from storage.internetarchive.query import exists, base_url
from storage.internetarchive.store import save
from redirect.hypothesis import redirecto

app = Flask(__name__)
application = app

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
        return redirecto("{0}{1}?cemmento".format(base_url, url))
    else:
        if save(url):
            # redirect to the correct URL
            return redirecto("{0}{1}?cemmento".format(base_url, url))
        else:
            return 'Unable to service request for {0}'.format(url)


def clean_url(url):
    """
    Reformat a URL with all querystrings stripped
    :param url: The URL
    :return: A clean URL
    """
    return url[:url.find('?')]

if __name__ == '__main__':
    app.run()
