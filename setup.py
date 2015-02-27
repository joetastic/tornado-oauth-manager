#!/usr/bin/env python

from distutils.core import setup

setup(
    name='tornado-oauth-manager',
    version='0.1',
    description='A tornado app that will manage oauth2 clients.  Users authenticate with Google',
    requires=['tornado'],
    package_dir = {'': 'src'},
    entry_points={'console_scripts': ['tornado_oauth_manager = tornado_oauth_manager.run:main']}
)
