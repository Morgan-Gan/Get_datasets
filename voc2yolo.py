import cv2
import os
import xml.etree.ElementTree as ET


def xml_txt(txt_path, image_path, path, labels):
	cnt = 0
	# 遍历图片文件夹
	for (root, dirname, files) in os.walk(image_path):
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
			# 解析xml
			tree = ET.parse(xml_path)
			root = tree.getroot()
			# 获取weight,height
			size = root.find('size')
			w = size.find('width').text
			h = size.find('height').text
			dw = 1/int(w)
			dh = 1/int(h)
			# 初始化line
			line = ''
			for item in root.findall('object'):
				# 提取label,并获取索引
				label = item.find('name').text
				label = labels.index(label)
				# 提取信息labels, x, y, w, h 
				# 多框转化
				for box in item.findall('bndbox'):
					xmin = float(box.find('xmin').text)
					ymin = float(box.find('ymin').text)
					xmax = float(box.find('xmax').text)
					ymax = float(box.find('ymax').text)
					print(xmin,ymin,xmax,ymax)

					# x, y, w, h归一化
					center_x = ((xmin + xmax) / 2) * dw
					center_y = ((ymin + ymax) / 2) * dh
					bbox_width = (xmax-xmin) * dw
					bbox_height = (ymax-ymin) * dh
					print(center_x,center_y,bbox_width,bbox_height)
                    
                    # 传入信息，txt是字符串形式
					line += '{} {} {} {} {}'.format(label,center_x,center_y,bbox_width,bbox_height) + '\n'              
			
			# 将txt信息写入文件
			with open(ftxt_path, 'w') as f_txt:
				f_txt.write(line)
			cnt += 1
			print('文件数量：', cnt)

if __name__ == '__main__':
    # filespath = os.getcwd()
    txt_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/ele_cap_protection_shoes_4cls/4cls/augment/labels'             # os.path.join(filespath, 'txt')  # yolo存放生成txt的文件目录
    image_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/ele_cap_protection_shoes_4cls/4cls/augment/JPEGImages'                     #os.path.join(filespath, 'image')  # 存放图片的文件目录
    path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/ele_cap_protection_shoes_4cls/4cls/augment/Annotations'          #os.path.join(filespath, 'xml')  # 存放xml的文件目录

    labels = ['person', 'ele_cap', 'protection_shoes', 'shoes']  # 用于获取label位置
    xml_txt(txt_path, image_path, path, labels)







# annot_path = "/home/window_share/home/os/window_share/ganhaiyang/datasets/head_hand_foot/20210305head_hand_foot/head_hand_foot/augment/Annotations"
# img_path = "/home/window_share/home/os/window_share/ganhaiyang/datasets/head_hand_foot/20210305head_hand_foot/head_hand_foot/augment/JPEGImages"

