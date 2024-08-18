import os

basePath = (f"{os.getcwd()}/stickman/")
newPath=basePath+"jump/"
for i in os.listdir(newPath):
    # if("frame" in i):
    #     newName=i.replace("frame","shoot")
    #     os.rename(newPath+i , newPath+newName)
    #     if("_delay-0.09s" in i):os.rename(newPath+newName , newPath+newName.replace("_delay-0.09s",""))

    if("_.jpg" in i):os.rename(newPath+i,newPath+i.replace("_.jpg",".jpg"))  