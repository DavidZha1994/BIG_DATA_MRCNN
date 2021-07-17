import os
import shutil

# 获取当前目录下所有文件及目录
listDir = os.listdir()

# 遍历
for dir in listDir:
    # 判断如果是文件夹或是自己则忽略
    if os.path.isdir(dir) or 'make folder.py' == dir:
        continue
    # 分离文件名和扩展名,获取不带后缀的文件名
    dirName = os.path.join(os.path.splitext(dir)[0] , "images")
    # 判断是否存在同名目录，
    # 不存在则将创建此目录，将同名文件移动到目录，
    # 存在则直接移动到此目录
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    shutil.move(dir, dirName)
