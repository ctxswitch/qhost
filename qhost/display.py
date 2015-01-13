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

from constants import STATE_CHARS, STATE_COLORS
from color import Color


class Display:
    RED = 0
    GREEN = 1
    GRAY = 2
    BLUE = 3
    TEAL = 4
    RESET = 5

    def __init__(self, color=False, showjobs=False, showprops=False,
                 showtype=False, shownote=False):
        self.color = color
        self.showjobs = showjobs
        self.showprops = showprops
        self.showtype = showtype
        self.shownote = shownote

    def list(self, nodelist):
        print self.header()
        for node in nodelist:
            self.display_node(node)

    def display_node(self, node):
        print self.nodeline(node)
        if self.showprops and len(node.properties) > 0:
            print self.proplines(node)
        if self.showtype and len(node.ntype) > 0:
            print self.typelines(node)
        if self.showjobs and len(node.jobs) > 0:
            print self.joblines(node)

    def header(self):
        line = "%-18s %-7s %-3s %-3s %-8s %-8s %-4s %-4s %-6s  %-8s" % (
            "NODE", "OS", "CPU", "GPU", "MEMTOT",
            "MEMUSE", "JOBS", "SLOT", "LOAD", "STATE"
        )
        if self.shownote:
            line += "    %-17s" % "NOTE"
        line += "\n"
        line += "-" * 80
        if self.shownote:
            line += "-" * 20

        return line

    def nodeline(self, node):
        line = "%s %s %s %s %s %s %s %s %s | %s" % (
            self.out(node.name, pad=18),
            self.out(node.os, pad=7),
            self.out(node.procs, pad=3),
            self.out(node.gpus, pad=3),
            self.memory(node.totmem, pad=8),
            self.memory(node.totmem - node.availmem, pad=8),
            self.out(len(node.jobs), pad=4),
            self.ratio(node.slots, node.procs, pad=4),
            self.ratio(node.loadave, node.procs, pad=6),
            self.state(node.state, pad=8)
        )
        if self.shownote and node.note:
            line += '| ' + node.note
        return line

    def joblines(self, node):
        line = " " * 19
        line += self.pad("Jobs", 12) + ": "
        # Use set to only show unique jobids
        line += ", ".join(node.jobs)
        return self.out(line, color=Color.GRAY)

    def proplines(self, node):
        line = " " * 19
        line += self.pad("Properties", 12) + ": "
        line += ", ".join(node.properties)
        return self.out(line, color=Color.GRAY)

    def typelines(self, node):
        line = " " * 19
        line += self.pad("Node Type", 12) + ": "
        line += node.ntype
        return self.out(line, color=Color.GRAY)

    def seperator(self):
        line = " " * 19
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

    def state(self, values, pad=0):
        arr = [" "] * 9
        if 'N' in values:
            values.remove('N')
        for s in values:
            arr[STATE_CHARS.index(s)] = s

        msg = ''.join(arr[:8])

        if self.color:
            """Use the first states color for all"""
            msg = Color.message(msg, STATE_COLORS[values[0]])

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
            pad_msg = (msg + label + " " * (size - len(msg) -
                       len(label)))[0:size]
        else:
            pad_msg = (msg + " " * (size - len(msg)))[0:size]

        return pad_msg
