'''
Ocr预处理：
1. 删除无标签对应的图片
2. 按比例划分数据集和验证集(json Dbnet)

数据转化：
labelme2txt.py
labelme2cut.py

'''

#################################################  1. 删除无标签对应的图片  ####################################################################
# imgs_path  = '/home/os/window_share/common3/dataset/ocr/cimc/20220519container_tianjin_open/images'
# labels_path = '/home/os/window_share/common3/dataset/ocr/cimc/20220519container_tianjin_open/labels'
# new_file_path =  '/home/os/window_share/common3/dataset/ocr/cimc/20220519container_tianjin_open/new_images'
# os.makedirs(new_file_path, exist_ok=True)


# # 按非空标签保存对应标签和图片
# dirs_list = os.listdir( imgs_path )
# for root,dirs,files in os.walk(imgs_path): #提取文件夹下所有jpg文件复制转移到新的文件夹
#     # str1 = str(files)
#     for str0 in files:
#       find_file = labels_path + '/' + str0.replace(".jpg", ".json")           #.replace(".JPG", ".txt")
#       if not os.path.exists(find_file):
#          print(imgs_path+ '/' + str0)
#          shutil.move(imgs_path + '/' + str0, new_file_path+ '/' + str0)
#         #  os.remove(imgs_path + '/' + str0 )


############################################### 2. 按比例划分数据集和验证集(json Dbnet)  ####################################################################
# path = '/home/os/window_share/common3/dataset/ocr/cimc/20220519container_tianjin_open/images/'
# output_path = '/home/os/window_share/common3/dataset/ocr/cimc/20220519container_tianjin_open/images_val'
# xml_path = '/home/os/window_share/common3/dataset/ocr/cimc/20220519container_tianjin_open/Annotations_val'
# os.makedirs(output_path, exist_ok=True)
# os.makedirs(xml_path, exist_ok=True)


# # 按顺序间隔n帧读取图片保存图片
# dirs_list = os.listdir( path )
# # dirs_list.sort()
# for root,dirs,files in os.walk(path): # root 为当前正在遍历文件夹地址，dirs为该文件夹目录名字，files为该文件夹所有的文件
# #   files.sort(key=lambda x:int(x[:-4]))                        #.jpg -> -4
#   files.sort(key=lambda x:x[:-4])                        #.jpg -> -4
#   for i in range(0,len(files), 4):
#     if files[i][-3:] == 'jpg' : # or files[i][-3:] == 'JPG':
#       print(i)
#       file_path = path + '/' + files[i]
#       new_file_path = output_path + '/' + files[i]
#     #   shutil.copy(file_path, new_file_path)
#       shutil.move(file_path, new_file_path)


#     xml_file = path.replace("images", "Annotations") + '/' + files[i].replace(".jpg",".json")
#     if os.path.exists(xml_file):
#         new_xml_file = path.replace("images", "Annotations_val") + '/' + files[i].replace(".jpg",".json")
#         shutil.move(xml_file, new_xml_file)
#         # shutil.copy(xml_file, new_xml_file)