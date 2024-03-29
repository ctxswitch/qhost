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

import re


class Node:
    def __init__(self, name):
        self.name = name
        self.uname = ''
        self.state = []
        self.sessions = []
        self.nsessions = 0
        self.nusers = 0
        self.physmem = 0
        self.totmem = 0
        self.availmem = 0
        self.procs = 0
        self.jobs = []
        self.loadave = 0
        self.os = ''
        self.gpus = 0
        self.properties = []
        self.ntype = ''
        self.slots = 0
        self.note = ''

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def from_hash(self, attrs):
        for attr, value in list(attrs.items()):
            setattr(self, attr, value)

    def has_job(self, jobid):
        return jobid in self.jobs

    def has_note(self):
        return self.note != ""

    def matches(self, regex):
        match = re.compile(regex)
        return not match.search(self.name) is None

    def state_exclusive_matches(self, states):
        compare_state = sorted(list(states))
        # compare the intersection set to the self.state set
        return set(self.state) & set(compare_state) == set(self.state)

    def state_any_matches(self, states):
        compare_state = list(states)
        return set(compare_state) <= set(self.state)
