# -*- coding: utf-8 -*-
# Copyright: (c) 2020
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import os
import tempfile
from datetime import datetime


DEBUG = os.environ.get("VG_ANSIBLE_DEBUG", "").lower() in ["yes", "true"]


def log(message, *args, **kwargs):
    """
    Log message to a file (/tmp/vg-ansible.log) at remote target
    """
    if DEBUG:
        with open(os.path.join(tempfile.gettempdir(), "vg-ansible.log"), "a") as f:
            f.write("[{0}]: {1}\n".format(datetime.utcnow(), message.format(*args, **kwargs)))
