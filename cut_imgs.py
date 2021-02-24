import os
import shutil
import glob
# import cv2

# ############################################## 按顺序间隔n帧读取图片保存图片  ################################################
# path = '../../../datasets/jingdianmao/2021-02-05imgs/20210205165632108'
# new_path = '../../../datasets/jingdianmao/2021-02-05imgs_new'

# # 按顺序间隔n帧读取图片保存图片
# dirs_list = os.listdir( path )
# dirs_list.sort()
# for root,dirs,files in os.walk(path): #提取文件夹下所有jpg文件复制转移到新的文件夹
#   files.sort(key=lambda x:int(x[:-4]))
# # for root,dirs,files in dirs_list: #提取文件夹下所有jpg文件复制转移到新的文件夹
#   video_name = root.split('/')[6]
#   for i in range(0,len(files),30):
#     # if files[i][-3:] == 'jpg' or files[i][-3:] == 'JPG':
#       print(i)
#       file_path = root + '/' + files[i]
#       new_file_path = new_path + '/' + video_name + '_'+ files[i]
#       shutil.copy(file_path,new_file_path)
  


#################################################  按非空标签保存对应标签和图片  ####################################################################
  

# path = '/home/window_share/home/os/window_share/likeliang/deep_learning_code/detection/pingtai_centernet/jingdianmao/jingdianmao_mao'
# save_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/jingdianmao/20210205jingdianmao_mao'
# # save_path_no = '/home/window_share/home/os/window_share/ganhaiyang/datasets/jingdianmao/20210205jingdianmao_no_tou'


# # 按非空标签保存对应标签和图片
# dirs_list = os.listdir( path )
# for root,dirs,files in os.walk(path): #提取文件夹下所有jpg文件复制转移到新的文件夹
#     # str1 = str(files)
#     for str0 in files:
#       if str0.endswith('.txt'):
#           with open(root + '/' + str0, "r") as f:
#             img_path = path.replace("jingdianmao_mao", "mao") + '/' + str0.replace('.txt', '.jpg')
#             label_path = path + '/'  + str0

#             if f.readlines(): 
#               new_label_path = save_path.replace("20210205jingdianmao_mao", "20210205jingdianmao_mao_labels") + '/' +str0
#               shutil.copy(label_path, new_label_path)
#               f_new = open(new_label_path, 'r+')
#               print(str0)
#               f_new.seek(0)
#               all_data = f_new.read()
#               split_data = all_data.split(' ')
#               if len(split_data )== 6:  
#                 first_num = 0
#                 new_data = str(first_num) + ' ' + str(split_data[2]) + ' ' + str(split_data[3]) +\
#                             ' ' + str(split_data[4]) +' ' + str(split_data[5])
#                 f_new.seek(0)                         # 将指针移到文件首位
#                 f_new.truncate()                      # 清空文件内容
#                 f_new.write(new_data)
#                 f_new.close()
#               shutil.copy(img_path,save_path)
#             # else:
#             #   shutil.copy(img_path, save_path_no )




#################################################  按比例划分数据集和验证集  ####################################################################
# path = '../../datasets/jingdianmao/20210205jingdianmao_tou'
# output_path = '../../datasets/jingdianmao/val_tou'

# # 按顺序间隔n帧读取图片保存图片
# dirs_list = os.listdir( path )
# dirs_list.sort()
# for root,dirs,files in os.walk(path): # root 为当前正在遍历文件夹地址，dirs为该文件夹目录名字，files为该文件夹所有的文件
#   # files.sort(key=lambda x:int(x[:-4]))
# # for root,dirs,files in dirs_list: #提取文件夹下所有jpg文件复制转移到新的文件夹
#   # video_name = root.split('/')[6]
#   for i in range(0,len(files),4):
#     # if files[i][-3:] == 'jpg' or files[i][-3:] == 'JPG':
#       print(i)
#       file_path = path + '/' + files[i]
#       new_file_path = output_path + '/' + files[i]
#       # shutil.copy(file_path, new_file_path)
#       shutil.move(file_path, new_file_path)


#################################################  删除无标签对应的图片  ####################################################################
  

# imgs_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/waibao_datasets/20210205jingdianmao_no_mao'
# labels_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/waibao_datasets/20210205jingdianmao_no_mao_labels/labels'

