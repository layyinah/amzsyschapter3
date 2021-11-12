import sys
import os
dic={}
def extcount():
    dir=sys.argv[1]
    for root,dirs,files in os.walk(dir):
        for name in files:
            filename=name.split(".")
            extension=filename[len(filename)-1]
            count=dic.get(0)
            count+=1
            dic=count
    for key,value in dic.items():
        print(key,value)
extcount()


