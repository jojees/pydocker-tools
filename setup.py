from setuptools import setup, find_packages

setup(
    name='pydocker-tools',
    version='0.0.1',
    description='pydocker-tools is a set of tools to work around lengthy or piped command line tools for docker',
    licence='MIT',
    url='https://github.com/jojees/pydocker-tools',
    author='Joji Vithayathil Johny',
    author_email='joji@jojees.net',

    packages=find_packages(
        exclude=['tests']
    ),

    test_suite='tests',

    entry_points={
        'console_scripts': [
            'jpy-dtools = pydockertools.jpydtools:main'
        ]
    }
)
