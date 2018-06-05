import os
from time import gmtime,strftime
def getflist(path):
    l=os.listdir(path)
    for a in l:
        print(a)
        fa=os.path.join(path,a)
        if(os.path.isfile(fa) or os.path.isdir(fa)):
            mt=os.path.getmtime(fa)
            print(mt)
            print( gmtime(mt))
            print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime(mt)))
        else:
            print('skip')


if __name__=="__main__":
    getflist('/home/john/Downloads/')
