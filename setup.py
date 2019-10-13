#!/usr/bin/env python
import sys
import setuptools
from distutils.core import setup

setup(name='rotate-proxies',
        version='0.1',
        description='Scrapy Proxies: random proxy middleware for Scrapy',
        author='Nabin Khadka',
        author_email='nbnkhadka14@gmail.com',
        url='https://github.com/nabinkhadka/rotate-proxies',
        packages=['rotate_proxies'],
        setup_requires=['wheel']
        )
