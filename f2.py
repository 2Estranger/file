f=open("f2.txt","w")
f.write("Hello\n")
f.write("My Name Is Prena Rai\n")
f.write("I am 20 Years old")
f.close()
print("Writing Succces.")

f=open('f2.txt','r')
data=f.read()
print(data)
f.close()

# f=open("f2.txt","rb")
# data=f.read()
# print(data)
# f.close()