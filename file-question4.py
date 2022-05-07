file=open("people1.txt","r")
for i in file:
    if "delhi" in i:
        f1=open("delhi.txt","a")
        f1.write(i)
    elif "shimla" in i:
        f2=open("shimla.txt","a")
        f2.write(i)
    else:
        f3=open("other.txt","a")
        f3.write(i)
        



