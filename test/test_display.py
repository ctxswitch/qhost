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
        self.assertEqual(len(o), 10)
        self.assertEqual(o, "m         ")

        o = self.display.pad("message", 4)
        self.assertEqual(len(o), 4)
        self.assertEqual(o, "mess")

    def test_memout(self):
        o = self.display.memory("1024", pad=4)
        self.assertEqual(len(o), 4)
        self.assertEqual(o, "1.0M")

        o = self.display.memory("1048576", pad=4)
        self.assertEqual(len(o), 4)
        self.assertEqual(o, "1.0G")

        o = self.display.memory("1073741824", pad=4)
        self.assertEqual(len(o), 4)
        self.assertEqual(o, "1.0T")

        o = self.display.memory("1536", pad=4)
        self.assertEqual(len(o), 4)
        self.assertEqual(o, "1.5M")

        o = self.display.memory("1572864", pad=4)
        self.assertEqual(len(o), 4)
        self.assertEqual(o, "1.5G")

        o = self.display.memory("536870912", pad=6)
        self.assertEqual(len(o), 6)
        self.assertEqual(o, "512.0G")

        o = self.display.memory("2684354560", pad=4)
        self.assertEqual(len(o), 4)
        self.assertEqual(o, "2.5T")

if __name__ == "__main__":
    unittest.main()
