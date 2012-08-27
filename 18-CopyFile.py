import shutil
import os
import os.path

src="C:\\Users\\E540258\\Downloads\\myfile1.txt"
dst="C:\\Users\\E540258\\Downloads\\myfile2.txt"
dst2="C:/Users/E540258/Downloads/myfile3.txt"

dir1=os.path.dirname(src)

print("dir1 %s" %dir1)

if(os.path.exists(src)==False):
    print("%s does not exist,create it!" %dir1)
    os.makedirs (dir1) #目录不存在的话创建目录
else:
    print("%s already exist!" %src)

f1=open(src,"w")
f1.write("line a\n")
f1.write("line b\n")
f1.close()

shutil.copyfile(src,dst) #copy src 到dst1
shutil.copyfile(src,dst2)#copy src 到dst2

f2=open(dst,"r")
for line in f2:
    print(line)


f2.close()

# copy 整个test 目录到test2
try:
    srcDir="c:/Users/E540258/Downloads/test"
    dstDir="c:/Users/E540258/Downloads/test2"
    shutil.copytree(srcDir,dstDir)
except Exception as err:
    print(err)
