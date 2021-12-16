import os

class BatchRename():

    def __init__(self):
        self.labelsPath = 'Annotations'
        self.imagesPath = 'JPEGImages'

    def getFileNames(self, path):
        filelist = os.listdir(path)
        fileName = []
        for item in filelist:
            index = item.rfind('.')
            name = item[:index]
            fileName.append(name)
        return fileName
            
    def removeUnlableImages(self):
        #标注文件名
        lablesNames = self.getFileNames(self.labelsPath)
        if(len(lablesNames)==0):
            print("no label file!!!")
            return 
        #图片文件名
        imagesNames = self.getFileNames(self.imagesPath)
        #图片文件
        imagesFiles = os.listdir(self.imagesPath)
        rmNum = 0
        for item in imagesNames:
            #如果图片，没有被标注
            if(item not in lablesNames):
                fileName = item + '.png'
                notlabelFile = os.path.join(os.path.abspath(self.imagesPath), fileName)
                #print(os.path.exists(notlabelFile))
                try:
                    os.remove(notlabelFile)
                    print('remove %s ' % (notlabelFile))
                    rmNum = rmNum + 1
                except:
                   print('remove exception :%s ' % (notlabelFile))
                   continue
        print("remove unlabeled image num: %d" %(rmNum))

    def removeInvalidImages(self):
        img_list = os.listdir(self.imagesPath)
        rmNum = 0
        for img in img_list:
            if not img[img.rfind('.')+1 : ] in ['jpg', 'png']:
                rmNum = rmNum + 1
                print('invalid image below will be removed')
                print(img)
                os.remove('JPEGImages/%s'%(img))
        print('remove invalid image num : %d'%(rmNum))

if __name__ == '__main__':
    demo = BatchRename()
    demo.removeInvalidImages()
    demo.removeUnlableImages()