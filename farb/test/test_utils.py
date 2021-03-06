# test_utils.py vi:ts=4:sw=4:expandtab:
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

""" Misc Utilities Unit Tests """

import os
import shutil
import unittest

from farb import utils

# Useful Constants
from farb.test import DATA_DIR
from farb.test.test_builder import BUILDROOT

class CopyRecursiveTestCase(unittest.TestCase):
    """
    Test copyRecursive
    """
    def setUp(self):
        self.copySrc = os.path.join(BUILDROOT, 'Makefile')
        self.copyDst = os.path.join(DATA_DIR, 'testcopy')
        self.copyRecursiveDst = os.path.join(DATA_DIR, 'testrecurse')

    def tearDown(self):
        if (os.path.exists(self.copyRecursiveDst)):
            shutil.rmtree(self.copyRecursiveDst)
        if (os.path.exists(self.copyDst)):
            os.unlink(self.copyDst)

    def test_copyWithOwnership(self):
        utils.copyWithOwnership(self.copySrc, self.copyDst) 
        # TODO Would need root running this test in order to test
        # if the ownership copying code works
        self.assert_(os.path.exists(os.path.join(DATA_DIR, 'testcopy')))

    def test_copyRecursive(self):
        utils.copyRecursive(BUILDROOT, self.copyRecursiveDst) 
        # TODO Would need root running this test in order to test
        # if the ownership copying code works
        self.assert_(os.path.exists(os.path.join(self.copyRecursiveDst, 'Makefile')))
