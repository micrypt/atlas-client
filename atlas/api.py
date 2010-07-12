# Atlas client library
# Copyright 2010 - Seyi Ogunyemi
# See LICENSE for details

import urllib
from atlas.error import AtlasError
from atlas.utils import *

ITEMS_URL = 'http://atlasapi.org/2.0/items.json'
BRANDS_URL = 'http://atlasapi.org/2.0/brands.json'
PLAYLISTS_URL = 'http://atlasapi.org/2.0/playlists.json'

class API(object):
    """Atlas API"""

    def items(self, *args, **kw):
        self.response = call(ITEMS_URL, **kw)
        return self.response

    def brands(self, *args, **kw):
        self.response = call(BRANDS_URL, **kw)
        return self.response

    def playlists(self, *args, **kw):
        self.response = call(PLAYLISTS_URL, **kw)
        return self.response

def call(url, **kw):
    """
    Makes a call to Atlas

    url = Base url for Atlas queries
    **kw = Query string arguments to be appended to the base URL
    """
    json = import_simplejson()
    if kw:
        url = url + '?' + urllib.urlencode(kw)
    print url
    try:
        response =  urllib.urlopen(url)
    except:
        raise AtlasError("Atlas API IO error")
    mime_type = response.info().type
    if ((mime_type  == 'application/json') and response):
        result = json.load(response)
    return result
