file=open("people1.txt","r")
val=file.read()
list=val.split("\n")
i=0
count=0
while i<len(list):
    count=count+1
    i=i+1
print(count)
