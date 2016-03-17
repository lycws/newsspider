#coding:utf-8
import urllib.request

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        headers = {
            'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
        }

        i_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'}

        req = urllib.request.Request(url, headers=i_headers)

        response = urllib.request.urlopen(req)

        if response.getcode() != 200:
            return None

        return response.read()
