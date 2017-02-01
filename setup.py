#!/usr/bin/env python
"""
sentry-twilio
=============
Sentry Notification plugin for Twilio Programmable SMS.
:copyright: 2017 Luis Nell.
:license: MIT, see LICENSE for more details.
"""
from __future__ import absolute_import

from setuptools import setup, find_packages


VERSION = '1.0'

install_requires = [
    'twilio==6.0.0rc10',
]


setup(
    name='sentry-twilio',
    version=VERSION,
    author='Luis Nell',
    author_email='luis.nell@simpleloop.com',
    url='https://github.com/originell/sentry-twilio',
    description='Sentry Notification plugin for Twilio Programmable SMS.',
    long_description=__doc__,
    license='MIT',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    zip_safe=False,
    install_requires=install_requires,
    include_package_data=True,
    entry_points={
        'sentry.apps': [
            'twilio = sentry_twilio',
        ],
        'sentry.plugins': [
            'twilio = sentry_twilio.plugin:TwilioPlugin',
        ],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
