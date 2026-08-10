n = int(input("Enter number of inputs in salary: "))
list = []
for i in range(n):
    x = int(input("Enter salary no" + str(i + 1) + ": "))
    list.append(x)
print (list)
x=len(list)

for i in range(0,x):
    minpos=i
    for j in range(i+1, x):
        if(list[minpos]>list[j]):
            minpos=j
    temp=list[i]
    list[i]=list[minpos]
    list[minpos]=temp
    

 
print(list)

Top5=[]
for i in range(-1,-6,-1):
   Top5.append(list[i])

print(Top5)