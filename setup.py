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

setup(
    name='Stockex',
    version='0.1.2',
    description='Python 3 wrapper for Yahoo! Finance API',
    author='Cttn',
    author_email='cj.cttn@gmail.com',
    url='https://github.com/cttn/Stockex',
    packages=['stockex', ],
    license='Public Domain'
    )
