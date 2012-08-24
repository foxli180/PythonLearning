import os.path

spath = "C:/Users/E540258/Downloads/Evernote_4.5.8.7356.exe"
spath = "C:\\Users\\E540258\\Downloads\\Evernote_4.5.8.7356.exe"
# case1:
p,f =os.path.split(spath);
print("dir is: "+p)
print("file is: "+f)

# case2:

dev,left=os.path.splitdrive(spath);
print("Driver is: "+ dev)
print("Left is: "+ left)

# case3:
f,ext=os.path.splitext(spath);
print("f is: "+f)
print("ext is: "+ext)



