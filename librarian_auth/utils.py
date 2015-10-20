import urlparse

from bottle import request, response


def http_redirect(path, code=303):
    """Redirect to the specified path. Replacement for bottle's builtin
    redirect function, because it loses newly set cookies.

    :param path:  Redirect to specified path
    """
    response.set_header('Location', urlparse.urljoin(request.url, path))
    response.status = code
    response.body = ""
    return response
