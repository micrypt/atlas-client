from atlas.api import API
import pprint

"""API examples"""

atlas_client = API()

"""
Inadvertently discovered that there are a TON of results when the publisher is set to  the BBC 

Needless to say, remember to set a limit when uncertain how many results to expect.
"""
items = atlas_client.playlists(publisher='bbc.co.uk', limit='2')

pprint.pprint(items)
