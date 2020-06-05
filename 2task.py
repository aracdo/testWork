def IsIp(a):
    y=0
    for i in a:
        if i>=0 and i<=255:
            y+=1
    if len(a)==4 and y==4:
        return True
    return False
try:
    a=list(map(int,input().split('.')))
    print(IsIp(a))
except ValueError:
    print(False)

    
