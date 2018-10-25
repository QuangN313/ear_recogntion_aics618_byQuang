import os
import os.path
from os import listdir
from os.path import isdir, join
import cv2 as cv
import argparse
import sys 

def rename(args):
    pathAWE = os.path.join(DATA_DIR,args.Image_folder_name)
    pathFolder = [ os.path.join(pathAWE,f) for f in listdir(pathAWE) if isfile(join(pathAWE,f))]
    for fs in pathFolder:
        for re_f in listdir(fs):
            namefile = os.path.basename(fs)
            if (".png" in re_f) or (".jpg" in re_f):
                os.rename(os.path.join(fs,re_f),os.path.join(fs,namefile + "_" + re_f ))
            

def resize(args):
    pathAWE = os.path.join(DATA_DIR,args.Image_folder_name)
    pathFolder = [ os.path.join(pathAWE,f) for f in listdir(pathAWE) if isdir(join(pathAWE,f))]
    for fs in pathFolder:
        for re_f in listdir(fs):
            namefile = os.path.basename(fs)
            if (".png" in re_f) or (".jpg" in re_f):
                img = cv.imread(os.path.join(fs,re_f))
                resize_img = cv.resize(img,(args.resize,args.resize))
                cv.imwrite(os.path.join(fs,re_f),resize_img)

def main(args):
    pathAWE = os.path.join(DATA_DIR,args.Image_folder_name)
    pathFolder = [ os.path.join(pathAWE,f) for f in listdir(pathAWE) if isdir(join(pathAWE,f))]
    for fs in pathFolder:
        for re_f in listdir(fs):
            namefile = os.path.basename(fs)
            if (".png" in re_f) or (".jpg" in re_f):
                if args.rename:
                    os.rename(os.path.join(fs,re_f),os.path.join(fs,namefile + "_" + re_f ))
                elif args.resize:
                    img = cv.imread(os.path.join(fs,re_f))
                    resize_img = cv.resize(img,(args.resize,args.resize))
                    cv.imwrite(os.path.join(fs,re_f),resize_img)

def parse_arguments(argv):          
    parser = argparse.ArgumentParser(description='Modify input image')
    
    parser.add_argument('--rename',
        help = 'Rename input image to FolderName_FileNum structure', action = 'store_true' )
    parser.add_argument('--resize',type = int,
        help = 'Resize input image', default = 160)
    parser.add_argument('Image_folder_name',type = str,
        help = 'Name of Image folder')
    return parser.parse_args(argv)


    
if __name__ == "__main__" :
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(BASE_DIR,'data')
    main(parse_arguments(sys.argv[1:]))
   