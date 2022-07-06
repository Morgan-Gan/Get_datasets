import cv2
import os
import shutil

import sys
import subprocess

__dir__ = os.path.dirname(os.path.abspath(__file__))
sys.path.append(__dir__)
sys.path.append(os.path.abspath(os.path.join(__dir__, '../..')))

os.environ['CUDA_VISIBLE_DEVICES'] = "0"
# os.environ["FLAGS_allocator_strategy"] = 'auto_growth'

# def save_img():
#     video_path = '/home/os/window_share/common3/dataset/ocr/cimc/20220419container_taicang/video/4'
#     images_path = '/home/os/window_share/common3/dataset/ocr/cimc/20220419container_taicang/images'
#     os.makedirs(images_path, exist_ok=True)
#     videos = os.listdir(video_path)
#     count = 0
#     for video_name in videos:
#         file_name = video_name.split('.')[0]  #.split('_')[2]
#         folder_name = images_path + '/' + file_name
#         os.makedirs(folder_name, exist_ok=True)
#         vc = cv2.VideoCapture(video_path+'/'+video_name)
#         c=0
#         timeF = 10                                            # 视频帧计数间隔频率30
#         rval=vc.isOpened()

#         while rval:
#             c = c + 1                                              # 1
#             rval, frame = vc.read()
#             pic_path = folder_name+'/'
#             if rval:
#                 if(c % timeF ==0):                      # h    w
#                     cropped = frame[217:1241, 281:2197] #[72:834, 7:1214]                                   # frame[0:1080, 0:1500] # 裁剪坐标为[y0:y1, x0:x1]
#                     # cropped = frame[53:1003, 15:1919]                                    # frame[0:1080, 0:1500] # 裁剪坐标为[y0:y1, x0:x1]
#                     img_name = pic_path + file_name + '_' +str(c) + '.jpg'
#                     cv2.imwrite(img_name, cropped)   # .png
#                     cv2.waitKey(1)
#                     print("It is saving {} fps".format(c))
#                     print("--------------> get {} fps imgs !",format(count))
#                     count += 1
#             else:
#                 break

#         vc.release()
#         print('save_success')
#         print(folder_name)
# save_img()


###########################################  间隔帧保存视频，并合并到一个文件夹中##############################################
# -*- coding: utf-8 -*-   
import os 
import cv2
import csv
import numpy as np
import concurrent.futures
 
def GetImgNameByEveryDir(file_dir,videoProperty):  
    FileNameWithPath = [] 
    FileName         = []
    FileDir          = []
    # videoProperty=['.png','jpg','bmp']
    for root, dirs, files in os.walk(file_dir):  
        for file in files:  
            if os.path.splitext(file)[1] in videoProperty:  
                FileNameWithPath.append(os.path.join(root, file))  # 保存图片路径
                FileName.append(file)                              # 保存图片名称
                FileDir.append(root[len(file_dir):])               # 保存图片所在文件夹
    return FileName,FileNameWithPath,FileDir
 
# 以视频文件名创建文件夹，然后保存图像到对应文件夹
def AVI_To_Img_And_save(video_file):
	video_name = video_file.split('/')[-1].split('.')[0]
	print('当前处理的视频为：',video_file)
	cap = cv2.VideoCapture(video_file)
	rval = cap.isOpened()
	framenum=0
	while rval:
		rval, frame  = cap.read()
		if framenum%25!=0:
			framenum+=1
			continue
		save_dir     = '/home/os/window_share/common3/dataset/car_window/car_window20220704/imgs_right/'
		os.makedirs(save_dir, exist_ok=True)
		Img_savename = save_dir + '/' + video_name + '_' + '%08d'%framenum +'.jpg'
		if rval:
			if os.path.exists(Img_savename)==False:
				cv2.imwrite(Img_savename, frame,[int(cv2.IMWRITE_JPEG_QUALITY), 100]) 
		else:
			break
		framenum+=1
		print('正在处理视频{}的第{}帧,rval = {}...'.format(video_name,framenum,rval))
	cap.release()
	return ''
	
 
FileName,FileNameWithPath,FileDir = GetImgNameByEveryDir('/home/os/window_share/common3/dataset/car_window/car_window20220704/right/',['.wmv','.mkv','.mp4'])
print('FileName = ',FileName)

