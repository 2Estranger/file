f=open("question4.txt","r")
f1=open("Delhi.txt","w")
f2=open("Sikkim.txt","w")
f3=open("other.txt","w")
b=f.read()
d=b.split("\n")
i=0
while i<len(d):
    if "Delhi" in d[i]:
        f1.write(d[i])
        f1.write("\n")
    elif "Sikkim" in(d[i]):
        f2.write(d[i])
        f2.write("\n")
    else:
        f3.write(d[i])
        f3.write("\n")
    i=i+1 
f.close()