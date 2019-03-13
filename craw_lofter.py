import os
import re
import requests
import time
from selenium import webdriver


url_all = []
pic_url_all = []

def get_guidang_page(page = 1):
    driver = webdriver.Chrome()
    driver.get('http://hatsunewaydy.lofter.com/?page=%d'% page)
    time.sleep(10)
    page1 = driver.page_source
    #print(page1)
    url_list = re.findall('class="postblk" href=\"(.*?)\"', page1, re.S)
    for url in url_list:
        if 'http' in url:
            #print(url)
            url_all.append(url)

    driver.close()

def get_pic_page(pic_in_url):
    r = requests.get(pic_in_url)
    pic_in_html = r.text.encode(r.encoding).decode()
    pic_list = re.findall('bigimgsrc=\"(.*?)\">', pic_in_html, re.S)
    for url in pic_list:
        if 'http' in url:
            #print(url)
            pic_url_all.append(url)


def pic_download(pic_url_all):
    for pic_url in pic_url_all:
        r = requests.get(pic_url)
        name = (pic_url.split('/')[-1]).split('?')[0]
        #print(name)
        with open(name, 'wb') as pic:
            pic.write(r.content)


def main():
    get_guidang_page(1)
    for pic_in_url in url_all:
        get_pic_page(pic_in_url)
    os.chdir('F:\\python_pic_craw\\vocaloid')
    #print(pic_url_all)
    pic_download(pic_url_all)

if __name__ == '__main__':
    main()