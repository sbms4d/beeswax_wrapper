#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
For setting and returning beeswax passwords (visible only to current environment user).
"""
from __future__ import unicode_literals

import keyring
import getpass
import argparse


def store_beeswax_credentials(usrnm, psswrd):
    """
    Store password in environment's keyring

    :param str|unicode usrnm: Beeswax username/email
    :param str|unicode psswrd: Beeswax password
    """
    user = getpass.getuser()
    keyring.set_password("beeswax_username", user, usrnm)
    keyring.set_password("beeswax_password", user, psswrd)


def get_beeswax_credentials():
    """
    Retrieve stored beeswax credentials
    :rtype: dict[str|unicode, str|unicode]
    :return: beeswax credentials, e.g. {"username":"foo", "password":"bar"}
    """
    user = getpass.getuser()
    return {
        'username': keyring.get_password("beeswax_username", user),
        'password': keyring.get_password("beeswax_password", user)
    }


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Sets beeswax credentials. Ran without arguments, the user will be'
                    ' prompted for their details. Should the details be passed in as'
                    ' arguments it is left to the user to exercise security best practices.')
    parser.add_argument('--username', dest='username', help='Beeswax username', action='store')
    parser.add_argument('--password', dest='password', help='Beeswax password', action='store')

    args = parser.parse_args()

    username = args.username
    password = args.password

    if username is None:
        username = raw_input('Beeswax Username: ')
    if password is None:
        password = getpass.getpass('Beeswax Password: ')

    store_beeswax_credentials(username, password)
