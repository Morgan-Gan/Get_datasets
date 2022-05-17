#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
import uuid
import argparse
import os
import datetime

req_url = "https://aim.360os.com//api/alarmImg/queryAlarmImgList"; ##公网地址
# req_url = "https://ism.jmc.com.cn/api/alarmImg/queryAlarmImgList";  ##江铃地址
# req_url = "https://hse-safety.cimc-containers.com/api/alarmImg/queryAlarmImgHistory";    
pagesize =20
path = "image"

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('-c', type=str, default = None)
parser.add_argument('-d', type=str, default = None)
parser.add_argument('-st', type=str, default = None)
parser.add_argument('-et', type=str, default = None)
parser.add_argument('-token', type=str, default = None) ##token
parser.add_argument('-at', type=str, default = None)##告警类型
parser.add_argument('-p', type=str, default = None) ##项目Id
parser.add_argument('-ims', type=str, default = None) ##图片状态 1表示正常，2表示有告警
args = parser.parse_args()

def post_req(url, data):
	req = requests.post(url,json=data)#发送post请求，第一个参数是URL，第二个参数是请求数据
	json_str = req.json()
	return json_str

def get_data(channel, device_id, start_time, end_time, token, alarm_type, project_id, img_state):
    print("开始下载图片...")
    data = req_data(channel, device_id, start_time, end_time,page_num=1,page_size=pagesize, token=token, alarm_type=alarm_type, project_id=project_id, img_state=img_state)
    json_data = json.dumps(data)
    result = json.loads(json_data)
    get_alarm(data)
    total = result['total']
    n_count = total // pagesize
    if n_count >= 1 :
        for i in range(2, n_count) :
            json_str = req_data(channel, device_id, start_time, end_time,page_num=i,page_size=pagesize, token=token, alarm_type=alarm_type, project_id=project_id, img_state=img_state)
            get_alarm(json_str)
        x_count = total % pagesize
        if x_count > 0 :
            json_str = req_data(channel, device_id, start_time, end_time,page_num=n_count+1,page_size=pagesize, token=token, alarm_type=alarm_type, project_id=project_id, img_state=img_state)
            get_alarm(json_str)
    print("下载图片完成！！！")

def get_alarm(json_str):
    print("json_str is:", json_str)
    json_data = json.dumps(json_str)
    result = json.loads(json_data)
    list1 = result['data']
    print("list1 is:", list1)
    if list1 is not None :
        save_img(list1)
    else :
        0

def save_img(alarm_data):
    # 遍历由json数据得到的list
    for alarm in alarm_data:
        try:
            img_url = alarm['imgUrl']
            print("img_url is: ", img_url)
            url_list = img_url.split(';')
            for url in url_list :
                uid = uuid.uuid4()
                print("img_name is: ", uid)
                urllib_download(url, uid)
        except Exception as e:
            pass
        continue

def urllib_download(img_url, name):
    from urllib.request import urlretrieve
    global path
    try:
        urlretrieve(img_url,  '%s/%s.png' %(path, name))
    except ZeroDivisionError as e:
        print('except:', e)

def req_data(channel, device_id, start_time, end_time, page_num, page_size, token, alarm_type, project_id, img_state):
    #调用函数
    data = {"companyId":1,"roleName": "root","channel": channel,"deviceId":device_id,"startTime": start_time,"endTime": end_time,"pageNum": page_num,"pageSize": page_size, "token":token, "alarmType":alarm_type, "projectId":project_id, "imgState":img_state};
    print("data is: ", data)
    json_str = post_req(req_url, data)
    # print("req_str is: ", json_str)
    return json_str


def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    is_exists = os.path.exists(path)

    # 判断结果
    if not is_exists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False

def main():
    global path
    dt = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    path = "image_"+dt
    mkdir(path)
    print("channel is: %s, deviceId is: %s, startTime is: %s, endTime is: %s, token is: %s, alarm_type is: %s" %(args.c, args.d, args.st, args.et, args.token, args.at))
    get_data(args.c, args.d, args.st, args.et, args.token, args.at, args.p, args.ims)

if __name__ == "__main__":
    main()