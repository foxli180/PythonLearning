import os
import os.path
rootdir="C:/Users/E540258/Downloads"
for parent,dirnames,filenames in os.walk(rootdir):

    #case1
    for dirname in dirnames:
        print("parent is: "+parent)
        print("dirname is: "+dirname)

    #case2:
    for filename in filenames:
        print("parent is: "+parent)
        print("filename is: "+ filename)
        print("filename with full path is: "+ os.path.join(parent,filename))
