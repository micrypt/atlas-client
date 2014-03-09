# Atlas client library
# Copyright 2010-2014 - Seyi Ogunyemi
# See LICENSE for details

class AtlasError(Exception):
    """Atlas exception"""
    def __init__(self, reason, response=None):
        self.reason = str(reason)
        self.response = response

    def __str__(self):
        return self.reason
