spath="D:/baa.txt"
f=open(spath,"w")#w:写数据,写之前先清空; a:append
f.write("first line 1.\n")
f.writelines("fist line 2.\n")
f.close()

f=open(spath,"r")
for line in f:
    print("每一行数据是:%s" %line)

f.close()
