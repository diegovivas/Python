#!/usr/bin/env python3
import argparse
import logging
logging.basicConfig(level=logging.INFO)

import news_page_objects as news
from  common import config


logger = logging.getLogger(__name__)


def _news_scraper(news_site_uid):
    host = config()['news_sites'][news_site_uid]['url']

    logging.info('Beginning scraper for {}'.format(host))
    homepage = news.HomePage(news_site_uid, host)

    for link in homepage.article_links:
        print(link)
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    news_site_choices = list(config()['news_sites'].keys())
    parser.add_argument('news_site',
                        help='The news site that you whant to scrape',
                        type=str,
                        choices=news_site_choices)
    args = parser.parse_args()
    print(args.news_site)
    _news_scraper(args.news_site)
