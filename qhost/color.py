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


class Color:
    RED = 0
    GREEN = 1
    GRAY = 2
    BLUE = 3
    TEAL = 4
    RESET = 5

    @staticmethod
    def message(msg, color):
        if color == Color.RED:
            return "\033[31m%s\033[0m" % (msg)
        elif color == Color.GREEN:
            return "\033[1;32m%s\033[0m" % (msg)
        elif color == Color.GRAY:
            return "\033[1;30m%s\033[0m" % (msg)
        elif color == Color.BLUE:
            return "\033[1;34m%s\033[0m" % (msg)
        elif color == Color.TEAL:
            return "\033[36m%s\033[0m" % (msg)
        return msg

    @staticmethod
    def ratio(value, maxval):
        # Get the percentage and return the string with the
        # appropriate color
        msg = ""
        p = float(value) / float(maxval)
        if p >= 1.0:
            msg = Color.message(value, Color.RED)
        elif p >= 0.75 and p < 1.0:
            msg = Color.message(value, Color.RED)
        elif p >= 0.50 and p < 0.75:
            msg = Color.message(value, Color.GREEN)
        elif p >= 0.25 and p < 0.50:
            msg = Color.message(value, Color.GREEN)
        else:
            msg = Color.message(value, Color.BLUE)
        return msg
