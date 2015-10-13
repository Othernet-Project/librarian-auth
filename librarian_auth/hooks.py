from .commands import create_superuser
from .menuitems import LogoutMenuItem
from .setup import has_no_superuser, setup_superuser_form, setup_superuser
from .utils import generate_random_key

from librarian_setup.decorators import autoconfigure


autoconfigure('session.secret')(generate_random_key)
autoconfigure('csrf.secret')(generate_random_key)


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
    # register setup wizard step
    setup_wizard = supervisor.exts.setup_wizard
    setup_wizard.register('superuser',
                          setup_superuser_form,
                          template='setup/step_superuser.tpl',
                          method='GET',
                          index=3,
                          test=has_no_superuser)
    setup_wizard.register('superuser',
                          setup_superuser,
                          template='setup/step_superuser.tpl',
                          method='POST',
                          index=3,
                          test=has_no_superuser)
