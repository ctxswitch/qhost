#!/usr/bin/env python3
# Copyright 2014, Rob Lyon <rob@ctxswitch.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from qhost.constants import VERSION
from distutils.core import setup

import os
import sys
lib_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
if lib_path not in sys.path:
    sys.path.insert(0, lib_path)

setup(
    name='qhost',
    version=VERSION,
    author='Rob Lyon <rob@ctxswitch.com>',
    url='http://rlyon.me',
    packages=['qhost'],
    scripts=['bin/qhost']
)
