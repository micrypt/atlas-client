# Atlas client library
# Copyright 2010-2014 - Seyi Ogunyemi
# See LICENSE for details

"""
Atlas  API library
"""
__version__ = '0.3'
__author__ = 'Seyi Ogunyemi'
__license__ = 'MIT'

from atlas.error import AtlasError
from atlas.api import API

# Global, unauthenticated instance of API
api = API()
