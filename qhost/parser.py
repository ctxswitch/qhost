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
import xml.dom.minidom
from qhost import Node
from qhost import NodeList
from constants import STATES


class Parser:
    def __init__(self, qxml):
        self.qxml = qxml

    def parse(self):
        return self.handle_data()

    def handle_data(self):
        dom = xml.dom.minidom.parseString(self.qxml)
        nodes = dom.getElementsByTagName("Node")
        return self.handle_nodes(nodes)

    def handle_nodes(self, nodes):
        nodelist = NodeList()
        for node in nodes:
            nodelist.add(self.handle_node(node))

        return nodelist

    def handle_node(self, node):
        name = self.handle_node_name(node.getElementsByTagName("name")[0])
        procs = self.handle_node_procs(node.getElementsByTagName("np")[0])

        try:
            gpus = self.handle_node_procs(node.getElementsByTagName("gpus")[0])
        except:
            gpus = ""

        state = self.handle_node_state(node.getElementsByTagName("state")[0])

        try:
            properties = self.handle_node_state(
                node.getElementsByTagName("properties")[0]).split(',')
        except:
            properties = ""

        ntype = self.handle_node_state(node.getElementsByTagName("ntype")[0])

        try:
            status = self.handle_node_status(
                node.getElementsByTagName("status")[0])
        except:
            status = ""

        if node.getElementsByTagName("jobs"):
            j = self.handle_node_jobs(node.getElementsByTagName("jobs")[0])

            jb = []
            for item in j:
                jb.append(item.split(','))
            # flatten the list of lists
            jb = [item for sublist in jb for item in sublist]

            jobs = map(lambda x: x.split('/')[1].split('.')[0], jb)
        else:
            jobs = []

        node = Node(name)
        node.procs = procs
        node.gpus = gpus
        node.state = sorted(map(lambda x: STATES[x][0], state.split(',')))
        node.properties = properties
        node.ntype = ntype
        node.slots = len(jobs)
        node.jobs = set(jobs)

        if 'physmem' in status:
            node.physmem = status['physmem']
        if 'availmem' in status:
            node.availmem = status['availmem']
        if 'totmem' in status:
            node.totmem = status['totmem']
        if 'nusers' in status:
            node.nusers = status['nusers']
        if 'sessions' in status:
            node.sessions = status['sessions']
        if 'nsessions' in status:
            node.nsessions = status['nsessions']
        if 'loadave' in status:
            node.loadave = status['loadave']
        if 'uname' in status:
            node.uname = status['uname']
        if 'os' in status:
            node.os = status['os']

        return node

    def handle_node_name(self, node):
        return self.getText(node.childNodes).strip()

    def handle_node_procs(self, node):
        return int(self.getText(node.childNodes).strip())

    def handle_node_state(self, node):
        return self.getText(node.childNodes).strip()

    def handle_node_status(self, node):
        text = self.getText(node.childNodes).strip()
        items = text.split(',')
        d = {}
        for item in items:
            i = item.split('=')
            key = i[0]
            value = i[1]
            if value and not value[0] == '?':
                d[key] = value

        retval = {}
        if 'physmem' in d:
            retval['physmem'] = int(d['physmem'][:-2])
        if 'availmem' in d:
            retval['availmem'] = int(d['availmem'][:-2])
        if 'totmem' in d:
            retval['totmem'] = int(d['totmem'][:-2])
        if 'nusers' in d:
            retval['nusers'] = int(d['nusers'])
        if 'sessions' in d:
            retval['sessions'] = map(lambda x: int(x), d['sessions'].split())
        if 'nsessions' in d:
            retval['nsessions'] = int(d['nsessions'])
        if 'loadave' in d:
            retval['loadave'] = float(d['loadave'])
        if 'uname' in d:
            retval['uname'] = d['uname']
        if 'opsys' in d:
            retval['os'] = d['opsys']

        return retval

    def handle_node_jobs(self, node):
        return self.getText(node.childNodes).split(', ')

    def getText(self, nodelist):
        rc = ""
        for node in nodelist:
            if node.nodeType == node.TEXT_NODE:
                rc = rc + node.data
        return rc.strip()
