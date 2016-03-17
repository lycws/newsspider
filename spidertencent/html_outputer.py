#coding:utf-8

import redis

class HtmlOutputer(object):

    def __init__(self):
        self.datas = []
        self.r = redis.Redis(host='localhost', port=6379, db=1)

    def collect_data(self, data, type):
        if not data:
            return
        #self.datas.append(data)
        r = self.r

        if type == 0:
            name = "news"
            source = "腾讯新闻"
        elif type == 1:
            name = "finance"
            source = "腾讯财经"
        elif type == 2:
            name = "sports"
            source = "腾讯体育"
        elif type == 3:
            name = "ent"
            source = "腾讯娱乐"
        else:
            name = ""

        pipe = r.pipeline()
        while 1:
            try:
                pipe.watch(name)

                id = r.lrange(name, 0, 0)

                if id == []:
                    id = 1
                else:
                    id = int(id[0].decode('utf-8')) + 1

                if not r.sismember(name+"set", data['title']):
                    r.lpush(name, id)
                    r.sadd(name + "set", data['title'])
                    r.hset(name + ':' + str(id), 'id', id)
                    r.hset(name + ':' + str(id), 'title', data['title'])
                    r.hset(name + ':' + str(id), 'content', data['content'])
                    r.hset(name + ':' + str(id), 'time', data['time'])
                    r.hset(name + ':' + str(id), 'source', source)

                pipe.execute()
                break
            except:
                continue
            finally:
                pipe.reset()
