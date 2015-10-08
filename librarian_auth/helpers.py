import functools

from bottle import request, redirect
from bottle_utils.i18n import i18n_path

from .options import Options


def identify_database(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        db = kwargs.pop('db', None) or request.db.sessions  # mustn't evaluate
        return func(db=db, *args, **kwargs)
    return wrapper


@Options.handler('language')
def handle_language(options, language):
    if request.query.get('action') == 'change':
        options['language'] = request.locale
    elif language and request.locale != language:
        redirect(i18n_path(locale=language))


@Options.handler('default_route')
def handle_default_route(options, default_route):
    if default_route:
        request.default_route = default_route
