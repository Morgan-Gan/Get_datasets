# from bs4 import BeautifulSoup
# import requests
 
# def download(img_url,headers,n):
#     req = requests.get(img_url, headers=headers)
#     name = '%s'%n+'='+img_url[-15:]
#     path = 'Elec_Cap'
#     file_name = path + '/' + name
#     f = open(file_name, 'wb')
#     f.write(req.content)
#     f.close
 
# def parses_picture(url,headers,n):
#     url = r'http://desk.zol.com.cn/' + url
#     img_req = requests.get(url, headers=headers)
#     img_req.encoding = 'gb2312'
#     html = img_req.text
#     bf = BeautifulSoup(html, 'lxml')
#     try:
#         img_url = bf.find('div', class_='photo').find('img').get('src')
#         download(img_url,headers,n)
#         url1 = bf.find('div',id='photo-next').a.get('href')
#         parses_picture(url1,headers,n)
#     except:
#         print(u'第%s图片集到头了'%n)
 
# if __name__=='__main__':
#     url='http://desk.zol.com.cn/dongman/huoyingrenzhe/'
#     headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
#     req = requests.get(url=url, headers=headers)
#     req=requests.get(url=url,headers=headers)
#     req.encoding = 'gb2312'
#     html=req.text
#     bf=BeautifulSoup(html,'lxml')
#     targets_url=bf.find_all('li',class_='photo-list-padding')
#     n=1
#     for each in targets_url:
#         url = each.a.get('href')
#         parses_picture(url,headers,n)
#         n=n+1




# import re
# import requests
# from urllib import error
# from bs4 import BeautifulSoup
# import os

# num = 0
# numPicture = 0
# file = './test'
# List = []


# def Find(url):
#     global List
#     print('正在检测图片总数，请稍等.....')
#     t = 0
#     i = 1
#     s = 0
#     while t < 100:
#         Url = url + str(t)
#         try:
#             Result = requests.get(Url, timeout=7) #超时设置-136  timeout=7
#         except BaseException:
#             t = t + 60 #向后滑动60个图-一页60个图
#             continue
#         else:
#             result = Result.text
#             pic_url = re.findall('"objURL":"(.*?)",', result, re.S)  # 先利用正则表达式找到图片url-147
#             s += len(pic_url)
#             # print(s)
#             if len(pic_url) == 0:
#                 break
#             else:
#                 List.append(pic_url)
#                 t = t + 60


#     print(s)
#     return s


# def recommend(url):
#     Re = []
#     try:
#         html = requests.get(url)
#     except error.HTTPError as e:
#         return
#     else:
#         html.encoding = 'utf-8'
#         bsObj = BeautifulSoup(html.text, 'html.parser')
#         # print(bsObj)
#         div = bsObj.find('div', id='topRS') #定位
#         if div is not None:
#             listA = div.findAll('a')#定位a标签
#             for i in listA:
#                 if i is not None:
#                     Re.append(i.get_text())#取出标签内的推荐标题放入列表中
#         return Re


# def dowmloadPicture(html, keyword):
#     global num
#     # t =0
#     pic_url = re.findall('"objURL":"(.*?)",', html, re.S)  # 先利用正则表达式找到图片url
#     # print(pic_url)
#     print('找到关键词:' + keyword + '的图片，即将开始下载图片...')
#     for each in pic_url:
#         print('正在下载第' + str(num + 1) + '张图片，图片地址:' + str(each))
#         try:
#             if each is not None:
#                 pic = requests.get(each, timeout=7)
#             else:
#                 continue
#         except BaseException:
#             print('错误，当前图片无法下载')
#             continue
#         else:
#             string = file + r'/' + keyword + '_' + str(num) + '.jpg'
#             fp = open(string, 'wb')
#             fp.write(pic.content)#-125-content是二进制形式（text打印的是str形式）
#             fp.close()
#             num += 1
#         if num >= numPicture: #控制下载的图片数
#             return


# if __name__ == '__main__':  # 主函数入口
#     word = input("请输入搜索关键词(可以是人名，地名等): ")
#     # add = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E5%BC%A0%E5%A4%A9%E7%88%B1&pn=120'
#     url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&pn='
#     print(url)
#     tot = Find(url)
#     Recommend = recommend(url)  # 记录相关推荐
#     print('经过检测%s类图片共有%d张' % (word, tot))
#     numPicture = int(input('请输入想要下载的图片数量 '))
#     file = input('请建立一个存储图片的文件夹，输入文件夹名称即可')
#     y = os.path.exists(file)
#     if y == 1:
#         print('该文件已存在，请重新输入')
#         file = input('请建立一个存储图片的文件夹，)输入文件夹名称即可')
#         os.mkdir(file)
#     else:
#         os.mkdir(file)
#     t = 0
#     tmp = url
#     while t < numPicture:
#         try:
#             url = tmp + str(t)
#             result = requests.get(url, timeout=10) #超时设置
#             # print(url)
#         except error.HTTPError as e:
#             print('网络错误，请调整网络后重试')
#             t = t + 60
#         else:
#             dowmloadPicture(result.text, word)
#             t = t + 60

