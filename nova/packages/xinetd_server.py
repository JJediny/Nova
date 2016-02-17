# -*- encoding: utf-8 -*-
'''
:rational: If there are no xinetd services required, it is recommended that the
daemon be deleted from the system.

:maintainer: HubbleStack
:maturity: 20160216
:depends: SaltStack
:platform: Linux
:compatibility: all

'''
from __future__ import absolute_import
from nova import *
import logging


def __virtual__():
    '''
    Compatibility Check
    '''
    if not salt.utils.is_windows():
        return True
    return False


def audit():
    if not _package('xinetd'):
        return True
    return False