# __init__.py vi:ts=4:sw=4:expandtab:
#
# Copyright (c) 2006-2008 Three Rings Design, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. Neither the name of the copyright owner nor the names of contributors
#    may be used to endorse or promote products derived from this software
#    without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import os

__all__ = ['builder', 'config', 'runner', 'utils', 'sysinstall', 'test']

# General Info
__version__ = '1.0'
__license__ = 'BSD License'
__author__ = 'Three Rings Design, Inc.'
__author_email__ = 'dpw@threerings.net'
__copyright__ = 'Copyright (C) 2006-2008 Three Rings Design, Inc. All rights reserved.'

# Useful Constants
LOG_NAME = 'farb:'
INSTALL_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(INSTALL_DIR, 'data')

# Resources
CONFIG_SCHEMA = os.path.join(DATA_DIR, "farb_conf.xml")
INSTALL_PACKAGE_SH = os.path.join(DATA_DIR, "install_package.sh")
BOOT_CONF_TMPL = os.path.join(DATA_DIR, "boot.conf.tmpl")
LOADER_RC = os.path.join(DATA_DIR, "loader.rc")
LOADER_CONF = os.path.join(DATA_DIR, "loader.conf")
NETINSTALL_FORTH_TMPL = os.path.join(DATA_DIR, "netinstall.4th.tmpl")

# Exceptions
class FarbError(Exception):
    pass
