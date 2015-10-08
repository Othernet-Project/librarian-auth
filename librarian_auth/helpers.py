import functools

from bottle import request, response

from .options import Options


def identify_database(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        db = kwargs.pop('db', None) or request.db.sessions  # mustn't evaluate
        return func(db=db, *args, **kwargs)
    return wrapper


@Options.collector('language')
def collect_language(options):
    return request.locale


@Options.processor('language', is_explicit=True)
def process_language(options, language):
    if language and request.locale != language:
        request.locale = language
        response.set_cookie('locale', language, path='/')


@Options.processor('default_route')
def process_default_route(options, default_route):
    if default_route:
        request.default_route = default_route