# 同时运行线程最多20个，多的会等待
with concurrent.futures.ThreadPoolExecutor(max_workers=20) as process:
	process.map(AVI_To_Img_And_save,FileNameWithPath)
 
 


###########################################3.1  合成视频##############################################
# import os
# import cv2
# file_dir = '/home/os/window_share/ganhaiyang/datasets/protection_shoes/918demo/ps_imgs/ps_imgs_output_b/'
# list = []
# for root, dirs, files in os.walk(file_dir):
#     for file in files:
#         list.append(file)  # 获取目录下文件名列表

# video = cv2.VideoWriter('/home/os/window_share/ganhaiyang/datasets/protection_shoes/918demo/ps_imgs/ps_imgs_output_b.mp4',
#                         cv2.VideoWriter_fourcc(*'MJPG'), 30, (1920, 1080))  # *'MJPG'定义保存视频目录名称及压缩格式，fps=10,像素为1280*720, (1920, 1080)
# list.sort(key=lambda x:x[:-4])
# for i in range(1, len(list)):
#     img = cv2.imread(file_dir+list[i-1])  # 读取图片
#     print(file_dir+list[i-1])
#     # img = cv2.resize(img, (1920, 1080))  # 将图片转换为1280*720  1080,1920
#     video.write(img)  # 写入视频

# video.release()

# # import cv2
# # import glob
 
# # def resize(img_array, align_mode):
# #     _height = len(img_array[0])
# #     _width = len(img_array[0][0])
# #     for i in range(1, len(img_array)):
# #         img = img_array[i]
# #         height = len(img)
# #         width = len(img[0])
# #         if align_mode == 'smallest':
# #             if height < _height:
# #                 _height = height
# #             if width < _width:
# #                 _width = width
# #         else:
# #             if height > _height:
# #                 _height = height
# #             if width > _width:
# #                 _width = width
 
# #     for i in range(0, len(img_array)):
# #         img1 = cv2.resize(img_array[i], (_width, _height), interpolation=cv2.INTER_CUBIC)
# #         img_array[i] = img1
 
# #     return img_array, (_width, _height)
 
# # def images_to_video(path):
# #     img_array = []
 
# #     for filename in glob.glob(path+'/*.jpg'):
# #         img = cv2.imread(filename)
# #         if img is None:
# #             print(filename + " is error!")
# #             continue
# #         img_array.append(img)
 
# #     # 图片的大小需要一致
# #     img_array, size = resize(img_array, 'largest')
# #     fps = 1
# #     out = cv2.VideoWriter('demo.avi', cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
 
# #     for i in range(len(img_array)):
# #         out.write(img_array[i])
# #     out.release()
 
# # def main():
# #     path = "/home/os/window_share/ganhaiyang/中集宝伟/oxygen/oxygen_demo_images/"
# #     images_to_video(path)
 
# # if __name__ == "__main__":
# #     main()


# ################################################  8. 更改文件夹中文件的名字  ####################################################################
# imgs_path = '/home/os/window_share/ganhaiyang/datasets/protection_shoes/918demo/ps_imgs/demo_imgs_output_a/'
# xml_save_path = '/home/os/window_share/ganhaiyang/datasets/protection_shoes/918demo/ps_imgs/demo_imgs_output_b/'
# os.makedirs(xml_save_path, exist_ok=True)

# for root,dirs,files in os.walk(imgs_path): #提取文件夹下所有jpg文件复制转移到新的文件夹
#     # str1 = str(files)  "2021020515270881_5551tensor(0.83910, device='cuda:0').jpg"
#     #                     '2021020515270881_5551(0.83910.jpg'
#     files.sort(key=lambda x:x[:-4])
#     i = 0
#     for str0 in files:
#     # for i, str0 in enumerate(files) :
#       # print(str0)
#       if str0.endswith(".jpg"):                          # .jpg
#         label_file = root + '/' + str0
#         # img_file = label_file.replace('tensor(0.', '0'). \
#         #           replace(", device='cuda:0')", "")                # replace(".txt", ".JPG").
#         # nem_name = str0.replace("frame_", "").replace(".jpg", "").zfill(4) + ".jpg"  #.zfill(3)
#         nem_name = str(i) + ".jpg"  #.zfill(3)
#         # os.rename(label_file, xml_save_path + '/' + nem_name)
#         shutil.copy(label_file,  xml_save_path + '/' + nem_name)
#         print(label_file)
#         i = i+1

