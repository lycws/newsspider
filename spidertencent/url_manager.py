#coding:utf-8

import queue

class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
        self.que = queue.Queue()

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
            self.que.put(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return self.que.empty() != True

    def nohas_new_url(self):
        return self.que.empty()

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        new_urlt = self.que.get()
        return new_url

    def old_url_num(self):
        return len(self.old_urls)