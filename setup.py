import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = '0.2.2'

if sys.argv[-1] == 'tag':
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

setup(
    name='django-filepicker',
    version=version,
    description='Official Filepicker Django Library',
    author='Filepicker.io',
    author_email='contact@filepicker.io',
    url='http://developers.filepicker.io/',
    packages=['django_filepicker'],
    install_requires=['django >= 1.3','requests'],
    license="MIT",
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ]
)