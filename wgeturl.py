# import sys
# import urllib
# def getpage(url):
#     if url[-1] == "/":
#         return "index.html"
#     else:
#         return url.split("/")
#
# def wget(url):
#     b=getpage(url)
#     result=urllib.urlopen(url)
#     print(url,b)
#     content=result.read()
#     file=open(b,"w")
#     file.write(content)
# wget(sys.argv[1])
import urllib
import sys
import re
def wget(url):
	x=re.search(r'(\w)+.(\w)+$',sys.argv[1])
	if sys.argv[1][-1]=='/':
		urllib.urlretrieve(sys.argv[1],'index.html')
	else:
		 urllib.urlretrieve(sys.argv[1],x.group())
wget(sys.argv[1])