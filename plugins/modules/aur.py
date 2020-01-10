#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2019, Vladimir Gurinovich <vladimir.gurinovich@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Прототип: https://github.com/cdown/ansible-aur

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
}

DOCUMENTATION = '''
---
module: aur
short_description: Работа с репозиторием AUR
description:
    - TODO
version_added: "2.8"
author:
    - Vladimir Gurinovich (@gurv)
options:
    name:
      description:
        - Имя пакета.
      type: str
    state:
      description:
        - Состояние после выполнения.
      type: str
      choices: [ 'present', 'absent' ]
      default: 'present'
    tool:
      description:
        - Инструмент-оболочка.
      type: str
      choices: [ 'pacaur', 'yaourt' ]
      default: 'pacaur'
    recurse:
      description:
        - TODO
      type: bool
      default: True
    nosave:
      description:
        - TODO
      type: bool
      default: True
    update:
      description:
        - TODO
      type: bool
      default: False
    auronly:
      description:
        - TODO
      type: bool
      default: True
requirements:
    - "python >= 2.6"
'''

EXAMPLES = '''
# TODO
'''

RETURN = '''
# TODO
'''

from ansible.module_utils.basic import AnsibleModule

TOOL_CMD_MAP = {
    'pacaur': ['env', 'EDITOR=cat', 'pacaur', '--noconfirm', '--noedit'],
    'yaourt': ['yaourt', '--noconfirm'],
}


def package_installed(module, package_name):
    cmd = ['pacman', '-Q', package_name]
    rc, _stdout, _stderr = module.run_command(cmd, check_rc=False)
    return rc == 0


def update_packages(module, tool, auronly):
    if tool not in TOOL_CMD_MAP:
        raise AssertionError("BUG: tool not in TOOL_CMD_MAP")

    cmd = ['env', 'LC_ALL=C'] + TOOL_CMD_MAP[tool] + ['-Su']
    if auronly:
        cmd += ['--aur']
    stdout = module.run_command(cmd, check_rc=True)

    module.exit_json(
        changed='there is nothing to do' not in stdout,
        msg='updated packages',
    )


def install_packages(module, package_name, tool, update, auronly):
    if package_installed(module, package_name):
        module.exit_json(
            changed=False,
            msg='package already installed',
        )

    if tool not in TOOL_CMD_MAP:
        raise AssertionError("BUG: tool not in TOOL_CMD_MAP")

    options = '-S'

    if update:
        options += 'u'

    cmd = TOOL_CMD_MAP[tool] + [options, package_name]
    if auronly:
        cmd += ['--aur']
    module.run_command(cmd, check_rc=True)

    module.exit_json(
        changed=True,
        msg='installed package',
    )


def remove_packages(module, package_name, recurse, nosave):
    if not package_installed(module, package_name):
        module.exit_json(
            changed=False,
            msg='package not installed',
        )

    options = '-R'

    if nosave:
        options += 'n'

    if recurse:
        options += 's'

    cmd = ['pacman', '--noconfirm', options, package_name]
    module.run_command(cmd, check_rc=True)

    module.exit_json(
        changed=True,
        msg='removed package',
    )


def main():
    module = AnsibleModule(
        argument_spec={
            'name': {
                'required': False,
            },
            'state': {
                'default': 'present',
                'choices': ['present', 'absent'],
            },
            'tool': {
                'default': 'pacaur',
                'choices': ['pacaur', 'yaourt'],
            },
            'recurse': {
                'default': True,
                'type': 'bool',
            },
            'nosave': {
                'default': True,
                'type': 'bool',
            },
            'update': {
                'default': False,
                'type': 'bool',
            },
            'auronly': {
                'default': True,
                'type': 'bool',
            },
        },
        required_one_of=[['name', 'update']],
    )

    params = module.params

    if params['update'] and not params['name']:
        update_packages(module, params['tool'], params['auronly'])
    elif params['state'] == 'present':
        install_packages(
            module, params['name'], params['tool'], params['update'],
            params['auronly'],
        )
    elif params['state'] == 'absent':
        remove_packages(
            module, params['name'], params['recurse'], params['nosave'],
        )


if __name__ == '__main__':
    main()
