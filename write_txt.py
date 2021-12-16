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
#设置所使用的字体
# font_number = ImageFont.truetype("/home/os/window_share/ganhaiyang/software/fonts/ArialNarrow/arialnarrow.ttf", 118)
# font_english = ImageFont.truetype("/home/os/window_share/ganhaiyang/software/fonts/DIN1451EF-EngNeu/DIN1451EF-EngNeu.otf", 118)


#打开图片
# image_path = "./images/augument"
string_english = "ABCDEFGGHIJKLMNOPQRSTUVWXYABCDEFGGHIJKLMNOPQRSTUVWXY"
string_number =list("012345678901234566789") 
string_sum = list("ABCDEFGGHIJKLMNOPQRSTUVWXYABCDEFGGHIJKLMNOPQRSTUVWXY012345678901234566789")
english_list = list(string_english)




#画图
def draw_txt(im1, start_point, font_size, save_img):
    draw = ImageDraw.Draw(im1)
    font_number = ImageFont.truetype("/home/os/window_share/ganhaiyang/software/fonts/ArialNarrow/arialnarrow.ttf", font_size - 1)
    font_english = ImageFont.truetype("/home/os/window_share/ganhaiyang/software/fonts/DIN1451EF-EngNeu/DIN1451EF-EngNeu.otf", font_size)

    for i in range(len(choice_str)): 
        font = font_number if choice_str[i] in string_number   else font_english        
        draw.text((start_point, 170 + i*85), choice_str[i], (207, 230, 236), font=font)    #设置文字位置/内容/颜色/字体SZUCG

        if i == 3:
            for j in range(len(choice_num)): 
                font = font_number  # if choice_str[i] in string_number   else font_english        
                draw.text((start_point, 170 + i*88 + 120 + j*88), choice_num[j], (207, 230, 236), font=font)    #设置文字位置/内容/颜色/字体SZUCG
            draw.text((start_point, 170 + i*87 + 230 + j*87), str_one[0], (207, 230, 236), font=font)    #设置文字位置/内容/颜色/字体SZUCG

    for i in range(len(choice_sum_4)): 
        font = font_number if choice_sum_4[i] in string_number   else font_english        
        draw.text((start_point + 210, 170 + i*88), choice_sum_4[i], (207, 230, 236), font=font)    #设置文字位置/内容/颜色/字体SZUCG

    draw = ImageDraw.Draw(im1)                          #Just draw it!

    #另存图片
    im1.save(save_img)
    img = cv2.imread(save_img)
    cv2.rectangle(img,(start_point+60, 1065+119),(start_point, 1075 + 10),(207, 230, 236),3)
    im1 = cv2.imwrite(save_img, img)

    im1 = Image.open(save_img)
    rotated_value = random.randint(0, 5)   # 之间的任意数，必须是整数
    rotated = im1.rotate(rotated_value)
    print("---------rotated_value : --------------->{}".format(rotated_value))
    rotated.save(save_img)
    # rotated.show()



for i in range(10):
    # imageFile = "./images/104844_104.jpg"
    # im1 = Image.open(imageFile)

    image_path = "./images/cimc_containers_906"
    save_path = "./images/save_img906"
    os.makedirs(save_path, exist_ok=True)
    for root, dirs, files in os.walk(image_path):
        for j in range(len(files)):
        
            print("---------i : --------------->{}".format(i))
            im1 = Image.open(os.path.join(root, files[j]))

            w, h = im1.width, im1.height

            num = 4
            choice_str = random.sample(english_list, num)
            choice_num = random.sample(string_number, 6)
            choice_sum_4 = random.sample(string_sum, num)
            str_one = random.sample(string_number, 1)

            start_point = random.randint(12, w)       # 640
            print("---------start_point : --------------->{}".format(start_point))

            # txt size
            font_size = random.randint(100, 118)     # default font size is 118
            print("---------font_size : --------------->{}".format(font_size))
            save_img = save_path + "/20210906_" + str(i*46 + j) + ".jpg"
            draw_txt(im1, start_point, font_size, save_img)

# #另存图片
# im1.save(save_img)
# img = cv2.imread("target.jpg")
# cv2.rectangle(img,(start_point+60, 1065+105),(start_point, 1075),(207, 230, 236),3)
# im1 = cv2.imwrite("target.jpg", img)

# h,w = img.shape[:2]


# cv2.imwrite('target1.jpg',dst)
# cv2.imshow("dst", dst)
# cv2.waitKey(0)

# im1 = Image.open("target.jpg")

# Rotate it by 45 degrees
# rotated_value = random.randint(0, 5)   # 之间的任意数，必须是整数
# rotated = im1.rotate(rotated_value)
# print("---------rotated_value : --------------->{}".format(rotated_value))

# rotated.save("rotated.jpg")
# rotated.show()


# # Rotate it by 90 degrees
# transposed  = im1.transpose(Image.ROTATE_90)
# transposed.show()















### ------- (1) 透视变换 ------------
# pts = np.float32([[0, 0], [0, 10], [10, 10], [10, 0]])         #np.float32([[100, 0], [0, 100], [100, 100], [200, 0]])
# pts1 = np.float32([[1, 0], [0, 10], [10, 10], [11, 0]])       # np.float32([[0, 0], [0, 100], [100, 100], [100, 0]])
# M = cv2.getPerspectiveTransform(pts,pts1)
# dst = cv2.warpPerspective(img,M,(h,w))      # M为变换矩阵，(h*2,w*2)输出图片大小， -----------》透射变换


### ------- (1) 仿射变换 ------------
# M1 = np.array([[np.cos(np.pi/8),np.sin(-np.pi/8),50],[np.sin(np.pi/8),np.cos(np.pi/8),30]]) #顺时针旋转45度，向左平移200，向下平移30
# dst = cv2.warpAffine(img,M1,(h,w))#把输出图像的大小改为输入图像的两倍  