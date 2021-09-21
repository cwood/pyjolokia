from setuptools import setup, Command


class PyTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys
        import subprocess
        errno = subprocess.call([sys.executable,
                                 'runtests.py',
                                 'tests.py'])
        raise SystemExit(errno)

setup(name='pyjolokia',
      version='0.3.2',
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
      cmdclass={'test': PyTest},
      classifiers=[
          'Development Status :: 4 - Beta'
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Topic :: Software Development :: Libraries :: Java Libraries',
      ],
)
