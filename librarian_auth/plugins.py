import functools

from bottle import request

from .sessions import SessionExpired, SessionInvalid, Session
from .users import User


EXPORTS = {
    'session_plugin': {},
    'user_plugin': {'depends_on': ['librarian_auth.plugins.session_plugin']}
}


def session_plugin(supervisor):
    # Set up a hook, so handlers that raise cannot escape session-saving
    @supervisor.app.hook('after_request')
    def save_session():
        if hasattr(request, 'session'):
            if request.session.modified:
                request.session.save()

            cookie_name = supervisor.config['session.cookie_name']
            secret = supervisor.config['session.secret']
            request.session.set_cookie(cookie_name, secret)

    def plugin(callback):
        @functools.wraps(callback)
        def wrapper(*args, **kwargs):
            cookie_name = supervisor.config['session.cookie_name']
            secret = supervisor.config['session.secret']
            session_id = request.get_cookie(cookie_name, secret=secret)
            try:
                request.session = Session.fetch(session_id)
            except (SessionExpired, SessionInvalid):
                request.session = Session.create()
            return callback(*args, **kwargs)
        return wrapper
    plugin.name = 'session'
    return plugin


def user_plugin(supervisor):
    # Set up a hook, so handlers that raise cannot escape session-saving
    @supervisor.app.hook('after_request')
    def store_user_in_session():
        if hasattr(request, 'session') and hasattr(request, 'user'):
            request.user.options.collect()
            request.session['user'] = request.user.to_json()

    def plugin(callback):
        @functools.wraps(callback)
        def wrapper(*args, **kwargs):
            request.no_auth = supervisor.config['args'].no_auth
            user_data = request.session.get('user', '{}')
            request.user = User.from_json(user_data)
            request.user.options.process()
            return callback(*args, **kwargs)

        return wrapper
    plugin.name = 'user'
    return plugin
