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
def handle_language(language):
    return  # FIXME: find some way to check for original requested path
    if language and request.locale == language:
        # redirect only requests without a locale prefixed path
        redirect(i18n_path(locale=language))

    return request.locale
