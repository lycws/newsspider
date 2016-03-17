#coding:utf-8
from spidertencent import url_manager, html_downloader, html_outputer, html_parser
import threading
import queue
import time

num = 4 #创建子进程数
sum = 1000 #要爬取的url数量

class ThreadClass(threading.Thread):
    def __init__(self, sp, type, root_url):
        threading.Thread.__init__(self)
        self.urls = url_manager.UrlManager()
        self.downloader = sp.downloader
        self.parser = sp.parser
        self.outputer = sp.outputer
        self.count = sp.count
        self.type = type
        self.root_url = root_url

    def run(self):
        count = self.count
        self.urls.add_new_url(self.root_url)
        while True:
            if self.urls.nohas_new_url():
                continue
            try:
                new_url = self.urls.get_new_url()
                print("%s" % new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont, self.type)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data, self.type)

                time.sleep(2)

                if self.urls.old_url_num() > sum:
                    break
                # if count == sum:
                #     self.urls.que.task_done()
                #     break
                # count = count + 1
            except:
                print('craw failed')
            self.urls.que.task_done()

class SpiderMain(object):
    def __init__(self):
       # self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        self.count = 1

    def craw(self, root_url):
       # self.urls.add_new_url(root_url)
        #生成一个线程池
        threads = []
        for i in range(num):
            t = ThreadClass(self, i, root_url[i])
            threads.append(t)
            #主程序退出时，子线程也立即退出
            t.setDaemon(True)
            #启动线程
            t.start()
        for t in threads:
            t.join()
        #self.urls.que.join()
        # self.outputer.output_html()

if __name__ == "__main__":
    root_url={}
    #新闻
    root_url[0] = "http://news.qq.com/"
    #财经
    root_url[1] = "http://finance.qq.com/"
    #体育
    root_url[2] = "http://sports.qq.com/"
    #娱乐
    root_url[3] = "http://ent.qq.com/"

    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
