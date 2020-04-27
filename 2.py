n,s = map(int,input().split())
numbers=[]
popka={}
numbers = input().split()
for i in range(0,len(numbers)):
    numbers[i]=int(numbers[i])
num = sorted(numbers, reverse = True)
i=0
j=0
while s!=0:
    while s>=0:
        s-=num[i]
        j+=1
    
    s+=num[i]
    i+=1
    j-=1
print(j)
