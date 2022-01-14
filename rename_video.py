import glob,shutil
num = 0
for f in glob.glob("*.mp4"):
    num += 1
    shutil.move(f, "ZI" + "_houdianji_" + str(num)  + ".mp4")
