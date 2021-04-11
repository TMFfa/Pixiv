# 镜像地址：https://www.vilipix.com/ranking
import requests
import datetime
import json
import re
import os


def yesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = str(today-oneday)
    return yesterday.replace('-', '')


def change(name):
    mode = re.compile(r'[\\/:*?"<>|]')
    new_name = re.sub(mode, '_', name)
    return new_name


try:
    os.mkdir('日榜')
except Exception as e:
    print(e)


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68'
}


def download(url):
    resp = requests.get(url, headers=headers)
    all_data = json.loads(resp.text)['rows']
    for data in all_data:
        title = change(data['title']) + '.jpg'
        url = data['regular_url']
        print('saving:  ', title, url)
        try:
            r = requests.get(url, headers=headers, timeout=5)
            with open('./日榜/'+title, 'wb') as f:
                f.write(r.content)
        except Exception as eee:
            print(eee)


def geturls():
    page = 0
    urls = []
    while True:
        date = yesterday()
        url = 'https://www.vilipix.com/api/illust?mode=daily&date={date}&limit=30&offset={p}' \
            .format(date=date, p=str(page * 30))
        r = requests.get(url, headers=headers)
        if r.text == '{"count":54,"rows":[]}':
            return urls
        else:
            urls.append(url)
            page += 1


def main():
    start = datetime.datetime.now()
    for url in geturls():
        try:
            download(url)
        except Exception as ee:
            print(ee)
    end = datetime.datetime.now()
    print('totally used ', (end-start).seconds, ' seconds')


if __name__ == '__main__':
    main()
