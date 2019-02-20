#!/usr/bin/env python3
'''
python_package_template setup config
'''
import os
from setuptools import setup

here = os.path.dirname(__file__)

about = {}
with open(os.path.join(here, 'python_package_template', '__about__.py')) as fobj:
    exec(fobj.read(), about)

setup(
    name='python_package_template',
    version=about['__version__'],
    packages = [
        'python_package_template',
    ],
    install_requires = [
        'numpy',
        'requests',
    ],
    include_package_data = True,
    author               = about['__author__'],
    author_email         = about['__author_email__'],
    maintainer           = about['__author__'],
    maintainer_email     = about['__author_email__'],
    description          = about['__description__'],
    url                  = about['__url__']
)