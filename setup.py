#!/usr/bin/env python

from setuptools import setup

setup(name='pyjolokia',
      version = '0.2.0',
      description='Pure Python based Jolokia client',
      author='Colin Wood',
      license="Apache License Version 2.0",
      platform='any',
      author_email='cwood06@gmail.com',
      py_modules=['pyjolokia'],
      url='https://github.com/cwood/pyjolokia',
      long_description=read('README.rst'),
      include_package_data=True,
 )
