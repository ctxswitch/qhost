import unittest
import sys
import os

class TestBin(unittest.TestCase):
    def test_run(self):
        top = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../')
        cmd = [
            os.path.join(top, 'bin', 'qhost'),
            '-X',
            os.path.join(top, 'test', 'output', 'output_00.xml')
        ]
        actual = os.popen(' '.join(cmd)).read()
        expected = open(
            os.path.join(top, 'test', 'output', 'output_00.txt')
        ).read()
        self.assertEquals(actual, expected)
