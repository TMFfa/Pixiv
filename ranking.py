import requests
import json
import datetime
import os
import re


def yesterday():
    today = datetime.date.today()
    one_day = datetime.timedelta(days=1)
    target_date = str(today-one_day)
    return target_date.replace('-', '')


def change(name):
    mode = re.compile(r'[\\/:*?"<>|]')
    new_name = re.sub(mode, '_', name)
    return new_name


def mkdir(options):
    if options == '日榜':
        try:
            os.mkdir(options)
        except Exception as e:
            print(e)
    elif options == '周榜':
        try:
            os.mkdir(options)
        except Exception as e:
            print(e)
    elif options == '月榜':
        try:
            os.mkdir(options)
        except Exception as e:
            print(e)


class Spider:
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/89.0.4389.128 Safari/537.36 Edg/89.0.774.77'
    }

    def __init__(self, headers):
        self.headers = headers

    def daily_urls(self):
        page = 0
        daily_urls = []
        while True:
            date = yesterday()
            url = 'https://www.vilipix.com/api/illust?mode=daily&date={date}&limit=30&offset={p}' \
                .format(date=date, p=str(page * 30))
            r = requests.get(url, headers=self.headers)
            js = json.loads(r.text)
            if not js['rows']:
                return daily_urls
            else:
                daily_urls.append(url)
                page += 1

    def weekly_urls(self):
        page = 0
        weekly_urls = []
        while True:
            date = yesterday()
            url = 'https://www.vilipix.com/api/illust?mode=weekly&date={date}&limit=30&offset={p}' \
                .format(date=date, p=str(page * 30))
            r = requests.get(url, headers=self.headers)
            js = json.loads(r.text)
            if not js['rows']:
                return weekly_urls
            else:
                weekly_urls.append(url)
                page += 1

    def monthly_urls(self):
        page = 0
        monthly_urls = []
        while True:
            date = yesterday()
            url = 'https://www.vilipix.com/api/illust?mode=monthly&date={date}&limit=30&offset={p}' \
                .format(date=date, p=str(page * 30))
            r = requests.get(url, headers=self.headers)
            js = json.loads(r.text)
            if not js['rows']:
                return monthly_urls
            else:
                monthly_urls.append(url)
                page += 1
