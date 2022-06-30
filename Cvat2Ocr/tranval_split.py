import os
import shutil
import glob
from tkinter import N
import cv2






############################################### 21. dbnet标签按比例划分训练集合验证集  ####################################################################
train_txt = '/home/os/window_share/common3/dataset/ocr/cimc/20220619con_zhangzhou_side/20220505container_side_train.txt'
val_txt = '/home/os/window_share/common3/dataset/ocr/cimc/20220619con_zhangzhou_side/20220505container_side_val.txt'
dir_txt = '/home/os/window_share/common3/dataset/ocr/cimc/20220619con_zhangzhou_side/labels/annotations.txt'
img_dir = '/home/os/window_share/common3/dataset/ocr/cimc/20220619con_zhangzhou_side/Images/'
train_img = '/home/os/window_share/common3/dataset/ocr/cimc/20220619con_zhangzhou_side/images_train/'
os.makedirs(train_img, exist_ok=True)
val_img = '/home/os/window_share/common3/dataset/ocr/cimc/20220619con_zhangzhou_side/images_val/'
os.makedirs(val_img, exist_ok=True)


with open(dir_txt, "r") as f:
    with open(train_txt, "a") as tf:
        with open(val_txt, "a") as vf:
            if f.readlines():
                f.seek(0)
                all_data = f.read().split('\n')
                count = 0
                for line in all_data:
                    img_path = img_dir + line.split('\t')[0].split('/')[1]  
                    print(img_path)
                    if count % 5 != 0:
                        train_imgPath = img_path.replace("/Images/", "/images_train/" )
                        shutil.copy(img_path, train_imgPath)
                        tf.write(line + '\n')
                    else:
                        val_imgPath = img_path.replace("/Images/", "/images_val/")
                        shutil.copy(img_path, val_imgPath)
                        vf.write(line + '\n')
                    print("----------->count : ", count)
                    count += 1
                    # print(transcription)
f.close()
tf.close()
vf.close()