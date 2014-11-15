#!/usr/bin/env python
import sys
import os
import glob
import unittest
import test_display
import test_parser

def suite(loader):
    suite = unittest.TestSuite()
    for file in glob.glob("test_*.py"):
        name = file.split('.')[0]
        camelcase = ''.join(map(lambda x: x.capitalize(), name.split('_')))
        tests = loader.loadTestsFromName("%s.%s" % (name, camelcase))
        suite.addTests(tests)
    return suite

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    loader = unittest.TestLoader()
    results = unittest.TextTestRunner(verbosity=2).run(suite(loader))
    if results.wasSuccessful():
	sys.exit(0)
    else:
        sys.exit(1)
