#!/usr/bin/env python

try:
    from setuptools.core import setup
except ImportError:
    from distutils.core import setup

setup(name='naive-bayes-classifier',
      version='0.1',
      license='MIT',
      description='yet another general purpose naive bayesian classifier',
      long_description=open('README.md').read(),
      author='Mustafa Atik',
      author_email='<muatik@gmail.com>',
      maintainer='Nejdet Yucesoy',
      maintainer_email='<nejdetyucesoy@gmail.com>',
      packages=['nbc'],
      platforms='any')