import requests
import os
cookie='''BIDUPSID=1341253689A1CBC130634374C8C6A500; PSTM=1600409916; BAIDUID=1341253689A1CBC142E54AC60908BCEB:FG=1; BDUSS=GJRaUtvUTVjRGo2THZESHpSTFYwNmlMS2N0Vi1HUGZDTDd4amIwNDBRb09PY2RmSVFBQUFBJCQAAAAAAAAAAAEAAABWFws60rvWsdK7uPbIy7zFxK8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA6sn18OrJ9fV; BDUSS_BFESS=GJRaUtvUTVjRGo2THZESHpSTFYwNmlMS2N0Vi1HUGZDTDd4amIwNDBRb09PY2RmSVFBQUFBJCQAAAAAAAAAAAEAAABWFws60rvWsdK7uPbIy7zFxK8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA6sn18OrJ9fV; MCITY=-340%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=1BF6D35D11A04F444A3C87A7B7EEC0BD:FG=1; delPer=0; PSINO=6; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; BDRCVFR[tox4WRQ4-Km]=mk3SLVN4HKm; BDRCVFR[CLK3Lyfkr9D]=mk3SLVN4HKm; ZD_ENTRY=baidu; userFrom=www.baidu.com; BCLID=9142563430683625100; BDSFRCVID=eT0OJeC62iv736TrdhA8hbFbFgKlvH5TH6bHef_bL42ScgDnbzG6EG0PSx8g0KubrpbhogKK3gOTH4PF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=tbCjVIDafC_3J4jTq4TJhJLy-fIX5-Cs5GPj2hcH0KLKjtL6DTjxK40JLH735f5a3DviWPQdJxb1MRoSbtjr-x73DRb2KM3XKjQx_q5TtUJ6JKnTDMRh-RDQ-x7yKMnitKv9-pP2LpQrh459XP68bTkA5bjZKxtq3mkjbPbDfn02eCKu-n5jHjo3DHt83J; H_PS_PSSID=1464_33102_33259_31254_33285_33286_33198_33237_33147_33267; BA_HECTOR=0l0l80848la48k0ler1ftgsug0q; ab_sr=1.0.0_MmM1NzY5OWE5MjA2YzVmZGExZjc2OGQxYzMxNjYwODg2Y2E3NjBmMjk1NGU2Y2NmMzEwOWVhM2NkZDc0ZDgyNzAzMjAyZWU5ZjI0NzE1NjVjMmEyOTAxOTYxMzE4OTVmOWQ3ZjJiZTY0ZTkyNWJjNTAxYzg3NTY4MGU2Nzc4YmM='''
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
          'Connection':'keep-alive',
          'accept':'*/*',
          'Cookie':cookie}

def getManyPages(keyword, pages):
    params = []
    for i in range(30, 30 * pages + 30, 30):
        params.append({
            'tn': 'resultjson_com',
            'ipn': 'rj',
            'ct': 201326592,
            'is': '',
            'fp': 'result',
            'queryWord': keyword,
            'cl': 2,
            'lm': -1,
            'ie': 'utf-8',
            'oe': 'utf-8',
            'adpicid': '',
            'st': -1,
            'z': '',
            'ic': 0,
            'word': keyword,
            's': '',
            'se': '',
            'tab': '',
            'width': '',
            'height': '',
            'face': 0,
            'istype': 2,
            'qc': '',
            'nc': 1,
            'fr': '',
            'pn': i,
            'rn': 30,
            'gsm': '1e',
            '1488942260214': ''
        })
    url = 'https://image.baidu.com/search/acjson'
  #  url = 'https://image.baidu.com/'
    urls = []
    for i in params:
        urls.append(requests.get(url, params=i,headers=header,allow_redirects=False).json().get('data'))
    return urls


def getImg(dataList, localPath):
    if not os.path.exists(localPath):  # 新建文件夹
        os.mkdir(localPath)
    x = 0

    for list in dataList:

        for i in list:

            if i.get('thumbURL') != None:
                print('正在下载中：%s' % i.get('thumbURL'))
                ir = requests.get(i.get('thumbURL'))
                open(localPath + '%d.jpg' % x, 'wb').write(ir.content)
                x += 1

            else:
                print('该图片链接不存在')

if __name__ == '__main__':
    dataList = getManyPages('监控视频', 5000)  # 参数1:关键字，参数2:要下载的页数     #监控视频  #办公区

    # getImg(dataList, 'E:\lishen\project\somecode\patu-python\knife\meigong')   # 参数2:指定保存的路径
    getImg(dataList, '/home/os/window_share/ganhaiyang/datasets/person')   # 参数2:指定保存的路径