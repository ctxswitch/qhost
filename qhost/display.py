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

    def __init__(self, color=False, showjobs=False):
        self.color = color
        self.showjobs = showjobs

    def list(self, nodelist):
        print self.header()
        for node in nodelist:
            print self.nodeline(node)
            if self.showjobs and len(node.jobs) > 0:
                print self.joblines(node)

    def header(self):
        line = "%-16s %-4s %-4s %-12s %-12s %-12s %-8s %-16s\n" % (
            "Node", "CPUs", "Jobs", "Memory", "Total", "Avail", "Load", "State"
        )
        line += "-" * 80
        return line

    def nodeline(self, node):
        line = "%s %s %s %s %s %s %s %s" % (
            self.out(node.name, pad=16),
            self.out(node.procs, color=Display.BLUE, pad=4),
            self.ratio(len(node.jobs), node.procs, 4),
            self.mem_out(node.physmem, pad=12),
            self.mem_out(node.totmem, pad=12),
            self.mem_out(node.availmem, pad=12),
            self.ratio(node.loadave, node.procs, pad=8),
            self.pad(node.state, 16)
        )
        return line

    def joblines(self, node):
        line = ""
        for job in node.jobs:
            line += " * %s\n" % (job)
        return self.out(line, color=Display.TEAL)

    def out(self, msg, color=None, pad=0):
        if pad > 1:
            msg = self.pad(msg, pad)

        if self.color and color is not None:
            msg = self.colorize(msg, color)

        return msg

    def mem_out(self, msg, color=None, pad=0):

        def sizeof_fmt(num):
            """ provide converted {''/K/.../Z}-byte and unit label """
            for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
                if abs(num) < 1024.0:
                    return "%3.2f" % num, unit
                num /= 1024.0
            return "%.2f" % num, 'Yi'

        if pad > 1:
            msg, unit = sizeof_fmt(int(msg) * 1024)  # convert kilobyte to byte
            msg = self.pad(msg, pad, label=unit)

        return msg

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
