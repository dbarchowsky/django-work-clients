import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

from work_clients import __author__, __version__

setup(
    name = 'django-work-clients',
    version = __version__,
    packages = ['work_clients'],
    include_package_data = True,
    license = 'MIT License',
    description = 'A Django app to manage work clients data.',
    long_description = README,
    url = 'https://github.com/dbarchowsky/django-work-clients',
    author = __author__,
    author_email = 'dbarchowsky@gmail.com',
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
    install_requires = [
        "django>=1.8",
        ],
    )