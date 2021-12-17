import cv2
import os
import xml.etree.ElementTree as ET


def xml_txt(txt_path, path):
    cnt = 0
    # 遍历图片文件夹
    for (root, dirname, files) in os.walk(path):
        print(root,dirname,files)
        # 获取图片名
        for ft in files:
            # ft是图片名字+扩展名，替换txt,xml格式
            ftxt = ft.replace(ft.split('.')[1], 'txt')
            fxml = ft.replace(ft.split('.')[1], 'xml')
            # xml文件路径
            xml_path = os.path.join(path, fxml)
            # txt文件路径
            ftxt_path = os.path.join(txt_path, ftxt)
            # 解析xml,返回根元素tree.(一级节点Annotation)
            tree = ET.parse(xml_path)
            root = tree.getroot()

            # 对tree进行findall操作，可到带有指定标签节点（二级节点：filename, object)
            for item in root.findall('image'):
                list_target = []
                write_flag = True
                # 提取label,并获取索引
                img_name = item.attrib["name"]      # .attrib获取标签中的属性和属性值
                print(img_name)

                if item.findall('polygon'):
                    for poly in item.findall('polygon'):
                        # 提取label,并获取索引
                        points = poly.attrib["points"]
                        # print(points)

                        dict02 = {}
                        label = poly.find('attribute').text
                        if label is None:
                           write_flag = False
                        dict02['transcription'] = label 
                        points = points.replace(',', ';').split(";")
                        list04 = []
                        for j in range(0, len(points), 2):
                            list04.append([float(points[j]), float(points[j+1])])
                        dict02['points'] = list04
                        list_target.append(dict02)

                    target_str = str(list_target)
                    target_str = target_str.replace("'", "\"")
                    print(target_str)
                    
                        # 传入信息，txt是字符串形式
                        # line += '{} {} {} {} {}'.format(label,center_x,center_y,bbox_width,bbox_height) + '\n'              
                
                    # 将txt信息写入文件
                    if write_flag:
                        with open(ftxt_path, 'a') as f_txt:
                            f_txt.write('20211201containers_train/' + img_name + '\t')
                            f_txt.write(target_str + '\n')
                        cnt += 1
                        print('文件数量：', cnt)
                else:
                    continue
        f_txt.close()

if __name__ == '__main__':
    # filespath = os.getcwd()
    txt_path = 'images/cvat_xml_label/labels'             # os.path.join(filespath, 'txt')  # yolo存放生成txt的文件目录
    path = 'images/cvat_xml_label/xml'          #os.path.join(filespath, 'xml')  # 存放xml的文件目录
    xml_txt(txt_path, path)







# annot_path = "/home/window_share/home/os/window_share/ganhaiyang/datasets/head_hand_foot/20210305head_hand_foot/head_hand_foot/augment/Annotations"
# img_path = "/home/window_share/home/os/window_share/ganhaiyang/datasets/head_hand_foot/20210305head_hand_foot/head_hand_foot/augment/JPEGImages"

