import os
import sys
import shutil

dr = r'C:\Users\sa-u\OneDrive - rub.de\RUB\Semester_2\Big Data in der Bioinformatik\Mask_RCNN-master\path\cell\stage1_train'

def path(*args):
    return os.path.join(*args)

for d in os.listdir(dr):
    try:
        if not os.listdir(path(dr, d, "mask")):
            shutil.rmtree(path(dr,d))
        
    except FileNotFoundError:
        shutil.rmtree(path(dr,d))
    except NotADirectoryError:
        pass

    
    
for d in os.listdir(dr):
    try:
        if os.listdir(path(dr, d, "position_chunk")):
            shutil.rmtree(path(dr,d+'\\position_chunk'))
    except FileNotFoundError:
        pass
    except NotADirectoryError:
        pass