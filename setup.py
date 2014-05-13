#!/usr/bin/env python

try:
    from setuptools.core import setup
except ImportError:
    from distutils.core import setup


setup(name='naiveBayesClassifier',
      version='0.1.3.1',
      license='MIT',
      description='yet another general purpose naive bayesian classifier',
      long_description=open('README.md').read(),
      url='https://github.com/muatik/naive-bayes-classifier',
      author='Mustafa Atik',
      author_email='muatik@gmail.com',
      maintainer='Nejdet Yucesoy',
      maintainer_email='nejdetyucesoy@gmail.com',
      packages=['naiveBayesClassifier'],
      platforms='any')