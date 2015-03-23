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

    def test_longer_run(self):
        top = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../')
        cmd = [
            os.path.join(top, 'bin', 'qhost'),
            '-X',
            os.path.join(top, 'test', 'output', 'output_04.xml')
        ]
        actual = os.popen(' '.join(cmd)).read()
        expected = open(
            os.path.join(top, 'test', 'output', 'output_04_4.txt')
        ).read()
        self.assertEquals(actual, expected)

    def test_filter_by_state(self):
        top = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../')
        cmd = [
            os.path.join(top, 'bin', 'qhost'),
            '-X',
            os.path.join(top, 'test', 'output', 'output_04.xml'),
            '-s EO -x',
        ]
        actual = os.popen(' '.join(cmd)).read()
        expected = open(
            os.path.join(top, 'test', 'output', 'output_04_1.txt')
        ).read()
        self.assertEquals(actual, expected)

    def test_filter_by_state_ODE(self):
        '''
        State filter on 'ODE'
        '''
        top = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../')
        cmd = [
            os.path.join(top, 'bin', 'qhost'),
            '-X',
            os.path.join(top, 'test', 'output', 'output_05.xml'),
            '-s DEO',
        ]
        actual = os.popen(' '.join(cmd)).read()
        expected = open(
            os.path.join(top, 'test', 'output', 'output_05.txt')
        ).read()
        self.assertEquals(actual, expected)

    def test_filter_by_state_and_node(self):
        top = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../')
        cmd = [
            os.path.join(top, 'bin', 'qhost'),
            '-X',
            os.path.join(top, 'test', 'output', 'output_04.xml'),
            '-s EO -x',
            'n0[35]'
        ]
        actual = os.popen(' '.join(cmd)).read()
        expected = open(
            os.path.join(top, 'test', 'output', 'output_04_2.txt')
        ).read()
        self.assertEquals(actual, expected)

    def test_filter_by_node(self):
        top = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../')
        cmd = [
            os.path.join(top, 'bin', 'qhost'),
            '-X',
            os.path.join(top, 'test', 'output', 'output_04.xml'),
            'n0[15]'
        ]
        actual = os.popen(' '.join(cmd)).read()
        expected = open(
            os.path.join(top, 'test', 'output', 'output_04_3.txt')
        ).read()
        self.assertEquals(actual, expected)

    def test_filter_by_jobid(self):
        top = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../')
        cmd = [
            os.path.join(top, 'bin', 'qhost'),
            '-X',
            os.path.join(top, 'test', 'output', 'output_04.xml'),
            '-J 1158770'
        ]
        actual = os.popen(' '.join(cmd)).read()
        expected = open(
            os.path.join(top, 'test', 'output', 'output_04_5.txt')
        ).read()
        self.assertEquals(actual, expected)

    def test_job_note_notification(self):
        top = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../')
        cmd = [
            os.path.join(top, 'bin', 'qhost'),
            '-X',
            os.path.join(top, 'test', 'output', 'output_06.xml')
        ]
        actual = os.popen(' '.join(cmd)).read()
        expected = open(
            os.path.join(top, 'test', 'output', 'output_06_1.txt')
        ).read()
        self.assertEquals(actual, expected)

    def test_job_note_display(self):
        top = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../')
        cmd = [
            os.path.join(top, 'bin', 'qhost'),
            '-X',
            os.path.join(top, 'test', 'output', 'output_06.xml'),
            '-N'
        ]
        actual = os.popen(' '.join(cmd)).read()
        expected = open(
            os.path.join(top, 'test', 'output', 'output_06_2.txt')
        ).read()
        self.assertEquals(actual, expected)

    def test_any_state_display(self):
        top = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../')
        cmd = [
            os.path.join(top, 'bin', 'qhost'),
            '-X',
            os.path.join(top, 'test', 'output', 'output_07.xml'),
            '-s E'
        ]
        actual = os.popen(' '.join(cmd)).read()
        expected = open(
            os.path.join(top, 'test', 'output', 'output_07_1.txt')
        ).read()
        self.assertEquals(actual, expected)

    def test_exclusive_state_display(self):
        top = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../')
        cmd = [
            os.path.join(top, 'bin', 'qhost'),
            '-X',
            os.path.join(top, 'test', 'output', 'output_07.xml'),
            '-s E -x'
        ]
        actual = os.popen(' '.join(cmd)).read()
        expected = open(
            os.path.join(top, 'test', 'output', 'output_07_2.txt')
        ).read()
        self.assertEquals(actual, expected)
