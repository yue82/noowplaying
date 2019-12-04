# -*- coding: utf-8 -*-


def read_secrets(filename):
    import os
    script_dir = os.path.abspath(os.path.dirname(__file__))
    secret_dir = '{}/secret'.format('/'.join(script_dir.split('/')[:-1]))
    secret_file = '{}/{}'.format(secret_dir, filename)
    secrets = {}

    with open(secret_file, 'r') as fs:
        for line in fs:
            k, v = line.strip().split(' ')
            secrets[k] = v
    return secrets


def check_status(status_code):
    import sys
    if status_code == 200:
        return True
    func_name = sys._getframe(1).f_code.co_name
    print('Error Status({}): {}'.format(status_code, func_name))
    return False
