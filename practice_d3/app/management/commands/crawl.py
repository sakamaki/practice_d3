# coding=utf-8

import logging
from datetime import datetime, timedelta

import pytz
from django.core.management.base import BaseCommand

import requests
from bs4 import BeautifulSoup
from practice_d3.app.models import Hotentry

URL = 'http://b.hatena.ne.jp/hotentry/{YYYYmmdd}'
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

jst = pytz.timezone('Asia/Tokyo')


class Command(BaseCommand):
    help = '''Crawling'''
    soup = None

    def add_arguments(self, parser):
        # optional arguments
        parser.add_argument(
            '--date', '-d',
            help="Specific crawl date")

    @staticmethod
    def get_user_count(content):
        return content.find('span').text

    @staticmethod
    def get_title_and_link(content):
        link = content.find('a', 'entry-link')
        return link.get('title'), link.get('href')

    @staticmethod
    def get_description(content):
        return content.find('li', 'description')

    @staticmethod
    def get_entry_date(content):
        text = content.find('li', 'date').text
        return datetime.strptime(text, '%Y/%m/%d %H:%M').replace(tzinfo=jst)

    @staticmethod
    def get_category(content):
        if content.find('a', 'category') is None:
            return u'カテゴリ不明'
        return content.find('a', 'category').text

    def handle(self, *args, **options):
        d = options.get('date')
        if d is None:
            tmp = datetime.now() - timedelta(1)
            d = tmp.strftime('%Y%m%d')
        res = requests.get(URL.format(YYYYmmdd=d))
        self.soup = BeautifulSoup(res.text, 'html.parser')

        for content in self.soup.find_all('li', 'entry-unit'):
            rank = content.get('data-entryrank')
            if rank is None:
                continue

            title, link = self.get_title_and_link(content)
            Hotentry.objects.get_or_create(
                bookmark_title=title,
                link=link,
                rank=rank,
                entry_date=self.get_entry_date(content),
                bookmark_user_count=self.get_user_count(content),
                description=str(self.get_description(content)),
                category=self.get_category(content),
            )
            # print hotentry.bookmark_user_count
            # print hotentry.bookmark_title
            # print hotentry.link
            # print hotentry.description
            # print hotentry.entry_date

