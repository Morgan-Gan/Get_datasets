import os
import shutil
import glob
import cv2

# ############################################## 1. 按顺序间隔n帧读取图片保存图片  ################################################
# path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/ele_cap/origin_video_imgs/cap_shoes_person'
# new_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/ele_cap/origin_video_imgs/cap_shoes_person_new'
# os.makedirs(new_path, exist_ok=True)

# # 按顺序间隔n帧读取图片保存图片
# dirs_list = os.listdir( path )
# dirs_list.sort()
# for root,dirs,files in os.walk(path): #提取文件夹下所有jpg文件复制转移到新的文件夹
#   files.sort(key=lambda x:int(x[:-4]))
# # for root,dirs,files in dirs_list: #提取文件夹下所有jpg文件复制转移到新的文件夹
#   # video_name = root.split('/')[6]
#   for i in range(0,len(files),8):
#     # if files[i][-3:] == 'jpg' or files[i][-3:] == 'JPG':
#       print(i)
#       file_path = root + '/' + files[i]
#       # new_file_path = new_path + '/' + video_name + '_'+ files[i]
#       new_file_path = new_path + '/' + files[i]
#       shutil.copy(file_path,new_file_path)
  


################################################# 2.  按非空标签保存对应标签和图片  ####################################################################
  

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




################################################# 3. 按比例划分数据集和验证集  ####################################################################
# path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/head_hand_foot/20210314datasets5000/augment/JPEGImages/'
# output_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/head_hand_foot/20210314datasets5000/augment/PEGImages_val'
# os.makedirs(output_path, exist_ok=True)

# # 按顺序间隔n帧读取图片保存图片
# dirs_list = os.listdir( path )
# # dirs_list.sort()
# for root,dirs,files in os.walk(path): # root 为当前正在遍历文件夹地址，dirs为该文件夹目录名字，files为该文件夹所有的文件
# #   files.sort(key=lambda x:int(x[:-4]))                        #.jpg -> -4
#   files.sort(key=lambda x:x[:-4])                        #.jpg -> -4
#   for i in range(0,len(files), 4):
#     # if files[i][-3:] == 'jpg' or files[i][-3:] == 'JPG':
#       print(i)
#       file_path = path + '/' + files[i]
#       new_file_path = output_path + '/' + files[i]
#       shutil.move(file_path, new_file_path)

#     #   txt_file = path.replace("JPEGImages_person", "sum_labels") + '/' + files[i].replace(".jpg",".txt")
#     #   if os.path.exists(txt_file):
#     #     new_txt_file = path.replace("JPEGImages_person", "labels") + '/' + files[i].replace(".jpg",".txt")
#     #     shutil.copy(txt_file, new_txt_file)

#     #   xml_file = path.replace("JPEGImages_person", "Annotations") + '/' + files[i].replace(".jpg",".xml")
#     #   if os.path.exists(txt_file):
#     #     new_xml_file = path.replace("JPEGImages_person", "Annotations_new") + '/' + files[i].replace(".jpg",".xml")
#     #     shutil.copy(xml_file, new_xml_file)

#       # shutil.copy(file_path, new_file_path)
#     #   shutil.move(file_path, new_file_path)


#################################################  4. 删除无标签对应的图片  ####################################################################
  

# imgs_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/protection_shoes/2021-3-5鞋子/JPEGImages'
# labels_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/protection_shoes/2021-3-5鞋子/labels'

# # 按非空标签保存对应标签和图片
# dirs_list = os.listdir( imgs_path )
# for root,dirs,files in os.walk(imgs_path): #提取文件夹下所有jpg文件复制转移到新的文件夹
#     # str1 = str(files)
#     for str0 in files:
#       find_file = labels_path + '/' + str0.replace(".jpg", ".txt")           #.replace(".JPG", ".txt")
#       if not os.path.exists(find_file):
#          print(str0)
#          os.remove(imgs_path + '/' + str0 )
         


