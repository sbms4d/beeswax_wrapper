#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
For setting and returning beeswax passwords (visible only to current environment user).
"""
from __future__ import unicode_literals

import keyring
import getpass
import os
import argparse

beeswax_file_name = '/data/beeswax_user.txt'


def store_beeswax_credentials(usrnm, psswrd):
    """
    Store password in environment's keyring

    :param str|unicode usrnm: Beeswax username/email
    :param str|unicode psswrd: Beeswax password
    """
    keyring.set_password("beeswax", usrnm, psswrd)
    with open(beeswax_file_name, 'w') as fw:
        fw.write(usrnm)


def get_beeswax_credentials():
    """
    Retrieve stored beeswax credentials
    :rtype: dict[str|unicode, str|unicode]
    :return: beeswax credentials, e.g. {"username":"foo", "password":"bar"}
    """

    if not os.path.exists(beeswax_file_name):
        return {}

    with open(beeswax_file_name) as fr:
        user_name = fr.read().strip()

    return {'username': user_name, 'password': keyring.get_password("beeswax", user_name)}


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
