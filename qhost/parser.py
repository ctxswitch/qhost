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
        nodelist = []
        for node in nodes:
            nodelist.append(self.handle_node(node))

        return nodelist

    def handle_node(self, node):
        name = self.handle_node_name(node.getElementsByTagName("name")[0])
        procs = self.handle_node_procs(node.getElementsByTagName("np")[0])
        state = self.handle_node_state(node.getElementsByTagName("state")[0])
        status = self.handle_node_status(node.getElementsByTagName("status")[0])
        if node.getElementsByTagName("jobs"):
            jobs = self.handle_node_jobs(node.getElementsByTagName("jobs")[0])
        else:
            jobs = []

        node = Node(name)
        node.procs = procs
        node.state = state
        node.physmem = status['physmem']
        node.availmem = status['availmem']
        node.totmem = status['totmem']
        node.nusers = status['nusers']
        node.sessions = status['sessions']
        node.nsessions = status['nsessions']
        node.loadave = status['loadave']
        node.uname = status['uname']
        node.os = status['os']
        node.jobs = jobs
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
            if value and value[0] == '?':
                value = '0'
            d[key] = value

        return {
            'physmem': int(d['physmem'][:-2]),
            'availmem': int(d['availmem'][:-2]),
            'totmem': int(d['totmem'][:-2]),
            'nusers': int(d['nusers']),
            'sessions': int(d['sessions']),
            'nsessions': int(d['nsessions']),
            'loadave': float(d['loadave']),
            'uname': d['uname'],
            'os': d['opsys']
        }

    def handle_node_jobs(self, node):
        return self.getText(node.childNodes).split(', ')

    def getText(self, nodelist):
        rc = ""
        for node in nodelist:
            if node.nodeType == node.TEXT_NODE:
                rc = rc + node.data
        return rc.strip()
