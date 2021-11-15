import sys
import find
import urllib.request


def urllinks(url):
     page=1
     urls=[]
     allpag=urllib.request.urlopen(url).read()
     while(page>0):
         page=allpag.find('http://')
         allpag=allpag[page+1:]
         page=allpag.find('"')
         url.append(allpag[:page])
         allpag=allpag[page:]
         page=allpag.find('http://')
     print(allpag)
urllinks(sys.argv[1])