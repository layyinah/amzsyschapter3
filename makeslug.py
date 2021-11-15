from string import *
import re
def makeslug(s):
    list = re.findall(r'(\w+)', " --hello-  world--")
    print('-'.join(list))
    # for st in punctuation:
    #     s=s.replace(st,"")
    # # s=strip(s,"")
    # s=re.sub(' + ',"",s)
    # s=re.sub('','-',s)
    # print(s)
makeslug("hello world")
makeslug("hello world!")
makeslug(" --hello-  world--")
