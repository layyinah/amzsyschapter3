import urllib

import sys
import os

def anti():
    url=sys.argv[1]
    urllength=len(url)
    if url[urllength-1] =="/":
        filename='index.html'
    else:
        urlsecone=url.split("/")
        urllength=len(urlsecone)
        filename=urlsecone[urllength-1]
    print(filename)
    path="/home/user/"
    getpath=os.path.join(path,filename)
    urllib.urlretrieve(url,getpath)
    line=open(getpath).readlines()
    for i in line:
        print(i)
anti()