import  os
import cv2

yolo_txt = r"/home/window_share/home/os/window_share/ganhaiyang/datasets/head_hand_foot/20210305shoes/detection_result"

output_path = r"/home/window_share/home/os/window_share/ganhaiyang/datasets/head_hand_foot/20210305shoes/norm_hand_labels"
os.makedirs(output_path, exist_ok=True)
image_path = r"/home/window_share/home/os/window_share/ganhaiyang/datasets/head_hand_foot/20210305shoes/JPEGImages"

yolo_list = os.listdir(yolo_txt)

# class_name = ["person","ele_cap","protection_shoes", "shoes"]
class_name = ["hand"]

for txt in yolo_list:
    txt_path = os.path.join(yolo_txt,txt)
    output_txt_path = os.path.join(output_path,txt)
    image_read_path = os.path.join(image_path,txt.split(".txt")[0]+".jpg")

    read_handle = open(txt_path,"r")
    write_handle = open(output_txt_path,"w")

    if os.path.exists(image_read_path):
        pass
    else:
        image_read_path = image_read_path.replace(".jpg",".JPG")
    print(image_read_path)
    h,w,_ = cv2.imread(image_read_path).shape
    for content in read_handle:
        if "\t" in content:
            content = content.replace("\t"," ")
        content_list = content.split(" ")
        # print()
        dw = 1. / w
        dh = 1. / h
        # name = class_name[int(content_list[0])]

        # ## xyxy -> yolo normal(xywh)
        # name = int(content_list[0])
        name = 1
        # center_x = float(int(content_list[1]) + int(content_list[3]))*dw/2
        # center_y = float(int(content_list[2]) + int(content_list[4]))*dh/2
        # box_w = float(abs(int(content_list[3]) - int(content_list[1])))*dw
        # box_h = float(abs(int(content_list[4]) - int(content_list[2])))*dh
        center_x = float(int(content_list[3]) + int(content_list[5]))*dw/2
        center_y = float(int(content_list[4]) + int(content_list[6]))*dh/2
        box_w = float(abs(int(content_list[5]) - int(content_list[3])))*dw
        box_h = float(abs(int(content_list[6]) - int(content_list[4])))*dh

        # top_x = float(int(content_list[1]))*w - float(int(content_list[3]))*w/2
        # top_y = float(int(content_list[2]))*h - float(int(content_list[4][:-3]))*h/2
        # bot_x = float(int(content_list[1]))*w + float(int(content_list[3]))*w/2
        # bot_y = float(int(content_list[2]))*h + float(int(content_list[4][:-3]))*h/2

        # yolo normal(xywh) -> xyxy
        # bbox_width = float(content_list[3]) * w
        # bbox_height = float(content_list[4]) * h
        # center_x = float(content_list[1]) * w
        # center_y = float(content_list[2]) * h
        # top_x = center_x - (bbox_width / 2)
        # top_y = center_y - (bbox_height / 2)
        # bot_x = center_x + (bbox_width / 2)
        # bot_y = center_y + (bbox_height / 2)

        write_handle.write(str(name) +" "+str(center_x)+" "+str(center_y)+" "+str(box_w)+" "+str(box_h)+"\n")
        # write_handle.write(name+" "+str(int(top_x))+" "+str(int(top_y))+" "+str(int(bot_x))+" "+str(int(bot_y))+"\n")
    write_handle.close()