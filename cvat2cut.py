import cv2
import os
import json
import numpy as np

flags = []


def json2cut(trans, img_path, crop_img_dir):
    img = cv2.imread(img_path)
    with open(save_txt,'a') as ftxt:
        count = 0
        str2dict = eval(trans)
        for ch in str2dict: 
            # print(ch['transcription'])          
            # points = np.array(shape['points'])np.float32
            points = np.float32(ch['points'])
            label=str(ch['transcription'])
            print("-----------------> ", label)
            # print("------->", points)
            if label == '###':
                continue
            crop_img_name = img_path.split('/')[-1].split('.jpg')[0] + '_' + str(count) + '.png'
            crop_img_path = crop_img_dir + crop_img_name

            crop_img = get_rotate_crop_image(img, points, img_path)
            cv2.imwrite(crop_img_path, crop_img)
            count += 1
            # for m,n in xy:
            #     strxy+=str(m)+','+str(n)+','
            # strxy+=label 
            label_str = 'train/' + crop_img_name + '	' + label                                            
            ftxt.writelines(label_str+"\n") 

                # new_plot_img = img_path.replace("/images/", "/images_plot/")
    # cv2.imwrite(new_plot_img, img)          
 

def get_rotate_crop_image(img, points, path_json):
    '''
    img_height, img_width = img.shape[0:2]
    left = int(np.min(points[:, 0]))
    right = int(np.max(points[:, 0]))
    top = int(np.min(points[:, 1]))
    bottom = int(np.max(points[:, 1]))
    img_crop = img[top:bottom, left:right, :].copy()
    points[:, 0] = points[:, 0] - left
    points[:, 1] = points[:, 1] - top
    '''
    flags.append(abs(points[0][0] - points[3][0]))
    img_crop_width = int(
        max(
            np.linalg.norm(points[0] - points[1]),       #求向量、矩阵范数（默认二范数-》距离）
            np.linalg.norm(points[2] - points[3])))
    img_crop_height = int(
        max(
            np.linalg.norm(points[0] - points[3]),
            np.linalg.norm(points[1] - points[2])))

    pts_std = np.float32([[0, 0], [img_crop_width, 0],
                            [img_crop_width, img_crop_height],
                            [0, img_crop_height]])
    if points.shape[0] != 4:
        img_wrong = path_json.split('/')[-1]
        print("--------------------------------->{}".format(img_wrong))
        return img
    M = cv2.getPerspectiveTransform(points, pts_std)
    # try:
    #     print("----------------1-----------------> {}----{}".format(type(pts_std), type(points)))
    # except cv2.error as e:
    #     print("---------------------------------> {}----{}".format(type(pts_std), type(points)))
    dst_img = cv2.warpPerspective(                      #透视变换函数，保持直线不变形，但是平行线可能不再平行
        img,
        M, (img_crop_width, img_crop_height),
        borderMode=cv2.BORDER_REPLICATE,
        flags=cv2.INTER_CUBIC)
    # dst_img = img[int(points[0][0]): int(points[0][0])+img_crop_height, int(points[0][1]): int(points[0][1])+img_crop_width]
    dst_img_height, dst_img_width = dst_img.shape[0:2]
    if dst_img_height * 1.0 / dst_img_width >= 1.5:
        dst_img = np.rot90(dst_img)                    #矩阵逆时针旋转90°
    return dst_img



save_txt = './images/cvat_xml_label/labels/annotations1_rec.txt'
dir_txt = './images/cvat_xml_label/labels/annotations1.txt'
img_dir = './images/cvat_xml_label/images/'
crop_img_dir = './images/cvat_xml_label/images_output/'


if not os.path.exists(crop_img_dir) :
    os.makedirs(crop_img_dir)

with open(dir_txt, "r") as f:
    if f.readlines():
        f.seek(0)
        all_data = f.read().split('\n')
        for line in all_data:
            img_path = img_dir + line.split('\t')[0].split('/')[1]  
            transcription = line.split('\t')[1]
            print(img_path)
            # print(transcription)
            json2cut(transcription, img_path, crop_img_dir)





