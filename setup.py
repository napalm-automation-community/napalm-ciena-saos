"""setup.py file."""

from setuptools import setup, find_packages

__author__ = 'Maarten Wallraf <maarten@2nms.com>'

with open("requirements.txt", "r") as fs:
    reqs = [r for r in fs.read().splitlines() if (len(r) > 0 and not r.startswith("#"))]

setup(
    name="napalm-ciena-saos",
    version="0.1.0",
    packages=find_packages(),
    author="Maarten Wallraf",
    author_email="maarten@2nms.com",
    description="Network Automation and Programmability Abstraction Layer with Multivendor support: Ciena SAOS",
    classifiers=[
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
    ],
    url="https://github.com/napalm-automation-community/napalm-ciena-saos",
    include_package_data=True,
    install_requires=reqs,
)
