import os

def del_files(path):
    for root , dirs, files in os.walk(path):
        for name in files:
            if name.endswith("otsu.png"):
                os.remove(os.path.join(root,name)) 



    for root , dirs, files in os.walk(path):
        for name in files:
            if "chunk" in name:
                #print(os.path.abspath(os.path.dirname(root))[-25:-24])
                #os.rename(os.path.join(root,name))
                if os.path.abspath(os.path.dirname(root))[-25:-24] == '\\':
                    pathname = os.path.abspath(os.path.dirname(root))[-24:]
                    os.rename(os.path.join(root,name), os.path.join(root,pathname) + '.png')
                elif os.path.abspath(os.path.dirname(root))[-25:-24] == '\n':
                    pathname = os.path.abspath(os.path.dirname(root))[-23:]
                    os.rename(os.path.join(root,name), os.path.join(root,pathname) + '.png')
                else:
                   pathname = os.path.abspath(os.path.dirname(root))[-25:]
                   os.rename(os.path.join(root,name), os.path.join(root,pathname) + '.png')
# test
if __name__ == "__main__":
    path = r'C:\Users\sa-u\OneDrive - rub.de\RUB\Semester_2\Big Data in der Bioinformatik\Mask_RCNN-master\path\cell\stage1_train'
    del_files(path)
