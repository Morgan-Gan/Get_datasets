import os
from PIL import Image
import time

import numpy as np
from concurrent.futures import ThreadPoolExecutor

fromDir = '/home/window_share/home/os/window_share/ganhaiyang/datasets/head_hand_foot/20210314datasets5000/new_imgs'

count = 0
small_count = 0
threadPool = ThreadPoolExecutor(max_workers=10)
min_size = 80                                                             # 100

def rmImage(file):
    os.remove(file)

#递归删除某个目录下宽度小于min_size的图片

def getImageList(dir):
    if os.path.isfile(dir) and dir.endswith('.jpg'):
        start=time.time()
        splits = dir.split('/')
        fileName = splits[len(splits)-1].split('.')[0]
        img = Image.open(dir)
        width = img.size[0]
        height = img.size[1]

        global count, small_count
        print(count,small_count, dir,width)
        count=count+1
        if width < min_size or height <min_size:
           small_count=small_count+1
           threadPool.submit(rmImage,dir)
           end=time.time()
           print("rm {} {} {} {}, tk time {:} ms".format(dir,width,height,count,int((end-start)*1000)))
    elif os.path.isdir(dir):
        for childfile in os.listdir(dir):
            getImageList(os.path.join(dir,childfile))

getImageList(fromDir)











