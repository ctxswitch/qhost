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
from constants import *
from color import Color

class Display:
    RED = 0
    GREEN = 1
    GRAY = 2
    BLUE = 3
    TEAL = 4
    RESET = 5

    def __init__(self, color=False, showjobs=False, showprops=False, showtype=False, noderegex=".*", statestring=None):
        self.color = color
        self.showjobs = showjobs
        self.showprops = showprops
        self.showtype = showtype
        self.noderegex = re.compile(noderegex)
        self.statestring = statestring

    def list(self, nodelist):
        print self.header()
        for node in nodelist:
            if self.matched_node(node.name) and self.matched_state(node.state):
                self.display_node(node)

    def matched_node(self, name):
        return not self.noderegex.search(name) is None

    def matched_state(self, states):
        # States come in as human readable, there's a good chance
        # this will change in the future, but for right now we need
        # to convert them to chars
        s = map(lambda x: STATES[x][0], states.split(','))
        ss = list(self.statestring)
        return list(set(s) & set(ss)) == s

    def display_node(self, node):
        print self.nodeline(node)
        if self.showprops and len(node.properties) > 0:
            print self.proplines(node)
        if self.showtype and len(node.ntype) > 0:
            print self.typelines(node)
        if self.showjobs and len(node.jobs) > 0:
            print self.joblines(node)

    def header(self):
        line = "%-21s %-8s %-3s %-3s %-8s %-8s %-6s %-4s   %-8s\n" % (
            "NODE", "OS", "CPU", "GPU", "MEMTOT", "MEMUSE", "LOAD", "JOBS", "STATE"
        )
        line += "-" * 79
        return line

    def nodeline(self, node):
        line = "%s %s %s %s %s %s %s %s | %s" % (
            self.out(node.name, pad=21),
            self.out(node.os, pad=8),
            self.out(node.procs, pad=3),
            self.out(node.gpus, pad=3),
            self.memory(node.totmem, pad=8),
            self.memory(node.totmem - node.availmem, pad=8),
            self.ratio(node.loadave, node.procs, pad=6),
            self.ratio(len(node.jobs), node.procs, pad=4),
            self.state(node.state, pad=8)
        )
        return line

    def joblines(self, node):
        line =  " " * 22
        line += self.pad("Jobs", 12) + ": "
        line += ", ".join(node.jobs)
        return self.out(line, color=Color.GRAY)

    def proplines(self, node):
        line =  " " * 22
        line += self.pad("Properties", 12) + ": "
        line += ", ".join(node.properties)
        return self.out(line, color=Color.GRAY)

    def typelines(self, node):
        line =  " " * 22
        line += self.pad("Node Type", 12) + ": "
        line += node.ntype
        return self.out(line, color=Color.GRAY)

    def seperator(self):
        line =  " " * 22
        line += "-" * 5
        line += "\n"
        return line

    def out(self, msg, color=None, pad=0):
        if pad > 1:
            msg = self.pad(msg, pad)

        if self.color and color is not None:
            msg = Color.message(msg, color)

        return msg

    def memory(self, msg, color=None, pad=0):
        val = int(msg)
        unit = 'K'

        units = ['M', 'G', 'T']
        for u in units:
            if val < 1024.0:
                break
            else:
                val /= 1024.0
                unit = u

        return self.out("%3.1f%s" % (val, unit), pad=pad)

    def state(self, value, pad=0):
        arr = [" "] * 8
        values = value.split(',')
        for s in values:
            arr[STATES[s][2]] = STATES[s][0]

        msg = ''.join(arr)

        if self.color:
            """Use the first states color for all"""
            msg = Color.message(msg, STATES[values[0]][1])

        return self.out(msg, pad=0)

    def ratio(self, value, maxval, pad=0):
        if pad > 1:
            value = self.pad(value, pad)

        if self.color:
            value = Color.ratio(value, maxval)

        return value

    def pad(self, msg, size, label=None):
        msg = str(msg)

        if label:
            pad_msg = (msg + label + " " * (size - len(msg) - len(label)))[0:size]
        else:
            pad_msg = (msg + " " * (size - len(msg)))[0:size]

        return pad_msg
