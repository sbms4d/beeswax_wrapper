from setuptools import setup, find_packages

setup(
    name='beeswax_wrapper',
    version='1.0.0',
    description='Python2 Wrapper for the Beeswax API',
    author='iotec',
    author_email='dev@dsp.io',
    url='https://github.com/iotgdev/beeswax_wrapper/',
    download_url='https://github.com/iotgdev/beeswax_wrapper/archive/1.0.0.tar.gz',
    packages=find_packages(include=['beeswax_wrapper', 'beeswax_wrapper.*']),
    data_files=[],
    include_package_data=True,
    install_requires=[
        'keyrings.alt>=3.1',
        'keyring>=13.2.1',
        'requests>=2.19.1',
        'boltons>=18.0.0',
        'ujson>=1.35',
    ]
)
