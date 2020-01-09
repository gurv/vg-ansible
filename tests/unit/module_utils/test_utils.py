# -*- coding: utf-8 -*-
# Copyright: (c) 2020
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import pytest

from ansible_collections.gurv.vg.plugins.module_utils import (
    utils,
)


class TestDictToSingleItemDicts:
    def test_conversion(self):
        result = utils.dict_to_single_item_dicts({"a": 0, 1: "b"})

        assert 2 == len(result)
        for item in ({"a": 0}, {1: "b"}):
            assert item in result


class TestDictToKeyValueString:
    def test_conversion(self):
        result = utils.dict_to_key_value_strings({"a": 0, 1: "b"})

        assert {"a=0", "1=b"} == set(result)
