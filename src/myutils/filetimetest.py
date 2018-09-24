import os
from time import gmtime,strftime
def getflist(path):
    l=os.listdir(path)
    final_result=[]
    for a in l:
        print(a)
        fa=os.path.join(path,a)
        if(os.path.isfile(fa) or os.path.isdir(fa)):
            mt=os.path.getmtime(fa)
            #print(mt)
            #print( gmtime(mt))
            #print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime(mt)))
            final_result.append([fa,strftime("%Y%m%d%H%M%S", gmtime(mt))])
        #else:
            #print('skip')

        final_result=sorted(final_result, key=lambda x: x[1],reverse=True)
    return final_result


def listdir_bydate(path):
    l=os.listdir(path)
    final_result=[]
    for a in l:
        print(a)
        fa=os.path.join(path,a)
        if(os.path.isfile(fa) or os.path.isdir(fa)):
            mt=os.path.getmtime(fa)
            #print(mt)
            #print( gmtime(mt))
            #print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime(mt)))
            final_result.append([a,strftime("%Y%m%d%H%M%S", gmtime(mt))])
        #else:
            #print('skip')

        final_result=sorted(final_result, key=lambda x: x[1],reverse=True)
    return [row[0] for row in final_result]


if __name__=="__main__":
    print(listdir_bydate('/home/sick/Downloads/'))