#     print('当前搜索结束，感谢使用')
#     print('猜你喜欢')
#     for re in Recommend:
#         print(re, end='  ')

# _*_ coding:utf-8 _*_

from tkinter import *
import requests
import re
import os
from urllib import parse
from urllib import request
from urllib.request import urlretrieve
# from bs4 import BeautifulSoup
import tkinter as tk
# 定义一个gui界面显示
# 显示图像框

os.environ['DISPLAY'] = 'localhost:27.0'

def main():
    running = 1
    global url_input,text,sshow
    # 创建空白窗口,作为主载体
    root = Tk()
    root.title('爬取数据')
    # 窗口的大小，后面的加号是窗口在整个屏幕的位置
    root.geometry('550x400+398+279')
    # 标签控件，窗口中放置文本组件
    Label(root,text='请输入关键词:',font=("华文行楷",20)).grid()
    # 定位 pack包 place位置 grid是网格式的布局
    url_input = Entry(root,font=("华文行楷",20))
    url_input.grid(row=0,column=1)
    # 输入
    #text = Listbox(root,font=('华文行楷',20),width=45,height=10)
    text = tk.Text(root, font=('华文行楷', 20), width=45, height=10)
    # columnspan 组件所跨越的列数
    text.grid(row=1,columnspan=2)
# 爬虫函数，爬取关键字的内容
# 定义一个爬虫函数
    def get_picture():
        word = '静电帽'                                             #url_input.get()
        url = ('https://image.baidu.com/search/acjson?'
               'tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&'
               'queryWord={word}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&'
               'word={word}&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&fr=&'
               'pn={pn}&rn=30&gsm=5a&1516945650575=')
        pattern = '"thumbURL":"(.+?\.jpg)"'
        def geturls(num, word):
            word = parse.quote(word)
            urls = []
            # pn = (num // 30 + 1) * 30
            pn = 9000
            # for i in range(30, pn + 1, 30):
            # for i in range(30, 9000, 30):
            for i in range(30, 9000, 10):
                urls.append(url.format(word=word, pn=i))
                # print(word)
            return urls
        def getimgs(num, urls):
            imgs = []
            reg = re.compile(pattern)
            for url in urls:
                page = request.urlopen(url)
                code = page.read()
                code = code.decode('utf-8')
                imgs.extend(reg.findall(code))
                # print(code)
            return imgs
# 获取url,设置存放图片的位置
        word = url_input.get()     # 输入关键字进行搜索
        num = 9000                # 最多打印100张图片
        path = 'test'     # 图片存贮的路径
        # 判断图片保存路径是否存在，不存在就创建
        if not os.path.exists(path):
            os.mkdir(path)
            print('路径不存在，但已新建')
        # 进入百度图片搜索网页，搜索关键字，获取num整除30页图片搜索页面的地址列表
        urls = geturls(num, '静电帽')  # 百度搜索页面地址    ## word
        # 打开urls列表中的url，用正则表达式搜索以.jpg结尾的图片源地址url，保存到imgs列表中，imgs中的url是30的倍数
        imgs = getimgs(num, urls)  # 图片地址
# 获取图片，保存图片
        i = 0  # 下载序号
        j = 0  # 请求超时数量
        for img in imgs:
            i += 1
            try:
                request.urlretrieve(img, path + '/' + '%s.jpg' % (i - j))  # 将图片下载到指定目录
            except OSError as err:  # 下载超时处理
                print('下载第%s图片时请求超时，已跳过该图片' % (i - j))

            else:
                # stri =  print('成功下载第' + str(i - j) + '张图片')
                sshow= '成功下载第' + str(i - j) + '张图片'
                print(sshow)
                text.insert(END,sshow+'\n')           # 在gui界面中动态显示下载的图片数量
                text.see(END)                         # 更新每次打印
                # 更新
                text.update()
                if (i - j) >= num:  # 判断是不是下载量达到指定数量
                    print('下载图片完毕，成功下载%d张照片，跳过%d张照片' % ((i - j), j))
                    break

# 设置按钮 sticky对齐方式，N S W E
    button =Button(root,text='开始下载',font=("华文行楷",15),command=get_picture).grid(row=2,column=0,sticky=W)
    button =Button(root,text='退出',font=("华文行楷",15),command=root.quit).grid(row=2,column=1,sticky=E)
    if running == 1:
       root.mainloop()
if __name__ == '__main__':
    main()

