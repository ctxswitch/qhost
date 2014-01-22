import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../'))

from qhost import Display

class TestDisplay(unittest.TestCase):
    def setUp(self):
        self.display = Display()

    def test_padding(self):
        o = self.display.pad("m", 10)
        self.assertEquals(len(o), 10)
        self.assertEquals(o, "m         ")

        o = self.display.pad("message", 4)
        self.assertEquals(len(o), 4)
        self.assertEquals(o, "mess")

if __name__ == "__main__":
    unittest.main()
