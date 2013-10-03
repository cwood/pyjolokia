from setuptools import setup, Command
import sys

kw = {}
if sys.version_info >= (3,):
        kw['use_2to3'] = True

class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        import sys,subprocess
        errno = subprocess.call([sys.executable,
                                 'runtests.py',
                                 'tests.py'])
        raise SystemExit(errno)

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
      cmdclass = {'test': PyTest},
      **kw
)
