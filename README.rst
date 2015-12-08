==============
librarian-auth
==============

This is a helper component, made to supplement the authentication related core
package (``librarian_core.contrib.auth``) with routes that handle the usual
user account creation, login, password reset and emergency password reset
features, as well as the superuser account creation step in the setup wizard.

Installation
------------

The component has the following dependencies:

- librarian_core_
- librarian_setup_
- librarian_menu_

To enable this component, add it to the list of components in librarian_'s
`config.ini` file, e.g.::

    [app]
    +components =
        librarian_auth

Configuration
-------------

``emergency.file``
    Path to emergency reset token file, needed to enable the emergency password
    reset feature. Example::

        [emergency]
        file = /path/to/emergency.token

Development
-----------

In order to recompile static assets, make sure that compass_ and coffeescript_
are installed on your system. To perform a one-time recompilation, execute::

    make recompile

To enable the filesystem watcher and perform automatic recompilation on changes,
use::

    make watch

.. _librarian: https://github.com/Outernet-Project/librarian
.. _librarian_core: https://github.com/Outernet-Project/librarian-core
.. _librarian_setup: https://github.com/Outernet-Project/librarian-setup
.. _librarian_menu: https://github.com/Outernet-Project/librarian-menu
.. _compass: http://compass-style.org/
.. _coffeescript: http://coffeescript.org/
