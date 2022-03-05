f=open("f1.txt","a")
append="\nsayjal"
f.write(append)
f.close()

f=open("f1.txt","r")
v=f.readline()
print(v)
f.close()