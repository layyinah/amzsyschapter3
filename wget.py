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