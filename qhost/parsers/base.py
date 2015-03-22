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


class Base:
    def __init__(self, node, tagname, default=""):
        self.tagname = tagname
        self.node = node
        self.default = default

    def parse(self):
        try:
            value = self.node_handler(
                self.node.getElementsByTagName(self.tagname)[0]
            )
            return self.convert(value)
        except KeyError:
            return self.default
        except IndexError:
            return self.default

    def convert(self, value):
        return value

    def node_handler(self, node):
        return self.text_handler(node.childNodes)

    def text_handler(self, children):
        text = ""
        for child in children:
            if child.nodeType == child.TEXT_NODE:
                text = text + child.data
        return text.strip()
