#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
    :copyright: (c) 2016 by Stellar Lee.
    :https://github.com/xx-li/HostsUpdate.git
    :http://devlxx.com
"""

# 使用方法：在终端定位到当前文件所在目录，执行 python HostsUpdate.py ，然后输入当前用户密码获取root权限更新hosts


import urllib2
import os
import sys
import platform

print 'start update hosts'

# 提升到root权限
if os.geteuid():
    args = [sys.executable] + sys.argv
    os.execlp('sudo', 'sudo', *args)

# 从此处开始是正常的程序逻辑
print('Running at root privilege. Your euid is', os.geteuid())

#hosts下载地址
url = 'https://raw.githubusercontent.com/racaljk/hosts/master/hosts'

# 不同的系统写入不同的目录
s = platform.system()
path = ''
if s == 'Darwin':
	path = '/private/etc/hosts'
elif s == 'Windows':
	path = 'C:\Windows\System32\drivers\etc\hosts'
elif s == 'Linux':
	path = '/etc/hosts'

print path

f = urllib2.urlopen(url) 
data = f.read()
fh = open(path, 'w') 
fh.write(data)
# 需要加入自定义的hosts，可以在这里编辑
# fh.write('test1\ntest2')
fh.close() 

print 'update hosts success'

