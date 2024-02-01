import os
import codecs

from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = 'API Integration of the GameAds service'

here = os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='gameadsapi',
    version=VERSION,
    author='Anton',
    author_email='<api@gameads.pro>',
    description=DESCRIPTION,
    long_description_content_type='text/markdown',
    long_description=long_description,
    packages=find_packages(),
    install_requires=['aiohttp'],
    python_requires='>=3.7',
    keywords=['python', 'gameads', 'async', 'asyncio'],
    classifiers=[
        'Development Status :: 1 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: Unix',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
    ],
    url='https://github.com/BotAdsCod/gameads',
    project_urls={
        'Homepage': 'https://github.com/BotAdsCod/gameads',
        'Bug Tracker': 'https://github.com/BotAdsCod/gameads/issues',
    },
)
