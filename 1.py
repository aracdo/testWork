n=int(input('n='))
i=1
answer=[]
while i!=n:
    m=1
    while m<=n-i:
        ans=[]
        k=n-m
        while k>0:
            ans.append(i)
            k-=i
        if k==0:
            ans.append(m)
            ans.sort()
            if ans not in answer:
                answer.append(ans)
        m+=1
    i+=1
an=[]
for i in answer:
    ans=''
    for j in range(0,len(i)-1):
        ans+=str(i[j])+"+"
    ans+=str(i[len(i)-1])
    an.append(ans)
an.append(str(n))
an.sort()
for i in an:
    print(i)
