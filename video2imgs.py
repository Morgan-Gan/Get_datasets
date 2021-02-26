import cv2
import os
def save_img():
    video_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/jingdianmao/test'
    videos = os.listdir(video_path)
    for video_name in videos:
        file_name = video_name.split('_')[2].split('.')[0]
        folder_name = video_path.replace('test', 'test/images') + '/' + file_name
        os.makedirs(folder_name, exist_ok=True)
        vc = cv2.VideoCapture(video_path+'/'+video_name) 
        c=0
        timeF = 1                                             # 视频帧计数间隔频率
        rval=vc.isOpened()
 
        while rval:  
            c = c + 1                                              # 1
            rval, frame = vc.read()
            pic_path = folder_name+'/'
            if rval:
                if(c % timeF ==0):
                    cropped = frame                                    # frame[0:1080, 0:1500] # 裁剪坐标为[y0:y1, x0:x1]
                    cv2.imwrite(pic_path + str(c) + '.jpg', cropped)   # .png
                    cv2.waitKey(1)
                    print("It is saving {} fps".format(c))
            else:
                break
        vc.release()
        print('save_success')
        print(folder_name)
save_img()


###########################################  间隔帧保存视频，并合并到一个文件夹中##############################################

# def save_img():
#     video_path = '/home/window_share/home/os/window_share/ganhaiyang/datasets/gongxie/20210223gongxie_video'
#     videos = os.listdir(video_path)
#     for video_name in videos:
#         file_name = video_name.split('_')[2].split('.')[0]
#         folder_name = video_path.replace('20210223gongxie_video', '20210223gongxie_images1')          #+ '/'          # + file_name
#         os.makedirs(folder_name, exist_ok=True)
#         vc = cv2.VideoCapture(video_path+'/'+video_name) 
#         c=0
#         timeF = 15                                             # 视频帧计数间隔频率
#         rval=vc.isOpened()
 
#         while rval:  
#             c = c + 1                                              # 1
#             rval, frame = vc.read()
#             # pic_path = folder_name+'/'
#             if rval:
#                 if(c % timeF ==0):
#                     cropped = frame                                    # frame[0:1080, 0:1500] # 裁剪坐标为[y0:y1, x0:x1]
#                     cv2.imwrite(folder_name +  '/' + file_name + '_' +str(c) + '.jpg', cropped)   # .png
#                     cv2.waitKey(1)
#                     print("It is saving {} fps".format(c))
#             else:
#                 break
#         vc.release()
#         print('save_success')
#         print(folder_name)
# save_img()