#################################################  5. 记录删除越界标签对应的图片  ####################################################################
  

# imgs_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/head_hand_foot/20210305head_hand_foot/head_hand_foot/augment/JPEGImages/'
# labels_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/head_hand_foot/20210305head_hand_foot/head_hand_foot/augment/labels/'

# # 按非空标签保存对应标签和图片
# # dirs_list = os.listdir( imgs_path )
# for root,dirs,files in os.walk(labels_path): #提取文件夹下所有jpg文件复制转移到新的文件夹
#     # str1 = str(files)
#     for str0 in files:
#       label_file = root + '/' + str0
#     #   img_file = label_file.replace('/labels', '/JPEGImages'). \
#     #              replace(".txt", ".jpg")                # replace(".txt", ".JPG").

#       img_train = label_file.replace('/labels', '/JPEGImages_train'). \
#                  replace(".txt", ".jpg")  
#       img_val = label_file.replace('/labels', '/JPEGImages_val'). \
#                  replace(".txt", ".jpg")  

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
#                 # os.remove(label_file)

#                 if os.path.exists(img_train):
#                   print(img_train)
#                 #   os.remove(img_train)
#                 elif os.path.exists(img_val):
#                   print(img_val)
#                 #   os.remove(img_val)

#                 # os.remove(img_file)
# print("------------------------------------Done!")

                # if os.path.exists(img_file):
                #   print(img_file)
                # elif os.path.exists(img_file1):
                #   print(img_file1)
                # elif os.path.exists(img_file2):
                #   print(img_file2)
                # elif os.path.exists(img_file3):
                #   print(img_file3)


              # os.remove(find_file)
              # os.remove(find_file.replace('test_labels', 'test_images').replace(".txt", ".jpg"))
              

  


#################################################  6. 更改文件夹中文件的名字  ####################################################################

# imgs_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/protection_shoes/2021-3-5shoes/labels'

# for root,dirs,files in os.walk(imgs_path): #提取文件夹下所有jpg文件复制转移到新的文件夹
#     # str1 = str(files)  "2021020515270881_5551tensor(0.83910, device='cuda:0').jpg"
#     #                     '2021020515270881_5551(0.83910.jpg'
#     for str0 in files:
#       print(str0)
#       if str0.endswith(".txt"):
#         label_file = root + '/' + str0
#         img_file = label_file.replace('.txt', 'personw.txt')
#         os.rename(label_file, img_file)
#         print(img_file)
      
    


#################################################  7. 按图片取对应标签  ####################################################################
  

# imgs_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/head_hand_foot/20210314datasets5000/new_imgs'
# xml_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/head_hand_foot/20210314datasets5000/Annotations'
# labels_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/head_hand_foot/20210314datasets5000/labels'

# new_label_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/head_hand_foot/20210314datasets5000/new_labels'
# os.makedirs(new_label_path, exist_ok=True)
# new_xml_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/head_hand_foot/20210314datasets5000/new_xml'
# os.makedirs(new_xml_path, exist_ok=True)

# # 按非空标签保存对应标签和图片
# # dirs_list = os.listdir( imgs_path )
# for root,dirs,files in os.walk(imgs_path): #提取文件夹下所有jpg文件复制转移到新的文件夹
#     # str1 = str(files)
#     for str0 in files:
#     #   if str0.endswith(".jpg"):
#           # find_file = imgs_path + '/' + str0.replace(".jpg", ".txt").replace(".JPG", ".txt")
#           find_labels_file = str0.replace(".jpg", ".txt")
#           # if os.path.exists(find_file):
#           print(str0)
#           new_labels_file = new_label_path + '/' + find_labels_file
#           shutil.copy(labels_path + '/' + find_labels_file,  new_labels_file)

#           find_xml_file = str0.replace(".jpg", ".xml")
#           # if os.path.exists(find_file):
#           new_labels_file = new_xml_path + '/' + find_xml_file
#           shutil.copy(xml_path + '/' + find_xml_file,  new_labels_file)





