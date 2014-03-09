from atlas.api import API
import pprint

'''API examples'''

atlas_client = API()

'''
Inadvertently discovered that there are a TON of results when the publisher is set to  the BBC 

Needless to say, remember to set a limit when uncertain how many results to expect.
'''

items = atlas_client.schedule(from_='now', to='now.plus.24h', channel_id='cbbh', publisher='bbc.co.uk')

pprint.pprint(items)
