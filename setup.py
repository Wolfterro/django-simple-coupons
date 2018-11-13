import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-simple-coupons',
    version='0.5',
    packages=['django_simple_coupons'],
    include_package_data=True,
    license='MIT License',
    description='A Django app that makes the use of coupons a simple task!',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/Wolfterro/django-simple-coupons',
    author='Wolfgang Almeida',
    author_email='wolfgang.almeida@yahoo.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
    ]
)