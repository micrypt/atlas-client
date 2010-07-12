import unittest

from atlas import *

"""Unit tests"""

class AtlasAPITests(unittest.TestCase):

    def setUp(self):
        self.api = API()

    def testitems(self):
        self.api.items(genre='http://ref.atlasapi.org/genres/atlas/factual', publisher='bbc.co.uk')

    def testbrands(self):
        self.api.brands(title='east', availableCountries='uk', publisher='bbc.co.uk')

    def testplaylists(self):
        self.api.playlists(publisher='bbc.co.uk', limit=5)

if __name__ == '__main__':

    unittest.main()

