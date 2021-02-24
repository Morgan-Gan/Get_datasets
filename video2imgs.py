import cv2
import os
def save_img():
    video_path = 'E:\\2021-02-05video'
    videos = os.listdir(video_path)
    for video_name in videos:
        file_name = video_name.split('_')[2].split('.')[0]
        folder_name = video_path.replace('video', 'imgs') + '\\' + file_name
        os.makedirs(folder_name, exist_ok=True)
        vc = cv2.VideoCapture(video_path+'/'+video_name) 
        c=0
        rval=vc.isOpened()
 
        while rval:  
            c = c + 1
            rval, frame = vc.read()
            pic_path = folder_name+'/'
            if rval:
                cropped = frame[0:1080, 0:1500] # 裁剪坐标为[y0:y1, x0:x1]
                cv2.imwrite(pic_path + str(c) + '.jpg', cropped)   # .png
                cv2.waitKey(1)
                print("It is saving {} fps".format(c))
            else:
                break
        vc.release()
        print('save_success')
        print(folder_name)
save_img()


