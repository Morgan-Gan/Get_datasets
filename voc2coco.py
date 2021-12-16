import numpy as np
import xml.dom.minidom as minidom
import json
import os

# config params
classes = ['nothat', 'wearhat', 'cap']
traintxt = './2020_train.txt'
valtxt = './2020_val.txt'


def getclsIndex(class_input):
    for i, cls in enumerate(classes):
        if cls == class_input:
            return i


def readxml(files, outfile):
    categories = []

    for i, cls in enumerate(classes):
        caterory = {}
        caterory['supercategory'] = 'humen'
        caterory['id'] = i
        caterory['name'] = cls
        categories.append(caterory)

    m_image_id = 0
    m_annotation_id = 0
    images = []
    annotations = []

    for file in files:
        if os.path.isdir(file):
            continue
        dom = minidom.parse(file)
        root = dom.documentElement
        m_width = 0
        m_height = 0
        m_type = ''
        m_x1 = 0
        m_x2 = 0
        m_y1 = 0
        m_y2 = 0
        m_filename = file.split("/")[-1][0:-4] + '.jpg'
        m_id = m_image_id
        m_image_id += 1

        sizes = root.getElementsByTagName('size')
        for size in sizes:
            widths = size.getElementsByTagName('width')
            for width in widths:
                m_width = int(width.childNodes[0].data)

            heights = size.getElementsByTagName('height')
            for height in heights:
                m_height = int(height.childNodes[0].data)

        temp_image = {}
        temp_image['file_name'] = m_filename
        temp_image['width'] = m_width
        temp_image['height'] = m_height
        temp_image['id'] = m_id
        images.append(temp_image)

        objects = root.getElementsByTagName('object')
        for obj in objects:
            names = obj.getElementsByTagName('name')
            for name in names:
                m_type = name.childNodes[0].data
                if m_type not in classes:
                    if m_type == "person":
                        m_type = "nothat"
                    elif m_type == "hat":
                        m_type = "wearhat"

            bndboxs = obj.getElementsByTagName('bndbox')
            for banbox in bndboxs:
                xmins = banbox.getElementsByTagName('xmin')
                for xmin in xmins:
                    m_x1 = int(xmin.childNodes[0].data)
                    # print(xmin.childNodes[0].data)

                ymins = banbox.getElementsByTagName('ymin')
                for ymin in ymins:
                    m_y1 = int(ymin.childNodes[0].data)
                    # print(ymin.childNodes[0].data)

                xmaxs = banbox.getElementsByTagName('xmax')
                for xmax in xmaxs:
                    m_x2 = int(xmax.childNodes[0].data)
                    # print(xmax.childNodes[0].data)

                ymaxs = banbox.getElementsByTagName('ymax')
                for ymax in ymaxs:
                    m_y2 = int(ymax.childNodes[0].data)
                    # print(ymax.childNodes[0].data)

            annotation = {}
            annotation['area'] = (m_x2-m_x1)*(m_y2-m_y1)
            annotation['bbox'] = [m_x1, m_y1, m_x2-m_x1, m_y2-m_y1]
            annotation['category_id'] = getclsIndex(m_type)
            annotation['id'] = m_annotation_id
            annotation['image_id'] = m_id
            annotation['iscrowd'] = 0
            annotation['segmentation'] = [[]]
            annotations.append(annotation)
            m_annotation_id += 1

    f = open('./json/instances_val2019_rotate_real_12.json', encoding='utf-8')
    root = json.load(f)
    info = root.get('info')
    licenses = root.get('licenses')

    root2 = {}
    root2['info'] = info
    root2['licenses'] = licenses
    root2['categories'] = categories
    root2['images'] = images
    root2['annotations'] = annotations

    # res = json.dumps(root2)
    res = json.dumps(root2, sort_keys=True, indent=4, separators=(',', ': '))

    with open(outfile.replace("json", "txt"), 'w') as f:
        f.write(res)

    os.rename(outfile.replace("json", "txt"), outfile)


def readtxt(path, outfile):
    files = []
    with open(path, "r") as f:
        for line in f.readlines():
            line = line.strip('\n')
            line = line.split('/')
            length = len(line)
            file = './Annotations'+'/'+line[length-1].split('.')[0]+'.xml'
            files.append(file)

    readxml(files, outfile)


if __name__ == '__main__':
    readtxt(traintxt, './coco/annotations/instances_train2019.json')
    # readtxt(testtxt, './json/instances_test2019.json')
    readtxt(valtxt, './coco/annotations/instances_val2019.json')
