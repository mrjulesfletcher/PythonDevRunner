
from setuptools import setup, find_packages

setup(
    name='PythonDevRunner',
    version='0.1.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'devrunner = dev_runner.cli:main',
        ],
    },
    install_requires=[
        'watchdog',
    ],
    author='Jules Le Masson',
    description='A Python auto-reloading development runner',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    python_requires='>=3.7',
)
