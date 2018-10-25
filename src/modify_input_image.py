import os
import os.path
from os import listdir
from os.path import isfile, join
def rename():
    pathAWE = os.path.join(DATA_DIR,"awe")
    pathFiles = [ os.path.join(pathAWE,f) for f in listdir(pathAWE) if isfile(join(pathAWE,f)) == 0]
    for fs in pathFiles:
        for re_f in listdir(fs):
            namefile = os.path.basename(fs)
            if ".png" in re_f:
                os.rename(os.path.join(fs,re_f),os.path.join(fs,namefile + "_" + re_f ))
                # print("1")
if __name__ == "__main__" :
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(BASE_DIR,'data')
    rename()