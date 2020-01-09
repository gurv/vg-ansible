# -*- coding: utf-8 -*-
# Copyright: (c) 2020
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


class Error(Exception):
    u'Базовая ошибка.'


class HttpError(Error):
    u'Ошибка HTTP-соединения.'


class SyncError(Error):
    u'Ошибка синхронизации состояния.'
