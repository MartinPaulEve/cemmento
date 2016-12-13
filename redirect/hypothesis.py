from flask import redirect


def redirecto(url):
    """
    Redirects to the hypothesis via service
    :param url: The URL to append to the hypothesis service
    :return: A redirect
    """
    viaurl = "https://via.hypothes.is/{0}".format(url)
    return redirect(viaurl, code=302)
