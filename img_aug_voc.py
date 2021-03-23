import xml.etree.ElementTree as ET
import pickle
import os
from os import getcwd
import numpy as np
from PIL import Image
import shutil
import matplotlib.pyplot as plt

import imgaug as ia
from imgaug import augmenters as iaa


ia.seed(1)


def read_xml_bndboxs(root, image_id):
    in_file = open(os.path.join(root, image_id))
    tree = ET.parse(in_file)
    root = tree.getroot()
    bndboxlist = []

    for object in root.findall('object'):  
        bndbox = object.find('bndbox')  
        xmin = int(bndbox.find('xmin').text)
        xmax = int(bndbox.find('xmax').text)
        ymin = int(bndbox.find('ymin').text)
        ymax = int(bndbox.find('ymax').text)
        bndboxlist.append([xmin, ymin, xmax, ymax])

    return bndboxlist


def save_aug_xml_file(src_xml_file, image_id, aug_bndbox, aug_xml_dir, aug_file_name):
    in_file = open(os.path.join(src_xml_file, str(image_id) + '.xml'))  # 这里root分别由两个意思
    tree = ET.parse(in_file)
    elem = tree.find('filename')
    elem.text = aug_file_name + '.jpg'
    xmlroot = tree.getroot()
    index = 0

    for object in xmlroot.findall('object'):  # 找到root节点下的所有country节点
        bndbox = object.find('bndbox')  # 子节点下节点rank的值

        # xmin = int(bndbox.find('xmin').text)
        # xmax = int(bndbox.find('xmax').text)
        # ymin = int(bndbox.find('ymin').text)
        # ymax = int(bndbox.find('ymax').text)

        new_xmin = aug_bndbox[index][0]
        new_ymin = aug_bndbox[index][1]
        new_xmax = aug_bndbox[index][2]
        new_ymax = aug_bndbox[index][3]

        xmin = bndbox.find('xmin')
        xmin.text = str(new_xmin)
        ymin = bndbox.find('ymin')
        ymin.text = str(new_ymin)
        xmax = bndbox.find('xmax')
        xmax.text = str(new_xmax)
        ymax = bndbox.find('ymax')
        ymax.text = str(new_ymax)

        index = index + 1

    tree.write(os.path.join(aug_xml_dir, aug_file_name + '.xml'))


def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False


class getAllAnnnotations():

    def __init__(self):
        self.classes = ['head', 'hand', 'foot']

    def convert(self, size, box):
        dw = 1./size[0]
        dh = 1./size[1]
        x = (box[0] + box[1])/2.0
        y = (box[2] + box[3])/2.0
        w = box[1] - box[0]
        h = box[3] - box[2]
        x = x*dw
        w = w*dw
        y = y*dh
        h = h*dh
        return (x,y,w,h)

    def convert_annotation(self,dataDir):
        txtdir = dataDir+'/labels'
        try:
            shutil.rmtree(txtdir)
        except FileNotFoundError as e:
            a = 1
        mkdir(txtdir)
        print('start create txt file....')
        xmls = os.listdir(dataDir+'/Annotations')
        for xml in xmls:
            in_file = open(dataDir+'/Annotations/%s'%(xml))
            out_file = open(dataDir+'/labels/%s.txt'%(xml[:-4]), 'w')
            tree = ET.parse(in_file)
            root = tree.getroot()
            size = root.find('size')
            w = int(size.find('width').text)
            h = int(size.find('height').text)

            for obj in root.iter('object'):
                difficult = obj.find('difficult').text
                cls = obj.find('name').text
                if cls not in self.classes or int(difficult) == 1:
                    continue
                cls_id = self.classes.index(cls)
                xmlbox = obj.find('bndbox')
                b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
                bb = self.convert((w,h), b)
                out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
        print('finish create txt file....')

