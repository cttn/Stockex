from distutils.core import setup
import codecs
try:
    codecs.lookup('mbcs')
except LookupError:
    ascii = codecs.lookup('ascii')
    func = lambda name, enc = ascii: {True: enc}.get(name == 'mbcs')
    codecs.register(func)


with open('README.txt') as file:
        long_description = file.read()

__author__ = 'Stockex'
__version__ = '0.1.3'
__email__ = 'cj.cttn@gmail.com'

setup(
    name=__author__,
    version=__version__,
    description='Python 3 wrapper for Yahoo! Finance API',
    author='Cttn',
    author_email=__email__,
    url='https://github.com/cttn/Stockex',
    packages=['stockex', ],
    license='Public Domain',
    classifiers = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Development Status :: 5 - Production/Stable',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Environment :: Console',
        'Intended Audience :: Developers',
    ],
    platforms=['Any']
)
