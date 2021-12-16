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
font_number = ImageFont.truetype("/home/os/window_share/ganhaiyang/software/fonts/ArialNarrow/arialnarrow.ttf", 118)
font_english = ImageFont.truetype("/home/os/window_share/ganhaiyang/software/fonts/DIN1451EF-EngNeu/DIN1451EF-EngNeu.otf", 118)


#打开图片
imageFile = "./images/104844_128.jpg"
string_english = "ABCDEFGGHIJKLMNOPQRSTUVWXYABCDEFGGHIJKLMNOPQRSTUVWXY"
string_number =list("012345678901234566789") 
string_sum = list("ABCDEFGGHIJKLMNOPQRSTUVWXYABCDEFGGHIJKLMNOPQRSTUVWXY012345678901234566789")

english_list = list(string_english)
num = 4
choice_str = random.sample(english_list, num)
choice_num = random.sample(string_number, 6)
string_sum = random.sample(string_sum, num)

im1 = Image.open(imageFile)
start_point = random.randint(12, 20)


#画图
draw = ImageDraw.Draw(im1)
# draw.text((100,160), "79546123", (207, 230, 236), font=font_number)    #设置文字位置/内容/颜色/字体
# draw.text((650,170), "Z", (207, 230, 236), font=font_english)    #设置文字位置/内容/颜色/字体SZUCG
for i in range(len(choice_str)): 
    font = font_number if choice_str[i] in string_number   else font_english        
    draw.text((640,170 + i*85), choice_str[i], (207, 230, 236), font=font)    #设置文字位置/内容/颜色/字体SZUCG

    if i == 3:
        for j in range(len(choice_num)): 
            font = font_number  # if choice_str[i] in string_number   else font_english        
            draw.text((640,170 + i*85 + 120 + j*85), choice_num[j], (207, 230, 236), font=font)    #设置文字位置/内容/颜色/字体SZUCG
        draw.text((640,170 + i*85 + 230 + j*85), random.sample(string_number, 1)[0], (207, 230, 236), font=font)    #设置文字位置/内容/颜色/字体SZUCG

for i in range(len(choice_str)): 
    font = font_number if choice_str[i] in string_number   else font_english        
    draw.text((850,170 + i*85), choice_str[i], (207, 230, 236), font=font)    #设置文字位置/内容/颜色/字体SZUCG


draw = ImageDraw.Draw(im1)                          #Just draw it!

#另存图片
im1.save("target.jpg")
img = cv2.imread("target.jpg")
cv2.rectangle(img,(640+60, 1065+105),(640, 1075),(207, 230, 236),3)
im1 = cv2.imwrite("target.jpg", img)

h,w = img.shape[:2]


# cv2.imwrite('target1.jpg',dst)
# cv2.imshow("dst", dst)
# cv2.waitKey(0)

from PIL import Image
im1 = Image.open("target.jpg")

# Rotate it by 45 degrees
rotated     = im1.rotate(3)
rotated.save("rotated.jpg")
rotated.show()


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