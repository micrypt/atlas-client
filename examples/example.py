from atlas.api import API
import pprint

'''API examples'''

atlas_client = API()

'''Fetch the CBBC schedule for the next 24 hours'''

items = atlas_client.schedule(from_='now', to='now.plus.24h', channel_id='cbbh', publisher='bbc.co.uk')

pprint.pprint(items)
