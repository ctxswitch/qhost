from qhost import Parser
import unittest


class TestParser(unittest.TestCase):
    def test_parse_01(self):
        output = open('./test/output/output_01.xml', 'r').read()
        p = Parser(output).parse()
        n = p[0]
        self.assertEqual(n.name, 'n061')
        self.assertEqual(len(n.jobs), 1)

    def test_parse_02(self):
        output = open('./test/output/output_02.xml', 'r').read()
        p = Parser(output).parse()
        n = p[0]
        self.assertEqual(n.name, 'n061')
        self.assertEqual(len(n.jobs), 1)
        n = p[1]
        self.assertEqual(n.name, 'n062')
        self.assertEqual(len(n.jobs), 1)

    def test_parse_03(self):
        # parses a node in an offline state
        output = open('./test/output/output_03.xml', 'r').read()
        p = Parser(output).parse()
        n = p[0]
        self.assertEqual(n.sessions, [])
        self.assertEqual(n.nsessions, 0)


if __name__ == '__main__':
    unittest.main()
