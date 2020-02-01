from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import mock
import pytest
from ansible.module_utils import basic
from .common.utils import (
    AnsibleExitJson, ModuleTestCase, set_module_args,
)
from ansible_collections.gurv.vg.plugins.modules import aur


class TestCase(ModuleTestCase):
    def test_main_method(self, mocker):
        set_module_args(tool='pacaur')

        mock_run_command = mock.patch.object(basic.AnsibleModule, 'run_command')
        mock_run_command.return_value = (0, '', '')

        with pytest.raises(AnsibleExitJson) as context:
            aur.main()

        result = context.value.args[0]
        assert result['changed'] is False
