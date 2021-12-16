import os
import time
import re
class BatchRename():
 
  def __init__(self):
        self.labelsPath = '/home/window_share/home/os/window_share/common3/dataset/vehicle/muye_20210324/Four/labels'
            
  def checkData(self):
    labelFiles = os.listdir(self.labelsPath)

    rmNum = 0
    for item in labelFiles:
        rmNum = rmNum+1
        filepath = os.path.join(os.path.abspath(self.labelsPath), item)
        with open(filepath, 'r') as file_to_read:
            for line in file_to_read.readlines():
                lineChars = line.split()
                coordinates = lineChars[-4:]
                for coordinate in coordinates:
                    if(float(coordinate)==0.0):
                       print(item,":",line)


if __name__ == '__main__':
    demo = BatchRename()
    #demo.rename()
    demo.checkData()
