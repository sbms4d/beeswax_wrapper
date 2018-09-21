from setuptools import setup, find_packages

from test import PyTest
from version import __version__

setup(
    name='beeswax_wrapper',
    version=__version__,
    description='Python2 Wrapper for the Beeswax API',
    author='iotec',
    author_email='dev@dsp.io',
    url='https://github.com/iotgdev/beeswax_wrapper/',
    download_url='https://github.com/iotgdev/beeswax_wrapper/archive/{}.tar.gz'.format(__version__),
    packages=find_packages(include=['beeswax_wrapper', 'beeswax_wrapper.*']),
    data_files=[],
    test_suite='test',
    setup_requires=['pytest-runner'],
    tests_require=['mock>=2.0.0', 'pytest'],
    cmdclass={'pytest': PyTest},
    scripts=['beeswax_wrapper/credentials/beeswax_credentials'],
    include_package_data=True,
    install_requires=[
        'keyrings.alt>=3.1',
        'keyring>=8.2.1',
        'requests>=2.19.1',
        'boltons>=18.0.0; python_version<"3.0"',
        'ujson>=1.35',
        'six>=1.11.0'
    ]
)
