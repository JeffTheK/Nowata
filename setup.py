from setuptools import setup

setup(
    name='nowata',
    version='1.0.0',
    entry_points={
        'console_scripts': [
            'nowata=nowata.interpreter:run'
        ]
    }
)