from flask import Flask
from storage.internetarchive.query import exists

app = Flask(__name__)


@app.route('/<path:url>')
def proxy_startup(url):
    """
    Proxy entry point
    :param url: The URL to parse
    :return: A redirect to the archived URL
    """

    if exists(url):
        return '{0} is in the internet archive'.format(url)
    else:
        return '{0} is not in the internet archive'.format(url)



if __name__ == '__main__':
    app.run()
