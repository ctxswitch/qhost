# Copyright 2015, Rob Lyon <nosignsoflifehere@gmail.com>
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
from .base import Base


class StatusParser(Base):
    def __init__(self, node, tagname, default=""):
        self.tagname = tagname
        self.node = node
        self.default = {}

    def convert(self, text):
        items = text.split(',')
        d = {}
        for item in items:
            i = item.split('=')
            key = i[0]
            value = i[1]
            if value and not value[0] == '?':
                d[key] = value

        retval = {}
        if 'physmem' in d:
            retval['physmem'] = int(d['physmem'][:-2])
        if 'availmem' in d:
            retval['availmem'] = int(d['availmem'][:-2])
        if 'totmem' in d:
            retval['totmem'] = int(d['totmem'][:-2])
        if 'nusers' in d:
            retval['nusers'] = int(d['nusers'])
        if 'sessions' in d:
            retval['sessions'] = [int(x) for x in d['sessions'].split()]
        if 'nsessions' in d:
            retval['nsessions'] = int(d['nsessions'])
        if 'loadave' in d:
            retval['loadave'] = float(d['loadave'])
        if 'uname' in d:
            retval['uname'] = d['uname']
        if 'opsys' in d:
            retval['os'] = d['opsys']

        return retval
