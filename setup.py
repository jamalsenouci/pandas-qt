
from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import codecs
import os
import re
import sys

# TODO: sip is only needed for PyQt4, they should be imported together.
try:
    import sip
except ImportError:
    print("install sip first")

try:
    import PyQt4
except ImportError:
    # TODO: try to import PySide.
    print("install PyQt4 or PySide")


here = os.path.abspath(os.path.dirname(__file__))

version_file = open(os.path.join(here, 'pandasqt', '__init__.py'), 'rU')
__version__ = re.sub(
    r".*\b__version__\s+=\s+'([^']+)'.*",
    r'\1',
    [ line.strip() for line in version_file if '__version__' in line ].pop(0)
)
version_file.close()

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README')

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

tests_require = ['pandas >= 0.15.2', 'pyside', 'pytest', 'pytest-cov', 'pytest-qt']
setup(
    name='pandas-qt',
    version=__version__,
    url='https://github.com/datalyze-solutions/pandas-qt',
    license='MIT License',
    namespace_packages = ['pandasqt'],
    author='Matthias Ludwig',
    tests_require=tests_require,
    install_requires=['pandas>=0.15.1', 'chardet', 'pytest', 'pytest-qt==1.2.2', 'pytest-cov'],
    cmdclass={'test': PyTest},
    author_email='m.Ludwig@datalyze-solutions.com',
    description='catches exceptions inside qt applications and writes them to a message box and into a log file',
    long_description=long_description,
    packages=['pandasqt'],
    include_package_data=True,
    platforms='any',
    test_suite='tests',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: German',
        'Environment :: X11 Applications :: Qt',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: User Interfaces'
        ],
    extras_require={
        'testing': tests_require,
    }
)
