from setuptools import setup, find_packages

VERSION = '1.1.0'

setup(
    name='beeswax_wrapper',
    version=VERSION,
    description='Python2 Wrapper for the Beeswax API',
    author='iotec',
    author_email='dev@dsp.io',
    url='https://github.com/iotgdev/beeswax_wrapper/',
    download_url='https://github.com/iotgdev/beeswax_wrapper/archive/{}.tar.gz'.format(VERSION),
    packages=find_packages(include=['beeswax_wrapper', 'beeswax_wrapper.*']),
    data_files=[],
    scripts=['beeswax_wrapper/credentials/beeswax_credentials'],
    include_package_data=True,
    install_requires=[
        'keyrings.alt>=3.1',
        'keyring>=8.2.1',
        'requests>=2.19.1',
        'boltons>=18.0.0',
        'ujson>=1.35',
        'six>=1.11.0',
    ]
)
