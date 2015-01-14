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

VERSION = '1.3.3'

""" Valid states are free, offline, down, reserve,
    job-exclusive, job-sharing, busy, time-shared,
    or state-unknown"""
STATES = {
    'free': 'F',
    'offline': 'O',
    'down': 'D',
    'reserve': 'R',
    'job-exclusive': 'E',
    'job-sharing': 'S',
    'time-shared': 'T',
    'state-unknown': 'U',
}

STATE_COLORS = {
    'F': Color.GREEN,
    'O': Color.GRAY,
    'D': Color.RED,
    'R': Color.TEAL,
    'E': Color.BLUE,
    'S': Color.TEAL,
    'T': Color.TEAL,
    'U': Color.RED,
}

STATE_CHARS = ['F', 'O', 'D', 'R', 'E', 'S', 'T', 'U']
