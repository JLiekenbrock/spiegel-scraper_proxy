from pathlib import Path
from setuptools import setup, find_packages

# The directory containing this file
here = Path(__file__).parent

# The text of the README file
readme = (here / 'README.md').read_text()

# This call to setup() does all the work
setup(
    name='spiegel-scraper_proxy',
    version='1.1.1',
    description='Scrape article metadata and comments from DER SPIEGEL',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/ietz/spiegel-scraper_proxy',
    author='Tim Pietz',
    author_email='tim@pietz.me',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'cssselect',
        'dateparser',
        'lxml',
        'requests',
        'tldextract',
    ],
)
