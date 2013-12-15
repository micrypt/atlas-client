import unittest

from atlas import *

"""Unit tests"""

class AtlasAPITests(unittest.TestCase):

    def setUp(self):
        self.api = API()

    def testcontent(self):
        self.api.content(uri='http://www.bbc.co.uk/programmes/b007rsj5', annotations='description,brand_summary,series_summary')

    def testbrands(self):
        self.api.brands(title='east', availableCountries='uk', publisher='bbc.co.uk')

    def testplaylists(self):
        self.api.playlists(publisher='bbc.co.uk', limit=5)

if __name__ == '__main__':

    unittest.main()

