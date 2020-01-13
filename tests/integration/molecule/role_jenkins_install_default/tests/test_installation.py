# -*- coding: utf-8 -*-
#
# Copyright: (c) 2020
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


def test_jenkins_installed(host):
    assert host.exists("jenkins")
