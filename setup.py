#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['requests','matplotlib','pandas']

test_requirements = ['pytest>=3', ]

setup(
    author="Balveer Singh",
    author_email='balveer@geoiq.io',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Get started with a wide range of location-based features and build ml models using this package.",
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='geoiq_automl',
    name='geoiq_automl',
    packages=find_packages(include=['geoiq_automl', 'geoiq_automl.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/geoiq-io/geoiq_automl',
    version='0.1.0',
    zip_safe=False,
)
