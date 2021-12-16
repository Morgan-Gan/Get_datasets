#-*- coding:utf-8 -*-
import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
import random
import cv2
import numpy as np

os.environ['DISPLAY'] = 'localhost:20.0'


#打开图片
string_en = list("abcdefghijklmnopqrstuvwxyz")
string_number =list("012345678901234566789") 
english_EN = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
string_containers = ["22G1", "25G1", "42G1", "45G1", "MSDU", "ZCSU"]



# import matplotlib.pyplot as plt
labels_path = 'labels.txt'
img_num = 20000
gs = 0
if os.path.exists(labels_path):  # 支持中断程序后，在生成的图片基础上继续
    f = open(labels_path,'a',encoding='utf-8')
    print('start generating...')
    img_n=0
    for i in range(img_num):
        chars = ''
        img_n+=1
        print('img_n',img_n)
        # rnd = random.random()
        # if rnd<0.3: # 设定产生水平文本的概率 0.8
        fun_index = random.randint(0, 4)
        # 固定箱号规格
        if fun_index == 0:             
            index = random.randint(0, 5)
            chars = string_containers[index]
            print(index)

        elif fun_index == 1:       # 生成6个数字
            for i in range(6):
                current = random.randint(0, 9)
                chars += str(current)

        elif fun_index == 2:       # 生成随机字母加数字共6个
            for i in range(6):
                current = random.randrange(0, 6)
                if current == i:
                    tmp = chr(random.randint(65, 90))
                else:
                    tmp = random.randint(0, 9)
                chars += str(tmp)

        elif fun_index == 3:       # 生成随机字母共4个
            for i in range(4):
                current = random.randrange(0, 4)
                tmp = chr(random.randint(65, 90))
                chars += str(tmp)

        elif fun_index == 4:       # 生成随机数字共1个
            tmp = random.randint(0, 9)
            chars += str(tmp)

        print(chars)
        f.write(chars+'\n')
        # save_img_name = 'img_3_' + str(i).zfill(7) + '.jpg'
        # f.write(save_img_name+ ' '+chars+'\n')
        # print('gennerating:-------'+save_img_name)  
    f.close()


# for i in range(10):
#     image_path = "./images/cimc_containers_906"
#     save_path = "./images/save_img906"
#     os.makedirs(save_path, exist_ok=True)
#     for root, dirs, files in os.walk(image_path):
#         for j in range(len(files)):
        
#             print("---------i : --------------->{}".format(i))
#             im1 = Image.open(os.path.join(root, files[j]))

#             w, h = im1.width, im1.height

#             num = 4
#             choice_str = random.sample(english_list, num)
#             choice_num = random.sample(string_number, 6)
#             choice_sum_4 = random.sample(string_sum, num)
#             str_one = random.sample(string_number, 1)

#             start_point = random.randint(12, w)       # 640
#             print("---------start_point : --------------->{}".format(start_point))

#             # txt size
#             font_size = random.randint(100, 118)     # default font size is 118
#             print("---------font_size : --------------->{}".format(font_size))
#             save_img = save_path + "/20210906_" + str(i*46 + j) + ".jpg"