################################################  8. 更改文件夹中文件的名字  ####################################################################

# imgs_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/jingdianmao/20210205jingdianmao_2cls/labels'

# for root,dirs,files in os.walk(imgs_path): #提取文件夹下所有jpg文件复制转移到新的文件夹
#     # str1 = str(files)  "2021020515270881_5551tensor(0.83910, device='cuda:0').jpg"
#     #                     '2021020515270881_5551(0.83910.jpg'
#     for str0 in files:
#       # print(str0)
#       if str0.endswith("='cuda:0').txt"):                          # .jpg
#         label_file = root + '/' + str0
#         img_file = label_file.replace('tensor(0.', '0'). \
#                   replace(", device='cuda:0')", "")                # replace(".txt", ".JPG").
#         os.rename(label_file, img_file)
#         # shutil.copy(old_labels_path + '/' + find_file,  new_label_path)
#         print(label_file)
#         print(img_file)
#       elif str0.endswith(".JPG"):
#         label_file = root + '/' + str0
#         img_file = label_file.replace('.JPG', '.jpg')
#         os.rename(label_file, img_file)
#         # shutil.copy(old_labels_path + '/' + find_file,  new_label_path)
#         print(label_file)
#         print(img_file)
        


# ################################################# 9.  根据标签列表取对应图片  ####################################################################
  

# txt_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/head_hand_foot/20210317head_hand_foot/20210317head_hand_foot_val.txt'
# # imgs_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/head_hand_foot/20210317head_hand_foot/images'
# # save_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/head_hand_foot/20210317head_hand_foot/images_val'
# xml_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/head_hand_foot/20210317head_hand_foot/Annotations'
# xml_save_path = '/home/window_share/home/os/window_share/ganhaiyang/Alg_Proj/2.2.0_20201117_042200/QK_AI_Train_performance/test_tool/head_hand_foot/Annotations/'
# os.makedirs(xml_save_path, exist_ok=True)


# with open(txt_path, "r") as f:

#   if f.readlines(): 

#     f.seek(0)
#     all_data = f.read().split('\n')
#     for str0 in all_data :
#     #   split_data = str0.split('/')[-1]
#     #   imgs_path1 = imgs_path + '/' + split_data
#     #   imgs_new_path = save_path + '/' + split_data

#       split_data = str0.split('/')[-1].replace('.jpg', '.xml')
#       xml_path1 = xml_path + '/' + split_data
#       xml_new_path = xml_save_path + '/' + split_data
 
#       print(xml_path1)
#     #   shutil.copy(imgs_path1, imgs_new_path)
#       shutil.copy(xml_path1, xml_new_path)


# ################################################# 9.  根据标签列表取对应标签  ####################################################################
  

# txt_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/ele_cap_protection_shoes_4cls/20210225ele_cap_protection_shoes_4cls_val.txt'
# imgs_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/ele_cap_protection_shoes_4cls/labels'
# save_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/ele_cap_protection_shoes_4cls/labels_val'
# os.makedirs(save_path, exist_ok=True)


# with open(txt_path, "r") as f:

#   if f.readlines(): 

#     f.seek(0)
#     all_data = f.read().split('\n')
#     for str0 in all_data :
#       split_data = str0.split('/')[-1].replace('.jpg', '.txt')
#       imgs_path1 = imgs_path + '/' + split_data
#       imgs_new_path = save_path + '/' + split_data
 
#       print(imgs_path1)
#       shutil.copy(imgs_path1, imgs_new_path)



#################################################  10. 对比两个文件夹图片  ####################################################################
  
# # xml_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/head_hand_foot/20210314datasets5000/augment/Annotations/'
# imgs_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/head_hand_foot/20210317head_hand_foot/images/'
# save_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/head_hand_foot/20210317head_hand_foot/images_train'
# os.makedirs(save_path, exist_ok=True)
# # old_labels_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/jingdianmao/20210205jingdianmao_2cls/labels'
# # labels_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/jingdianmao/test_labels'

