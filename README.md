# spiegel-scraper_proxy
[![PyPI](https://img.shields.io/pypi/v/spiegel-scraper)](https://pypi.org/project/spiegel-scraper/)

Scrape articles and comments from DER SPIEGEL using a proxy-server. Probably still needs sessions.

## Setup
```bash
pip install spiegel-scraper_proxy
```

## Usage
```python
from datetime import date
import scraper-scraper_proxy as spon

from fp.fp import FreeProxy

proxy = FreeProxy(country_id=['DE'],timeout=.5).get()
proxie = proxy.split("://",1)
proxie = {proxie[0]:proxie[1]}

# list all articles from 2020-01-31
archive_entries = spon.archive.by_date(date(2020, 1, 31),proxie)
# or, for later replication, retrieve and scrape the html instead
archive_html = spon.archive.html_by_date(date(2020, 1, 31),proxie)
archive_entries_from_html = spon.archive.scrape_html(archive_html)

# fetch one article by url
article_url = archive_entries[0]['url']
article = spon.article.by_url(article_url,proxie)
# or alternatively using the html
article_html = spon.article.html_by_url(article_url,proxie)
article_from_html = spon.article.scrape_html(article_html)

# retrieve all comments for an article
comments = spon.comments.by_article_id(article['id'])
```
