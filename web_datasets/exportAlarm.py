#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
import uuid
import argparse
import os
import datetime
import time

# req_url = "http://10.100.14.201/api/alarm/queryAlarmList";
req_url = "http://aim.360os.com/api/alarm/queryAlarmList";
pagesize =20
requests.DEFAULT_RETRIES = 100000000
path = "image"
request_count = 0


def post_req(url, data):
	req = requests.post(url,json=data)#发送post请求，第一个参数是URL，第二个参数是请求数据
	json_str = req.json()
	return json_str

def get_data(alarm_type, project_id, token, start_time, end_time, img_ori):
    if token is None:
        print("token is None")
        return
    print("开始下载图片...")
    data = req_data(alarm_type, project_id, token, start_time, end_time, page_num=1,page_size=pagesize)
    json_data = json.dumps(data)
    result = json.loads(json_data)
    total = result['total']
    print("total is: ", total)
    get_alarm(data, img_ori)
    n_count = total // pagesize
    if n_count >= 1 :
        for i in range(2, n_count) :
            json_str = req_data(alarm_type, project_id, token, start_time, end_time, page_num=i,page_size=pagesize)
            get_alarm(json_str, img_ori)
        x_count = total % pagesize
        if x_count > 0 :
            json_str = req_data(alarm_type, project_id, token, start_time, end_time, page_num=n_count+1,page_size=pagesize)
            get_alarm(json_str, img_ori)
    print("下载图片完成！！！")

def get_alarm(json_str, img_ori):
    json_data = json.dumps(json_str)
    result = json.loads(json_data)
    list1 = result['data']
    save_img(list1, img_ori)

def save_img(alarm_data, img_ori):
    # 遍历由json数据得到的list
    for alarm in alarm_data:
        try:
            img_url = alarm['alarmPicUrl']
            if len(img_url) == 1:
                continue;
            url_list = img_url.split(';')
            if img_ori == 1:
                if len(url_list) == 1:
                    url = url_list[0]
                    continue;
                else:
                    url = url_list[1]
                print("img_ori_url is: ",url);
                uid = uuid.uuid4()
                urllib_download(url, uid)
            elif img_ori == 2:
                url = url_list[0]
                print("img_frame_url is: ",url);
                uid = uuid.uuid4()
                urllib_download(url, uid)
            else:
                for url in url_list :
                    print("img_all_url is: ",url);
                    uid = uuid.uuid4()
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

def req_data(alarm_type, project_id, token, start_time, end_time, page_num, page_size):
    global request_count
    request_count = request_count+1
    print('----------------------request_count:',request_count)
    #调用函数
    #{"r":1614930110607,"nonce":18667,"uid":1,"sign":"d2c0daa2a37de36fd8cef9b16c45707f","token":"50ce6d18-553c-46ac-9c74-1c7ca75ff51b","roleName":"root","companyId":1,"pageNum":1,"pageSize":20,"alarmType":7}
    data = {"roleName": "root","alarmType": alarm_type, "companyId": 1, "token":token,"projectId":project_id, "startTime": start_time,"endTime": end_time,"pageNum": page_num,"pageSize": page_size};
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
    print("alarmType is: %s, projectId is: %s, token is: %s, startTime is: %s, endTime is: %s, ori is: %s" %(args.at, args.p, args.token, args.st, args.et, args.ori))
    get_data(args.at, args.p, args.token, args.st, args.et, args.ori)
    # get_data(1, 29, "50ce6d18-553c-46ac-9c74-1c7ca75ff51b", None, None, 1)

#if __name__ == "__main__":
#    main()

config_file='./config.txt'
pars_dict = {}


def get_args(config_file):
    if os.path.isfile(config_file):
        with open(config_file, 'r') as file_to_read:
            for line in file_to_read.readlines():
                if not line.startswith('#'):
                    key = line.split(':')[0]
                    value = line.split(':')[1].split()
                    pars_dict[key] = value

get_args(config_file)
print(pars_dict)
path = ''

for ai_type in pars_dict['at']:
    for p_id in pars_dict['p']:
        dt = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        print("------start-------------")
        path = "image_at"+ai_type+"_p"+p_id+"_dt"+dt;
        mkdir(path)
        #print("alarmType is: %s, projectId is: %s, token is: %s, startTime is: %s, endTime is: %s, ori is: %s" %(pars_dict['at'], pars_dict['p'], args.token, args.st, args.et, args.ori))
        print("args:")
        print("    alarmType is: %s"%ai_type)
        print("    projectId is: %s"%p_id)
        print("    token is: %s"%pars_dict['token'][0])
        print("    startTime is: %s"%pars_dict['st'][0])
        print("    endTime is: %s"%pars_dict['et'][0])
        print("    ori is: %s"%int(pars_dict['ori'][0]))
        get_data(ai_type, p_id, pars_dict['token'][0], pars_dict['st'][0], pars_dict['et'][0], int(pars_dict['ori'][0]) )
        #time.sleep(5)