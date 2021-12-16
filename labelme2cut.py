import cv2
import os
import json
import numpy as np

flags = []
def json2txt(path_json,path_txt):
    with open(path_json,'r') as path_json:
        jsonx=json.load(path_json)
        with open(path_txt,'w+') as ftxt: 
            for shape in jsonx['shapes']:           
                xy=np.array(shape['points'])
                label=str(shape['label'])
                strxy = ''
                for m,n in xy:
                    strxy+=str(m)+','+str(n)+','
                strxy+=label                                            
                ftxt.writelines(strxy+"\n")  

def json2cut(path_json, img_path, crop_img_dir):
    img = cv2.imread(img_path)
    with open(path_json,'r') as path_json:
        jsonx=json.load(path_json)
        path_txt = dir_txt + 'rec_gt_val.txt'
        with open(path_txt,'a') as ftxt:
            count = 0
            for shape in jsonx['shapes']:           
                # points = np.array(shape['points'])np.float32
                points = np.float32(shape['points'])
                label=str(shape['label'])
                if label == '###':
                    continue
                crop_img_name = img_path.split('/')[-1].split('.jpg')[0] + '_' + str(count) + '.png'
                crop_img_path = crop_img_dir + crop_img_name
                # img = cv2.imread(img_path)
                
                # # 四点画图
                # cv2.circle(img, (int(points[0][0]),int(points[0][1])), 5, (0, 0, 255), 4)  #纯蓝
                # cv2.circle(img, (int(points[1][0]),int(points[1][1])), 5, (0, 255, 0), 4)  #绿色
                # cv2.circle(img, (int(points[2][0]),int(points[2][1])), 5, (0, 255, 255), 4) #青色
                # cv2.circle(img, (int(points[3][0]),int(points[3][1])), 5, (255,140,0), 4)   #橙色


                crop_img = get_rotate_crop_image(img, points, img_path)
                # print("---------------------------->", flags[0])
                # if flags[0] > 50:
                #     print("------------------------------------------------>", crop_img_name)
                # flags.clear()
                # img_id = img_id + str(count) +'.jpg'
                cv2.imwrite(crop_img_path, crop_img)
                count += 1
                # for m,n in xy:
                #     strxy+=str(m)+','+str(n)+','
                # strxy+=label 
                label_str = 'train/' + crop_img_name + '	' + label                                            
                ftxt.writelines(label_str+"\n") 

                new_plot_img = img_path.replace("/images/", "/images_plot/")
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

    # print("---------------------------->", abs(points[0][0] - points[3][0]))
    # if abs(points[0][0] - points[3][0] )> 50:
    #     img_crop_width = int(
    #     max(
    #         np.linalg.norm(points[0] - points[3]),       #求向量、矩阵范数（默认二范数-》距离）
    #         np.linalg.norm(points[2] - points[1])))
    #     img_crop_height = int(
    #         max(
    #             np.linalg.norm(points[0] - points[1]),
    #             np.linalg.norm(points[3] - points[2])))
    #     points10, points11 = points[3][0], points[3][1]

    #     points30, points31 = points[1][0], points[1][1]
    #     points[1][0], points[1][1] = points10, points11
    #     points[3][0], points[3][1] = points30, points31
    # else:
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



dir_json = '/home/os/window_share/common3/dataset/ocr/cimc/20211201containers/labels_val/'
dir_txt = '/home/os/window_share/common3/dataset/ocr/cimc/20211201containers/'
img_dir = '/home/os/window_share/common3/dataset/ocr/cimc/20211201containers/20211201containers_val/'
crop_img_dir = '/home/os/window_share/common3/dataset/ocr/cimc/20211201containers/images_val_output/'

if not os.path.exists(dir_txt) :
    os.makedirs(dir_txt)
if not os.path.exists(crop_img_dir) :
    os.makedirs(crop_img_dir)

list_json = os.listdir(dir_json)
for cnt,json_name in enumerate(list_json):
    # print('cnt=%d,name=%s'%(cnt,json_name))
    path_json = dir_json + json_name
    # path_txt = dir_txt + json_name.replace('.json','.txt')
    # path_txt = dir_txt + 'img_test.txt'
    img_path = os.path.join(img_dir, json_name.replace('.json','.jpg'))
    #print(path_json,path_txt)    
    # json2txt(path_json,path_txt)
    json2cut(path_json, img_path, crop_img_dir)



