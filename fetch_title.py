import time
from selenium import webdriver
import datetime
from datetime import date, datetime
import requests
import json
import os

import dropbox_api
import reload_cms

class Selenium:
    def __init__(self,url):
        self.url = url
    
    def fetch_title_selenium(self):
        driver.get(self.url)
        url_and_title[self.url] = driver.title

class Md_file:
    def __init__(self, title, date):
        self.title = title
        self.date = date

    def create_md_body(self):
        lists = []
        for url, value in url_and_title.items():
            md_list = f'- [{value}]({url})'
            lists.append(md_list)
        
        md_body = '\n'.join(lists)
        return md_body

    def create_md_description(self):
        container = []
        for value in url_and_title.values():
            container_list = f'- {value}'
            container.append(container_list)
        return container

def post_microcms(title, date, content, description):
    shorter_description = '\n'.join(description[:3])
    URL = os.environ['URL']
    headers = {
    'Content-Type': 'application/json',
    'X-WRITE-API-KEY': os.environ['X_WRITE_API_KEY'],
    }
    payload = {
        'title': title,
        'date': date,
        'content': content,
        'description': shorter_description
    }
    try:
        r = requests.post(URL, headers=headers, data=json.dumps(payload))
        post_message = f'post success. blogId:{r.text}'
        print(post_message)
    except Exception as e:
        error_message = 'error occur\n===========\n'\
            f'type:{type(e)}\nargs:{e.args}'
        print(error_message)

def main(title, date):
    urls = dropbox_api.download_file()

    for url in urls:
        try:
            Selenium(url).fetch_title_selenium()
        except Exception as e:
            error_message = 'error occur\n===========\n'\
                f'type:{type(e)}\nargs:{e.args}'
            print(error_message)

    body = Md_file(title, date).create_md_body()
    print('=====contents=====')
    print(body)
    description = Md_file(title, date).create_md_description()
    print('=====description=====')
    print('\n'.join(description[:3]))
    post_microcms(title, date, body, description)
    response = reload_cms.reload()
    print(response.status_code)

    driver.close()
if __name__ == '__main__':
    url_and_title = {}
    title = date.today().strftime('%Y-%m-%d')
    dt_now = datetime.now().isoformat()
    driver = webdriver.Chrome()
    # main(title, dt_now)