import os

import albumentations as A
import cv2

# Declare an augmentation pipeline
transform = A.OneOf([
    A.HorizontalFlip(p=0.5),
    A.Affine(scale=(0.8, 1.0)),
    A.ShiftScaleRotate(shift_limit=0.0625, scale_limit=0.2, rotate_limit=45, p=0.2),
    # A.VerticalFlip(p=0.5),
    # A.HueSaturationValue(hue_shift_limit=20, sat_shift_limit=30, val_shift_limit=20, always_apply=False, p=0.5),
    # A.OpticalDistortion(distort_limit=0.05, shift_limit=0.05, interpolation=1, border_mode=4, value=None, mask_value=None, always_apply=False, p=0.5),
    # A.GaussNoise(var_limit=(10.0, 50.0), always_apply=False, p=0.5),
],p=0.5)


image_path = "val/0head"

image_list = os.listdir(image_path)
for image_file in image_list:
    image_file_path = os.path.join(image_path,image_file)
    image = cv2.imread(image_file_path)

    image_h, image_w, _ = image.shape

    # cv2.line(image, (0, int(image_h / 2)), (image_w, int(image_h/2)), (0, 0, 0), 2)
    #
    # output_path = image_file_path.replace(".jpg", "_" + "fv.jpg")

    # cv2.imwrite(output_path, image)

    for i in range(3):
        # Augment an image
        transformed = transform(image=image)
        transformed_image = transformed["image"]
        output_path = image_file_path.replace(".jpg","_"+str(i)+"output.jpg")

        cv2.imwrite(output_path,transformed_image)





# # Declare an augmentation pipeline
# transform = A.Compose([
#     # A.RandomCrop(200, 200, always_apply=False, p=1.0),
#     A.RandomGridShuffle(grid=(2, 2), always_apply=False, p=1),
#     A.ShiftScaleRotate(shift_limit=0.0625, scale_limit=0.2, rotate_limit=45, p=0.2),
# ])
#
# image_path = "JPEGImages"
#
# image_list = os.listdir(image_path)
# for image_file in image_list:
#     image_file_path = os.path.join(image_path,image_file)
#     image = cv2.imread(image_file_path)
#
#     for i in range(10):
#         transformed = transform(image=image)
#         transformed_image = transformed["image"]
#         output_path = image_file_path.replace("JPEGImages","output")
#         output_path = output_path.replace(".jpg",str(i)+"_.jpg")
#         cv2.imwrite(output_path,transformed_image)

# #随机crop目标周边的区域的图片
# import xml.etree.ElementTree as ET
# import random
#
# classid={'safe':0,'oxygen':1,'package':2}  #类别列表，与训练配置文件中的顺序保持一直
#
# image_path = "JPEGImages"
#
# image_list = os.listdir(image_path)
# for image_file in image_list:
#     image_file_path = os.path.join(image_path,image_file)
#
#     Annotations_path = image_file_path.replace("JPEGImages","Annotations")
#     Annotations_path = Annotations_path.replace(".jpg",".xml")
#     tree = ET.parse(Annotations_path)
#     root = tree.getroot()
#     size = root.find('size')
#     w_image = float(size.find('width').text)
#     h_image = float(size.find('height').text)
#
#     for cnt in range(25):
#         for obj in root.iter('object'):
#             image = cv2.imread(image_file_path)
#             output_txt_path = Annotations_path.replace("Annotations","labels")
#             output_image_path = image_file_path.replace("JPEGImages","output_images")
#             output_image_path = output_image_path.replace(".jpg","_"+str(cnt)+".jpg")
#             output_txt_path = output_txt_path.replace(".xml","_"+str(cnt)+".txt")
#             outfile = open(output_txt_path,"w")
#             print(output_txt_path)
#             print(output_image_path)
#             classname = obj.find('name').text
#             cls_id = classid[classname]
#             xmlbox = obj.find('bndbox')
#             xmin = float(xmlbox.find('xmin').text)
#             xmax = float(xmlbox.find('xmax').text)
#             ymin = float(xmlbox.find('ymin').text)
#             ymax = float(xmlbox.find('ymax').text)
#             if ymax > h_image:
#                 ymax = h_image
#             if ymin > h_image:
#                 ymin = h_image
#             if xmax > w_image:
#                 xmax = w_image
#             if xmin > w_image:
#                 xmin = w_image
#
#             x_center=(xmin+xmax)/2-1
#             y_center=(ymin+ymax)/2-1
#
#             random_num = random.randint(50, 300)
#             top_x = int(x_center - random_num)
#             random_num = random.randint(50, 300)
#             top_y = int(y_center - random_num)
#
#             random_num = random.randint(50, 300)
#             bot_x = int(x_center + random_num)
#             random_num = random.randint(50, 300)
#             bot_y = int(y_center + random_num)
#
#             new_image = image[top_y:bot_y, top_x:bot_x]
#
#             new_image_h,new_image_w,_ = new_image.shape
#
#             new_x_center=(x_center-top_x)/new_image_w
#             new_y_center=(y_center-top_y)/new_image_h
#             new_w=(xmax-xmin)/new_image_w
#             new_h=(ymax-ymin)/new_image_h
#
#             cv2.imwrite(output_image_path,new_image)
#
#             outfile.write(str(cls_id)+" "+str(new_x_center)+" "+str(new_y_center)+" "+str(new_w)+" "+str(new_h)+'\n')
#             outfile.close()