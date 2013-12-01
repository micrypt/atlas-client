# Atlas client library
# Copyright 2010 - Seyi Ogunyemi
# See LICENSE for details

"""
Atlas  API library
"""
__version__ = '0.2'
__author__ = 'Seyi Ogunyemi'
__license__ = 'MIT'

from atlas.error import AtlasError
from atlas.api import API

# Global, unauthenticated instance of API
api = API()
