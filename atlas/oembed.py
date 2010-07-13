# Contribution by Adam T. Lindsay

from atlas.api import call

ITEMS_OEMBED = 'http://atlasapi.org/2.0/items.oembed.json'
BRANDS_OEMBED = 'http://atlasapi.org/2.0/brands.oembed.json'
PLAYLISTS_OEMBED = 'http://atlasapi.org/2.0/playlists.oembed.json'

class OEmbed(object):
    """Fetch the OEmbed versions of objects."""

    def items(self, *args, **kw):
        self.response = call(ITEMS_OEMBED, **kw)
        return self.response

    def brands(self, *args, **kw):
        self.response = call(BRANDS_OEMBED, **kw)
        return self.response

    def playlists(self, *args, **kw):
        self.response = call(PLAYLISTS_OEMBED, **kw)
        return self.response
