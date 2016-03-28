# -*- coding: utf-8 -*-
import time
import redis
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TutorialPipeline(object):

    def __init__(self):
        self.r = redis.Redis(host='localhost', port=6379, db=1)

    def process_item(self, item, spider):

        #print item['title'], item['content'], item['time']
        r = self.r
        name = item['type']

        pipe = r.pipeline()
        while 1:
            try:
                pipe.watch(name)

                id = r.get(name+"_num")
                t = time.strptime(item['time'], "%Y-%m-%d %H:%M:%S")
                s = int(time.mktime(t))

                if id is None:
                    id = 1
                else:
                    id = int(id.decode('utf-8')) + 1

                if not r.sismember(name+"set", item['title']):
                    r.zadd(name+"zset", id, s)
                    r.set(name+"_num", id)
                    r.sadd(name + "set", item['title'])
                    r.hset(name + ':' + str(id), 'id', id)
                    r.hset(name + ':' + str(id), 'title', item['title'])
                    r.hset(name + ':' + str(id), 'content', item['content'])
                    r.hset(name + ':' + str(id), 'time', item['time'])
                    if item['showimg']:
                        r.hset(name + ':' + str(id), 'showimg', item['showimg'])
                    else:
                        r.hset(name + ':' + str(id), 'showimg', '')
                    r.hset(name + ':' + str(id), 'source', item['src'])
                    r.hset(name + ':' + str(id), 'click', 0)

                pipe.execute()
                break
            except:
                continue
            finally:
                pipe.reset()

        return item