# # 按非空标签保存对应标签和图片
# # dirs_list = os.listdir( imgs_path )
# for root,dirs,files in os.walk(imgs_path): #提取文件夹下所有jpg文件复制转移到新的文件夹
#     # str1 = str(files)
#     for str0 in files:
#       # if str0.endswith(".xml"):
#         # find_file = imgs_path.replace("Annotations", "labels") + '/' + str0.replace(".xml", ".txt")              #+ '/' + str0.replace("leg", "should")
#         find_file = imgs_path.replace("images", "images_val")+ '/' + str0            #+ '/' + str0.replace("leg", "should")
#         if not os.path.exists(find_file):
#             print(save_path+ '/' + str0)
#         # new_label_path = labels_path + '/' + find_file
#             # os.remove(xml_path + '/' + str0)                                     # shutil.rmtree删除文件夹
#             shutil.copy(imgs_path + '/' + str0, save_path+ '/' + str0)










# ################################################# 11.  更改每个标签内容  ####################################################################
  
# labels_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/ele_cap/origin_video_imgs/cap_shoes_person_leg_out/labels'
# save_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/ele_cap/origin_video_imgs/cap_shoes_person_leg_out/labels_new'
# os.makedirs(save_path, exist_ok=True)


# # 按非空标签保存对应标签和图片
# for root,dirs,files in os.walk(labels_path): #提取文件夹下所有jpg文件复制转移到新的文件夹
#     # str1 = str(files)
#     for str0 in files:
#       if str0.endswith('.txt'):
#           with open(root + '/' + str0, "r") as f:
#             img_path = labels_path.replace("cap_shoes_person_leg_out/labels", "cap_shoes_person_should_out") + '/' + str0.replace('leg', 'should').replace('.txt', '.jpg')
#             img = cv2.imread(img_path)
#             h,w,_ = img.shape
#             label_path = labels_path + '/'  + str0

#             if f.readlines(): 
#               new_label_path = save_path + '/' +str0
#               shutil.copy(label_path, new_label_path)
#               f_new = open(new_label_path, 'a+')             #r+
#               print(str0)
#               f_new.seek(0)
#               all_data = f_new.read()
#               split_data = all_data.split('\n')
#               f_new.seek(0) 
#               f_new.truncate()                      # 清空文件内容

#               for i in range(len(split_data)-1):
#                   a = split_data[i].split(' ')
#                   print(a)
#                   y1 = h + int(a[2])
#                   y2 = h + int(a[4])
#                   new_data = a[0] + ' ' + a[1] + ' ' + str(y1) +\
#                                ' ' + a[3] + ' ' + str(y2) + '\n'
#                   f_new.write(new_data)
#               f_new.close()



# ################################################# 12.  根据标签取图片，合并两个标签内容 ####################################################################
  
# labels_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/ele_cap/origin_video_imgs/cap_shoes_person_leg_out/labels_new'
# img_save_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/ele_cap/origin_video_imgs/person_imgs'
# os.makedirs(img_save_path, exist_ok=True)


# # 按非空标签保存对应标签和图片
# for root,dirs,files in os.walk(labels_path): #提取文件夹下所有jpg文件复制转移到新的文件夹
#     for str0 in files:
#       if str0.endswith('.txt'):
#           with open(root + '/' + str0, "r") as f:
#             img_path = labels_path.replace("cap_shoes_person_leg_out/labels_new", "cap_shoes_person") + '/' + str0.replace('leg', '').replace('.txt', '.jpg')
#             label_path = labels_path + '/'  + str0
#             imgs_save_path = img_save_path + '/'  + str0.replace('leg.txt','person.jpg')
#             shutil.copy(img_path, imgs_save_path)