def create_aug_data(modelpath,AUGLOOP):

    SRC_IMG_DIR = modelpath+"/JPEGImages"
    SRC_XML_DIR = modelpath+"/Annotations"

    AUG_XML_DIR = modelpath+"/augment/Annotations"  # 存储增强后的XML文件夹路径
    try:
        shutil.rmtree(AUG_XML_DIR)
    except FileNotFoundError as e:
        a = 1
    os.makedirs(AUG_XML_DIR)

    AUG_IMG_DIR = modelpath+"/augment/JPEGImages"  # 存储增强后的影像文件夹路径
    try:
        shutil.rmtree(AUG_IMG_DIR)
    except FileNotFoundError as e:
        a = 1
    mkdir(AUG_IMG_DIR)


    boxes_img_aug_list = []
    new_bndbox = []
    new_bndbox_list = []

    # 影像增强

    seq = iaa.Sequential([
            iaa.Flipud(0.5),  # 垂直翻转
            iaa.Fliplr(0.5),  # 水平翻转
            iaa.Multiply((0.88, 1.1)),  # 调节亮度
            iaa.Affine(scale=(0.8, 1.0)), #图像缩放
            #iaa.Affine(rotate=(-180, 180)),
            iaa.Affine(shear=(-10, 10)),
            #iaa.Affine(scale={"x": (0.8, 1.5), "y": (0.8, 1.5)}),
            #iaa.Resize({"height": "keep-aspect-ratio" , "width":(0.8, 1.2)}),
            #iaa.CropAndPad(percent=(-0.25, 0.25)),
            #iaa.Resize((0.8, 1.0)),
            iaa.Add((-20, 20)),
            #iaa.Invert(0.25, per_channel=0.5),
            iaa.Sometimes(
              0.5,
              iaa.CoarseDropout(0.01, size_percent=0.5),
              iaa.Sequential([iaa.Sharpen(alpha=0.2)])
            ),
            #iaa.Add((-40, 40), per_channel=0.5),
            #iaa.Multiply((0.5, 1.5), per_channel=0.5),
            iaa.Sequential([
                iaa.ChangeColorspace(from_colorspace="RGB", to_colorspace="HSV"),
                iaa.WithChannels(0, iaa.Add((50, 100))),
                iaa.ChangeColorspace(from_colorspace="HSV", to_colorspace="RGB")
            ])
        ])



    for root, sub_folders, files in os.walk(SRC_XML_DIR):
        count = 0
        for name in files:
            
            bndbox = read_xml_bndboxs(SRC_XML_DIR, name)
            shutil.copy(os.path.join(SRC_XML_DIR, name), AUG_XML_DIR)
            shutil.copy(os.path.join(SRC_IMG_DIR, name[:-4] + '.jpg'), AUG_IMG_DIR)
            count = count+1
            print('----------augment:',name,count)
            for epoch in range(AUGLOOP):
                seq_det = seq.to_deterministic()  # 保持坐标和图像同步改变，而不是随机
                # 读取图片
                img = Image.open(os.path.join(SRC_IMG_DIR, name[:-4] + '.jpg')).convert('RGB')
                # sp = img.size
                img = np.asarray(img)
                # bndbox 坐标增强

                #一次遍历，处理每一个标注框
                for i in range(len(bndbox)):
                    #得到当前标注框的位置信息
                    bbs = ia.BoundingBoxesOnImage([
                        ia.BoundingBox(x1=bndbox[i][0], y1=bndbox[i][1], x2=bndbox[i][2], y2=bndbox[i][3]),
                    ], shape=img.shape)

                    #返回增强后的图片和标注框信息
                    bbs_aug = seq_det(bounding_boxes=bbs)
                    boxes_img_aug_list.append(bbs_aug)

                    # new_bndbox_list:[[x1,y1,x2,y2],...[],[]]
                    #print(bbs_aug)
                    n_x1 = int(max(1, min(img.shape[1], bbs_aug.bounding_boxes[0].x1)))
                    n_y1 = int(max(1, min(img.shape[0], bbs_aug.bounding_boxes[0].y1)))
                    n_x2 = int(max(1, min(img.shape[1], bbs_aug.bounding_boxes[0].x2)))
                    n_y2 = int(max(1, min(img.shape[0], bbs_aug.bounding_boxes[0].y2)))
                    if n_x1 == 1 and n_x1 == n_x2:
                        n_x2 += 1
                    if n_y1 == 1 and n_y2 == n_y1:
                        n_y2 += 1
                    if n_x1 >= n_x2 or n_y1 >= n_y2:
                        print('error', name)
                    new_bndbox_list.append([n_x1, n_y1, n_x2, n_y2])
                # 存储变化后的图片
                image_aug = seq_det.augment_images([img])[0]
                
                savefilebasename = str(name[:-4]) + '_' +str(epoch*10)
                path = os.path.join(AUG_IMG_DIR,  savefilebasename+'.jpg')
                image_auged = bbs.draw_on_image(image_aug, size=0)
                print('save:',path)
                Image.fromarray(image_auged).save(path)

                # 存储变化后的XML
                save_aug_xml_file(SRC_XML_DIR, name[:-4], new_bndbox_list, AUG_XML_DIR,
                                           savefilebasename)
                #print(str("%06d" % (len(files) + int(name[:-4]) + epoch * 250)) + '.jpg')
                new_bndbox_list = []
      #生成txt文件
    labeltxtclas = getAllAnnnotations()

    labeltxtclas.convert_annotation(modelpath+'/augment')


if __name__ == "__main__":
    aug_config_file = open('aug_data_config.xml')
    AUGLOOP = 10
    for line in aug_config_file.readlines():
        if '#' not in line and len(line)>0:
            print(len(line))
            print('---',len(line), line.replace("\n","").split(':'))
            modelpath = line.replace("\n","").split(':')[0]
            AUGLOOP = line.replace("\n","").split(':')[1]
            print(modelpath,AUGLOOP)
            if os.path.isdir(modelpath):
                print('-------augment',modelpath)
                create_aug_data(modelpath,int(AUGLOOP))
    
 

