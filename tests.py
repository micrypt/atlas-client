import unittest

from atlas import *

"""Unit tests"""

class AtlasAPITests(unittest.TestCase):

    def setUp(self):
        self.api = API()

    def testcontent(self):
        self.api.content(uri='http://www.bbc.co.uk/programmes/b007rsj5', annotations='description,brand_summary,series_summary')

if __name__ == '__main__':
    unittest.main()