#             if f.readlines(): 
#               new_label_path = label_path.replace("cap_shoes_person_leg_out/labels_new", "cap_shoes_person_should_out/labels").replace("leg", "should")
#               f_new = open(new_label_path, 'a+')             #r+
#               print(str0)
#               f.seek(0)                             # read之前要seek定位
#               all_data = f.read()
#               split_data = all_data.split('\n')
              

#               for i in range(len(split_data)-1):
#                   f_new.seek(0) 
#                   new_data = split_data[i] + '\n'
#                   f_new.write(new_data)
#               f_new.close()
#       os.rename(new_label_path, new_label_path.replace('should.txt', 'person.txt'))



################################################# 13.  合并两个标签内容到一个新的标签 ####################################################################
# img_path = "/home/window_share/home/os/window_share/ganhaiyang/datasets/head_hand_foot/20210305shoes/JPEGImages_out"
# labels1_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/head_hand_foot/20210305shoes/labels_ps'
# labels2_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/head_hand_foot/20210305shoes/norm_hand_labels'
# save_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/head_hand_foot/20210305shoes/sum_labels'
# os.makedirs(save_path, exist_ok=True)
# img_save_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/head_hand_foot/20210305shoes/choice_imgs'
# os.makedirs(img_save_path, exist_ok=True)


# # 按非空标签保存对应标签和图片
# for root,dirs,files in os.walk(img_path): #提取文件夹下所有jpg文件复制转移到新的文件夹
#     for str0 in files:
#         print(str0)
#         find_labels1 = labels1_path + '/'+ str0.replace("_out.jpg", "personw.txt")
#         find_labels2 = labels2_path + '/'+ str0.replace("_out.jpg", "personw.txt")
#         new_labels = save_path + '/'+ str0.replace("_out.jpg", "personw.txt")
#         shutil.copy(img_path.replace("JPEGImages_out", "JPEGImages") + '/' + str0.replace("_out.jpg", "personw.jpg"),  img_save_path + '/' + str0.replace("_out.jpg", "personw.jpg"))


#         if os.path.exists(find_labels1) and os.path.exists(find_labels2) :
#             outputFile = open(new_labels, "a")
#             inputFile1 = open(find_labels1, "r")
#             inputFile2 = open(find_labels2, "r")

#             for line in inputFile1:
#                 outputFile.write(line)
#             for line in inputFile2:
#                 outputFile.write(line)
#         # else:
#         elif os.path.exists(find_labels1):
#             shutil.copy(find_labels1, new_labels)
#         elif os.path.exists(find_labels2):
#             shutil.copy(find_labels2, new_labels)

# print("-----------------------------------done")


          
# # ################################################# 14.  根据标签截取保存图片  ####################################################################
img_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/head_hand_foot/20210317head_hand_foot/images_train'
labels_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/head_hand_foot/20210317head_hand_foot/labels'
save_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/head_hand_foot/20210317head_hand_foot/20210317cap_shoes_4classifier/train'
os.makedirs(save_path, exist_ok=True)


