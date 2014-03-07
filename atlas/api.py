# Atlas client library
# Copyright 2010-2013 - Seyi Ogunyemi
# See LICENSE for details

from urllib.request import urlopen
from urllib.parse import urlencode
from types import MethodType

from atlas.error import AtlasError
from atlas.utils import *

BASE_URL = 'https://atlas.metabroadcast.com/3.0/%s.json'

class API(object):
    """Atlas API"""
    
    def __getattribute__(self, name):
        fn = MethodType(makeFunc(name), self)
        setattr(self, name, MethodType(fn, self))
        return fn
        
def makeFunc(name):
    def call(self, **kw):
        """
        Makes a call to Atlas

        name = Endpoint for Atlas queries
        **kw = Query string arguments to be appended to the base URL
        """
        url = BASE_URL % name
        json = import_simplejson()
        if kw:
            # replace ffrom with from
            # Note: from is a reserved python keyword, therefore
            # cannot be used and as such raises SyntaxError
            if 'ffrom' in kw:
                kw['from'] = kw.pop('ffrom')
            
            url = url + '?' + urlencode(kw)
        try:
            response =  urlopen(url)
        except:
            raise AtlasError("Atlas API IO error")
        mime_type = response.info().get_content_type()
        if (response and mime_type.startswith('application/') and mime_type.endswith('json')):
            result = json.loads(response.readall().decode('utf-8'))
            return result
        else:
            return None
        
    return call
