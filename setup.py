#!/usr/bin/env python

from setuptools import setup

setup(name='pyjolokia',
      version = '0.2.0',
      description='Pure Python based Jolokia client',
      author='Colin Wood',
      license="Apache License Version 2.0",
      author_email='cwood06@gmail.com',
      py_modules=['pyjolokia'],
      url='https://github.com/cwood/pyjolokia',
      download_url='http://github.com/cwood/sshed/tarball/master',
      long_description=open('README.rst').read(),
      include_package_data=True,
      keywords=['jolokia', 'jmx'],
      use_2to3=True
 )