# 按非空标签保存对应标签和图片
for root,dirs,files in os.walk(img_path): #提取文件夹下所有jpg文件复制转移到新的文件夹
    for str0 in files:
        print(str0)
        with open(labels_path + '/' + str0.replace(".jpg", ".txt"), "r") as f:
            img_read_path = os.path.join(img_path, str0)
            image = cv2.imread(img_read_path)
            h,w,_ = image.shape

            number = 0
            for content in f:
                if "\t" in content:
                    content = content.replace("\t"," ")
                content_list = content.split(" ")

                # yolo normal(xywh) -> xyxy
                bbox_width = float(content_list[3]) * w
                bbox_height = float(content_list[4]) * h
                center_x = float(content_list[1]) * w
                center_y = float(content_list[2]) * h
                top_x = center_x - (bbox_width / 2)
                top_y = center_y - (bbox_height / 2)
                bot_x = center_x + (bbox_width / 2)
                bot_y = center_y + (bbox_height / 2)

                img_cut = image[max(0, int(top_y)): int(bot_y), max(0, int(top_x)) : int(bot_x)]
                if content_list[0] == '0':
                    head_path = os.path.join(save_path, "head")   
                    os.makedirs(head_path, exist_ok=True)
                    save_head = head_path +'/' + str0.split('.')[0] +"_" + str(number) +".jpg"               
                    cv2.imwrite(save_head,img_cut ) 
                    number += 1
                elif content_list[0] == '1':
                    head_path = os.path.join(save_path, "ele_cap")   
                    os.makedirs(head_path, exist_ok=True)
                    save_head = head_path +'/' + str0.split('.')[0] +"_" + str(number) +".jpg"               
                    cv2.imwrite(save_head,img_cut ) 
                    number += 1
                elif content_list[0] == '2':
                    head_path = os.path.join(save_path, "protection_shoes")   
                    os.makedirs(head_path, exist_ok=True)
                    save_head = head_path +'/' + str0.split('.')[0] +"_" + str(number) +".jpg"               
                    cv2.imwrite(save_head,img_cut ) 
                    number += 1
                elif content_list[0] == '3':
                    head_path = os.path.join(save_path, "shoes")   
                    os.makedirs(head_path, exist_ok=True)
                    save_head = head_path +'/' + str0.split('.')[0] +"_" + str(number) +".jpg"               
                    cv2.imwrite(save_head,img_cut ) 
                    number += 1
print("------------------------------------------------done!")



# ################################################# 15.  更改每个标签类别  ####################################################################
  
# labels_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/head_hand_foot/20210305head_hand_foot/labels/'
# save_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/head_hand_foot/20210305head_hand_foot/labels_new'
# os.makedirs(save_path, exist_ok=True)


# # 按非空标签保存对应标签和图片
# for root,dirs,files in os.walk(labels_path): #提取文件夹下所有jpg文件复制转移到新的文件夹
#     # str1 = str(files)
#     for str0 in files:
#         with open(root + '/' + str0, "r") as f:
#             label_path = labels_path + '/'  + str0

#             if f.readlines(): 
#                 new_label_path = save_path + '/' +str0
#                 shutil.copy(label_path, new_label_path)
#                 f_new = open(new_label_path, 'a+')             #r+
#                 print(str0)
#                 f_new.seek(0)
#                 all_data = f_new.read()
#                 split_data = all_data.split('\n')
#                 f_new.seek(0) 
#                 f_new.truncate()                      # 清空文件内容

#                 for i in range(len(split_data)-1):
#                     if '\t' in split_data[i]:
#                         split_data[i] = split_data[i].replace('\t', ' ')
#                     a = split_data[i].split(' ')
#                     if a[0] == '3':
#                         new_data = '2' + ' ' + a[1] + ' ' + a[2] +\
#                                     ' ' + a[3] + ' ' + a[4] + '\n'
#                     else:
#                         new_data = a[0] + ' ' + a[1] + ' ' + a[2] +\
#                                     ' ' + a[3] + ' ' + a[4] + '\n'
#                     f_new.write(new_data)
#                 f_new.close()



# ################################################# 16.  根据标签取图片 ####################################################################
  
# labels_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/head_hand_foot/20210314datasets5000/labels'
# img_save_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/head_hand_foot/20210314datasets5000/img_new'
# os.makedirs(img_save_path, exist_ok=True)


# # 按非空标签保存对应标签和图片
# for root,dirs,files in os.walk(labels_path): #提取文件夹下所有jpg文件复制转移到新的文件夹
#     for str0 in files:
#         print(str0)
#         img_path = labels_path.replace("labels", "JPEGImages") + '/' + str0.replace('.txt', '.jpg')
#         imgs_save_path = img_save_path + '/'  + str0.replace('.txt', '.jpg')
#         shutil.copy(img_path, imgs_save_path)
# print("------------------------------------------------done!")


