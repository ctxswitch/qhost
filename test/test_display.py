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

    def test_memout(self):
        o = self.display.mem_out("1024", pad=5)
        self.assertEquals(len(o), 5)
        self.assertEquals(o, "1.00M")

        o = self.display.mem_out("1048576", pad=5)
        self.assertEquals(len(o), 5)
        self.assertEquals(o, "1.00G")

        o = self.display.mem_out("1073741824", pad=5)
        self.assertEquals(len(o), 5)
        self.assertEquals(o, "1.00T")

        o = self.display.mem_out("1536", pad=5)
        self.assertEquals(len(o), 5)
        self.assertEquals(o, "1.50M")

        o = self.display.mem_out("1572864", pad=5)
        self.assertEquals(len(o), 5)
        self.assertEquals(o, "1.50G")

        o = self.display.mem_out("536870912", pad=7)
        self.assertEquals(len(o), 7)
        self.assertEquals(o, "512.00G")

        o = self.display.mem_out("2684354560", pad=5)
        self.assertEquals(len(o), 5)
        self.assertEquals(o, "2.50T")

if __name__ == "__main__":
    unittest.main()
