# -*- coding: utf-8 -*-
# Copyright: (c) 2020
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


def dict_to_single_item_dicts(data):
    return [{k: v} for k, v in data.items()]


def dict_to_key_value_strings(data):
    return ["{0}={1}".format(k, v) for k, v in data.items()]
