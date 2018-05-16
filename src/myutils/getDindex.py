from pathlib import Path
import os
import re

#   def singleton(cls,*args,**kw):
#       instances={}
#       def _singleton():
#           if cls not in instances:
#               instances[cls]=cls(*args,*kw)
#           return instances[cls]
#       return _singleton
#   @singleton
class SysSetting(object):
    def __init__(self):
        self.itemlist0=[]
        self.datamap={}
        self.home = str(Path.home())
        self.target=os.path.join(self.home,"Downloads")
    def resetitems(self):
        self.itemlist0.clear()
        self.datamap.clear()

    def updateattr(self):
        if not self.itemlist0:
            templist=os.listdir(self.target)
            for a in templist:
                b=os.path.join(self.target,a)
                if(os.path.isdir(b)):
                    self.itemlist0.append(a)
    def getallplayfiles(self,epname):
        vpath=os.path.join(self.target,epname)
        lst=os.listdir(vpath)
        for a in lst:
            a=os.path.join(vpath,a)
            if(os.path.isdir(a)):
                yield from self.getallplayfiles(a)
            else:
                filename, file_extension = os.path.splitext(a)
                if(file_extension in ['.mp4','.MP4','.MKV','.mkv']):
                #print(file_extension)
                    yield a

    def updatedatamap(self,keyname):
        if keyname not in self.datamap:
            templist=[]
            it=self.getallplayfiles(keyname)
            for a in it:
                tmpa=a.split(keyname+os.sep,1)
                templist.append(tmpa[1].replace('/','-->'))
            self.datamap[keyname]=templist.copy()
    


if __name__ == "__main__":
    a=SysSetting()
    a.updateattr()
    print(a.itemlist0)
    b=SysSetting()
    print(b.itemlist0)
    b.updatedatamap("2")
    print(b.datamap)

