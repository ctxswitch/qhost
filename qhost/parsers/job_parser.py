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
from base import Base


class JobParser(Base):
    def __init__(self, node, tagname, default=""):
        self.tagname = tagname
        self.node = node
        self.default = ([], 0)

    def convert(self, value):
        jobs = value.split(', ')
        mapped = map(lambda x: x.split('/')[1].split('.')[0], jobs)
        return (set(mapped), len(jobs))
