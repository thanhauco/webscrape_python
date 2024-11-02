from setuptools import setup, find_packages

setup(
    name="ScrapeFlow",
    version="1.0.0",
    install_requires=[
        'pytest',
        'selectolax~=0.3.16',
        'aiohttp~=3.8.4',
        'playwright~=1.37.0',
        'setuptools~=63.2.0',
        'aiofiles~=23.2.1',
        'EVNTDispatch~=0.0.2',
        'requests~=2.28.2',
    ],
    packages=find_packages()
)
