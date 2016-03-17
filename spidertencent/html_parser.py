#coding:utf-8

import re
import urllib.parse
from bs4 import BeautifulSoup
import time

class HtmlParser(object):

    def _get_new_urls(self, page_url, soup, type):
        new_urls = set()

        #http://news.qq.com/a/20160314/018566.htm
        if type == 0:
            links = soup.find_all('a', href=re.compile(r"http://news\.qq\.com/.+"))
        elif type == 1:
            links = soup.find_all('a', href=re.compile(r"http://finance\.qq\.com/.+"))
        elif type == 2:
            links = soup.find_all('a', href=re.compile(r"http://sports\.qq\.com/.+"))
        elif type == 3:
            links = soup.find_all('a', href=re.compile(r"http://ent\.qq\.com/.+"))
        else:
            links = []

        for link in links:
            new_url = link['href']
            #pattern = re.compile(r"http://news\.qq\.com/.+")
            #new_url = pattern.match(new_url).group()
            #new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_full_url = new_url
            new_urls.add(new_full_url)
        return  new_urls

    def _get_new_data(self, page_url, soup, type):
        res_data = {}

        if type == 0:
            pattern = re.compile(r"http://news\.qq\.com/a/\d+/\d+\.htm")
        elif type == 1:
            pattern = re.compile(r"http://finance\.qq\.com/a/\d+/\d+\.htm")
        elif type == 2:
            pattern = re.compile(r"http://sports\.qq\.com/a/\d+/\d+\.htm")
        elif type == 3:
            pattern = re.compile(r"http://ent\.qq\.com/a/\d+/\d+\.htm")
        else:
            pattern = None

        if re.match(pattern, page_url):
            #url
            res_data['url'] = page_url
            title = soup.find('div', class_='hd')
            title = title.contents[1].get_text()
            print(title)
            res_data['title'] = title

            time = soup.find('span', class_='article-time').get_text()
            #print(time.get_text())
            res_data['time'] = time

            #<div id="Cnt-Main-Article-QQ" bosszone="content">
            content = soup.find('div', id='Cnt-Main-Article-QQ').get_text()
            #print(content.get_text())
            res_data['content'] = content

            #res_data["creatime"] = time.time()

        return res_data

    def parse(self, page_url, html_cont, type):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='GB18030')
        new_urls = self._get_new_urls(page_url, soup, type)
        new_data = self._get_new_data(page_url, soup, type)
        return new_urls, new_data