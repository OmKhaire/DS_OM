n = int(input("Enter number of inputs in salary: "))
list = []
for i in range(n):
    x = int(input("Enter salary no" + str(i + 1) + ": "))
    list.append(x)
print (list)
x=len(list)

for i in range(0,x):
    for j in range(0, x-i-1):
        if(list[j]>list[j+1]):
            temp=list[j]
            list[j]=list[j+1]
            list[j+1]=temp
print(list)

Top5=[]
for i in range(-1,-6,-1):
   Top5.append(list[i])

print(Top5)