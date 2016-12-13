from flask import Flask
from storage.internetarchive.query import exists
from storage.internetarchive.store import save

app = Flask(__name__)


@app.route('/<path:url>')
def proxy_startup(url):
    """
    Proxy entry point
    :param url: The URL to parse
    :return: A redirect to the archived URL
    """

    if exists(url):
        # redirect to the correct URL
        return '{0} is in the internet archive'.format(url)
    else:
        if save(url):
            # redirect to the correct URL
            pass
        else:
            return 'Unable to service request for {0}'.format(url)


if __name__ == '__main__':
    app.run()
