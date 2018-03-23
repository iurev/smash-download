import sys
import datetime
import re
import requests
from bs4 import BeautifulSoup
import mimetypes
import os

now = datetime.datetime.now()

default_settings = {
    'year': now.year,
    'month': now.month,
    'size': '2560x1440',
    'calendar': True
}
months_names = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
base_url = 'https://www.smashingmagazine.com'
image_base_url = 'http://files.smashingmagazine.com/wallpapers'

def get_month_page_url(year, month):
    posted_year = year
    posted_month = month
    if month == 1:
        posted_year = posted_year - 1
        posted_month = 12
    else:
        posted_month = posted_month - 1
    return '{0}/{1}/{2:02d}/desktop-wallpaper-calendars-{3}-{4}'.format(
        base_url,
        posted_year,
        posted_month,
        months_names[month - 1],
        year
    )

def get_year(args = []):
    p = re.compile(r'^\d{4}$')
    for a in args:
        if isinstance(a, str) and p.match(a):
            return int(a)

    return default_settings['year']

def get_month(args = []):
    p = re.compile(r'^\d{1,2}$')
    for a in args:
        if isinstance(a, str) and p.match(a):
            return int(a)

    return default_settings['month']

def get_size(args = []):
    p = re.compile(r'^\d{3,4}x\d{3,4}$')
    for a in args:
        if isinstance(a, str) and p.match(a):
            return a

    return default_settings['size']

def get_calendar(args = []):
    p = re.compile(r'^\d{3,4}x\d{3,4}$')
    for a in args:
        if a == 'no-calendar':
            return False
    return default_settings['calendar']

def get_settings(args):
    settings = {}
    settings['year'] = get_year(args)
    settings['month'] = get_month(args)
    settings['size'] = get_size(args)
    settings['calendar'] = get_calendar(args)
    return settings

def get_page(url):
    return requests.get(url).text

def get_images_urls(page, calendar, size):
    soup = BeautifulSoup(page, 'html.parser')
    urls = []
    for ul in soup.find('div', {'class': 'c-garfield-the-cat'}).find_all('ul'):
        lis = ul.find_all('li')
        li = lis[1] if calendar else lis[2]
        for a in li.find_all('a'):
            url = a.get('href')
            if size in url:
                urls.append(url) 
    return urls

def save_image(url, year, month, index):
    res = requests.get(url)
    content_type = res.headers['content-type']
    ext = mimetypes.guess_extension(content_type)
    data = res.content
    path = './output/{year}-{month:02d}-{index}{ext}'.format(
        index=index,
        year=year,
        month=month,
        ext=ext
    )
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'wb') as handler:
        handler.write(data)

def main():
    settings = get_settings(sys.argv[1:])
    url = get_month_page_url(settings['year'], settings['month'])
    page = get_page(url)
    urls = get_images_urls(page, settings['calendar'], settings['size'])
    for i, img_url in enumerate(urls[0:3]):
        save_image(img_url, settings['year'], settings['month'], i)

if __name__ == '__main__':
    main()
