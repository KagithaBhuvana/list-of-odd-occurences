list_n=input().split()
list_a=[]
for i in list_n:
    count=list_n.count(i)
    i=int(i)
    flag=0
    for j in range(len(list_a)):
        num=int(list_a[j])
        if(num==i):
            flag=1
            break 
    if(flag==0):
        if(count%2!=0):
            list_a.append(i)
list_a.sort()
print(list_a)
