# Copyright 2014, Rob Lyon <nosignsoflifehere@gmail.com>
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


class NodeList:
    def __init__(self):
        self.nodes = []
        self.filters = {}

    def __iter__(self):
        for node in self.nodes:
            if self.matches(node):
                yield node

    def __getitem__(self, index):
        return self.nodes[index]

    def add(self, node):
        self.nodes.append(node)

    def add_filter(self, filter, value):
        if value:
            self.filters[filter] = value

    def matches(self, node):
        for key, value in self.filters.iteritems():
            if not getattr(self, "filter_by_%s" % key)(node, value):
                return False
        return True

    def filter_by_jobid(self, node, jobid):
        return node.has_job(jobid)

    def filter_by_node_regex(self, node, regex):
        return node.matches(regex)

    def filter_by_state(self, node, state):
        return node.state_matches(state)
