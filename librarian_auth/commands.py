import getpass

from .users import User


def create_superuser(arg, supervisor):
    print("Press ctrl-c to abort")
    try:
        username = raw_input('Username: ')
        password = getpass.getpass()
    except (KeyboardInterrupt, EOFError):
        print("Aborted")
        raise supervisor.EarlyExit("Aborted", exit_code=1)

    try:
        user = User.create(username=username,
                           password=password,
                           is_superuser=True,
                           db=supervisor.exts.databases.sessions,
                           overwrite=True)
        print("User created. The password reset token is: {}".format(
            user.reset_token))
    except User.InvalidUserCredentials:
        print("Invalid user credentials, please try again.")
        create_superuser(arg, supervisor)

    raise supervisor.EarlyExit()
