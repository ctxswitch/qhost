import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../'))

from qhost import Parser

class TestParser(unittest.TestCase):
    def test_parse_01(self):
        output = open('output/output_01.xml', 'r').read()
        p = Parser(output).parse()
        n = p[0]
        self.assertEqual(n.name, 'n061')
        self.assertEqual(len(n.jobs), 8)

    def test_parse_02(self):
        output = open('output/output_02.xml', 'r').read()
        p = Parser(output).parse()
        n = p[0]
        self.assertEqual(n.name, 'n061')
        self.assertEqual(len(n.jobs), 8)
        n = p[1]
        self.assertEqual(n.name, 'n062')
        self.assertEqual(len(n.jobs), 8)

    def test_parse_03(self):
        # parses a node in an offline state
        output = open('output/output_03.xml', 'r').read()
        p = Parser(output).parse()
        n = p[0]
        self.assertEqual(n.sessions, [])
        self.assertEqual(n.nsessions, 0)

if __name__ == '__main__':
    unittest.main()
