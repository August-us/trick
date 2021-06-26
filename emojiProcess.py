import imghdr
import os,shutil
from filetype import filetype
import glob

dir=glob.glob('E:\paper\VQVAE\Image\Group2\**\*', recursive=True)


for file in dir:
    # print(file)
    if os.path.isfile(file):

        p=imghdr.what(file)
        # print(os.path.split(file)[-1])
        # input()
        # if p != file.split('.')[-1]:
        # shutil.move(file, file+'.%s'%p)
        shutil.move(file, 'E:\paper\VQVAE\Image\Group2\%s'%os.path.split(file)[-1])



