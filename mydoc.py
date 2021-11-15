import sys
def mydoc(py):
    print("documentation of modules ")
    mod=__import__(py)
    print(py)
    print("functions in the module")
    for i in dir(mod):
        print(i)
mydoc(sys.argv[1])