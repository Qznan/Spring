#! /usr/bin/env python
# -*- coding: utf-8 -*-
:utf-8 -*-
from threading import Thread
import subprocess
from Queue import Queue
num_threads = 3
ips = ['10.108.100.174', '119.75.218.77', '127.0.0.1']
q = Queue()
def pingit(i, queue):
    while True:
        ip = queue.get()
        print "thread %s is pinging %s" % (i, ip)
        ret = subprocess.call('ping -c 3 %s' % ip, shell=True, stdout=open('/dev/null','w'))#正常则返回0，异常则返回1；stdout=open('/dev/null','w')屏蔽ping具体细节信息
        if ret != 0:
            print "%s is down" % ip
        queue.task_done()
for i in xrange(num_threads):#xrang比range好
    t = Thread(target=pingit, args=(i, q))
    t.setDaemon(True)#设置了setDaemon则线程会随着主线程关闭而关闭，python中，主线程结束后，会默认等待子线程结束后，主线程才退出
    t.start()
for ip in ips:
    q.put(ip)
print "main thread is waiting..."
q.join()
print "Done..."