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

from color import Color

VERSION = '1.2.1'

""" Valid states are free, offline, down, reserve,
    job-exclusive, job-sharing, busy, time-shared,
    or state-unknown"""
STATES = {
    'free':             ('F', Color.GREEN,    0),
    'offline':          ('O', Color.GRAY,     1),
    'down':             ('D', Color.RED,      2),
    'reserve':          ('R', Color.TEAL,     3),
    'job-exclusive':    ('E', Color.BLUE,     4),
    'job-sharing':      ('S', Color.TEAL,     5),
    'time-shared':      ('T', Color.TEAL,     6),
    'state-unknown':    ('U', Color.RED,      7)
}

STATE_CHARS = [ 'F', 'O', 'D', 'R', 'E', 'S', 'T', 'U' ]

STATE_DEFAULT = "FODRESTU"
