#!/usr/bin/env python
#from distutils.core import setup
from setuptools import setup, find_packages

setup(name="atlas-client",
      version="0.3",
      description="An Atlas library for python",
      license="MIT",
      author="Seyi Ogunyemi",
      author_email="micrypt@gmail.com",
      url="http://github.com/micrypt/atlas-client",
      packages = find_packages(),
      keywords= "atlas library",
      zip_safe = True)
