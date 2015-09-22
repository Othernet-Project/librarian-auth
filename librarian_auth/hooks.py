from .commands import create_superuser
from .menuitems import LogoutMenuItem
from .utils import generate_secret_key

from librarian_setup.decorators import autoconfigure


autoconfigure('session.secret')(generate_secret_key)
autoconfigure('csrf.secret')(generate_secret_key)


def initialize(supervisor):
    supervisor.exts.commands.register('su',
                                      create_superuser,
                                      '--su',
                                      action='store_true')
    supervisor.exts.commands.register('no_auth',
                                      None,
                                      '--no-auth',
                                      action='store_true',
                                      help='disable authentication')
    supervisor.exts.menuitems.register(LogoutMenuItem)
