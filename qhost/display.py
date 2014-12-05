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


class Display:
    RED = 0
    GREEN = 1
    GRAY = 2
    BLUE = 3
    TEAL = 4
    RESET = 5

    def __init__(self, color=False, showjobs=False, showprops=False, showtype=False):
        self.color = color
        self.showjobs = showjobs
        self.showprops = showprops
        self.showtype = showtype

    def list(self, nodelist):
        print self.header()
        for node in nodelist:
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
            self.mem_out(node.totmem, pad=8),
            self.mem_out(node.totmem - node.availmem, pad=8),
            self.ratio(node.loadave, node.procs, pad=6),
            self.ratio(len(node.jobs), node.procs, pad=4),
            self.state_out(node.state, pad=8)
        )
        return line

    def joblines(self, node):
        line =  " " * 22
        line += self.pad("Jobs", 12) + ": "
        line += ", ".join(node.jobs)
        return self.out(line, color=Display.GRAY)

    def proplines(self, node):
        line =  " " * 22
        line += self.pad("Properties", 12) + ": "
        line += ", ".join(node.properties)
        return self.out(line, color=Display.GRAY)

    def typelines(self, node):
        line =  " " * 22
        line += self.pad("Node Type", 12) + ": "
        line += node.ntype
        return self.out(line, color=Display.GRAY)

    def seperator(self):
        line =  " " * 22
        line += "-" * 5
        line += "\n"
        return line

    def out(self, msg, color=None, pad=0):
        if pad > 1:
            msg = self.pad(msg, pad)

        if self.color and color is not None:
            msg = self.colorize(msg, color)

        return msg

    def mem_out(self, msg, color=None, pad=0):
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

    def state_out(self, value, pad=0):
        """ Valid states are free, offline, down, reserve,
            job-exclusive, job-sharing, busy, time-shared,
            or state-unknown"""
        states = {
            'free': ('F', Display.GREEN, 0),
            'offline': ('O', Display.GRAY, 1),
            'down': ('D', Display.RED, 2),
            'reserve': ('R', Display.TEAL, 3),
            'job-exclusive': ('E', Display.BLUE, 4),
            'job-sharing': ('S', Display.TEAL, 5),
            'time-shared': ('T', Display.TEAL, 6),
            'state-unknown': ('U', Display.RED, 7)
        }

        arr = [" "] * 8
        values = value.split(',')
        for s in values:
            arr[states[s][2]] = states[s][0]

        msg = ''.join(arr)

        if self.color:
            """Use the first states color for all"""
            msg = self.colorize(msg, states[values[0]][1])

        return self.out(msg, pad=0)

    def ratio(self, value, maxval, pad=0):
        if pad > 1:
            value = self.pad(value, pad)

        if self.color:
            value = self.colorize_ratio(value, maxval)

        return value

    def pad(self, msg, size, label=None):
        msg = str(msg)

        if label:
            pad_msg = (msg + label + " " * (size - len(msg) - len(label)))[0:size]
        else:
            pad_msg = (msg + " " * (size - len(msg)))[0:size]

        return pad_msg

    def colorize_ratio(self, value, maxval):
        # Get the percentage and return the string with the
        # appropriate color
        msg = ""
        p = float(value) / float(maxval)
        if p >= 1.0:
            msg = self.colorize(value, Display.RED)
        elif p >= 0.75 and p < 1.0:
            msg = self.colorize(value, Display.RED)
        elif p >= 0.50 and p < 0.75:
            msg = self.colorize(value, Display.GREEN)
        elif p >= 0.25 and p < 0.50:
            msg = self.colorize(value, Display.GREEN)
        else:
            msg = self.colorize(value, Display.BLUE)
        return msg

    def colorize(self, msg, color):
        if color == Display.RED:
            return "\033[31m%s\033[0m" % (msg)
        elif color == Display.GREEN:
            return "\033[1;32m%s\033[0m" % (msg)
        elif color == Display.GRAY:
            return "\033[1;30m%s\033[0m" % (msg)
        elif color == Display.BLUE:
            return "\033[1;34m%s\033[0m" % (msg)
        elif color == Display.TEAL:
            return "\033[36m%s\033[0m" % (msg)
        return msg
