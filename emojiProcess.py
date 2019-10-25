import imghdr
import os,shutil
import filetype

dir=os.listdir('emoji')
k=1
for file in dir:
    f=os.path.join('emoji',file)
    p=imghdr.what(f)
    n=filetype.guess(f)
    print(n)

    if p:
        shutil.move(f,os.path.join('emoji','%s.%s'%(str(k),str(p))))
        k+=1
    # else:
    #     os.remove(f)