# # 按非空标签保存对应标签和图片
# dirs_list = os.listdir( imgs_path )
# for root,dirs,files in os.walk(imgs_path): #提取文件夹下所有jpg文件复制转移到新的文件夹
#     # str1 = str(files)
#     for str0 in files:
#       find_file = labels_path + '/' + str0.replace(".jpg", ".txt").replace(".JPG", ".txt")
#       if not os.path.exists(find_file):
#          print(str0)
#          os.remove(imgs_path + '/' + str0 )
         


#################################################  记录删除越界标签对应的图片  ####################################################################
  

# imgs_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/test_images'
# labels_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/jingdianmao/20210205jingdianmao_2cls/labels'

# # 按非空标签保存对应标签和图片
# # dirs_list = os.listdir( imgs_path )
# for root,dirs,files in os.walk(labels_path): #提取文件夹下所有jpg文件复制转移到新的文件夹
#     # str1 = str(files)
#     for str0 in files:
#       label_file = root + '/' + str0
#       img_file = label_file.replace('20210205jingdianmao_2cls/labels', '20210205jingdianmao_mao'). \
#                  replace(".txt", ".jpg")                # replace(".txt", ".JPG").
#       img_file_2 = label_file.replace('20210205jingdianmao_2cls/labels', '20210205jingdianmao_mao'). \
#                  replace(".txt", ".JPG")                # replace(".txt", ".JPG"). 

#       img_file1 = label_file.replace('20210205jingdianmao_2cls/labels', '20210205jingdianmao_tou'). \
#                  replace(".txt", ".jpg")
#       img_file1_2 = label_file.replace('20210205jingdianmao_2cls/labels', '20210205jingdianmao_tou'). \
#                  replace(".txt", ".JPG")  

#       img_file2 = label_file.replace('20210205jingdianmao_2cls/labels', 'val_mao'). \
#                  replace(".txt", ".jpg")
#       img_file2_2 = label_file.replace('20210205jingdianmao_2cls/labels', 'val_mao'). \
#                  replace(".txt", ".JPG")  

#       img_file3 = label_file.replace('20210205jingdianmao_2cls/labels', 'val_tou'). \
#                  replace(".txt", ".jpg")
#       img_file3_2 = label_file.replace('20210205jingdianmao_2cls/labels', 'val_tou'). \
#                  replace(".txt", ".JPG")  
#       #    os.remove(imgs_path + '/' + str0 )
#       with open(label_file, "r") as f:


#           all_data = f.readlines()
#           for line_data in all_data:
#             line_data = line_data.replace('\t',' ')
#             split_data = str(line_data).split(' ')
#             last_data = split_data[4].replace('\n','')

#             if (float(split_data[1])<0 or float(split_data[1])>=1) or (float(split_data[2])<0 or float(split_data[2])>=1) or (float(split_data[3])<0 \
#                 or float(split_data[3])>=1) or (float(last_data)<0 or float(last_data)>=1): 
#                 print(label_file)

#                 if os.path.exists(img_file):
#                   print(img_file)
#                 elif os.path.exists(img_file1):
#                   print(img_file1)
#                 elif os.path.exists(img_file2):
#                   print(img_file2)
#                 elif os.path.exists(img_file3):
#                   print(img_file3)

#                 elif os.path.exists(img_file_2):
#                   print(img_file_2)
#                 elif os.path.exists(img_file1_2):
#                   print(img_file1_2)
#                 elif os.path.exists(img_file2_2):
#                   print(img_file2_2)
#                 elif os.path.exists(img_file3_2):
#                   print(img_file3_2)

#               # os.remove(find_file)
#               # os.remove(find_file.replace('test_labels', 'test_images').replace(".txt", ".jpg"))
              

  


#################################################  更改文件夹中文件的名字  ####################################################################

imgs_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/jingdianmao/20210205jingdianmao_val'

for root,dirs,files in os.walk(imgs_path): #提取文件夹下所有jpg文件复制转移到新的文件夹
    # str1 = str(files)  "2021020515270881_5551tensor(0.83910, device='cuda:0').jpg"
    #                     '2021020515270881_5551(0.83910.jpg'
    for str0 in files:
      if str0.endswith("='cuda:0').jpg"):
        label_file = root + '/' + str0
        img_file = label_file.replace('tensor(0.', '0'). \
                  replace(", device='cuda:0')", "")                # replace(".txt", ".JPG").
        os.rename(label_file, img_file)
        print(img_file)
      
    
              