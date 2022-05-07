# file=open("people.txt","w")
# val=file.write("i am going")
# print(val)
# file.close()

# file=open("people.txt","r")
# print(file.read())
# file.close()

# file=open("people.txt","a")
# val=file.write("\ni am teaching")
# file.close()

a=[1,[2,3],4,[5],6]
i=0
sum=0
b=[]
while i<len(a):
    n=a[i]
    if type (n) is list:
       
        for j in b:
            
            sum=sum+n[j]
    else:
        sum=sum+a[i]
    i=i+1
print(sum)
    
        