class SetofStacks:
    def __init__(self,maximum):
        self.maximum = maximum
        self.lst=[[]]
        self.e=0
    def push(self,a):
        if len(self.lst[self.e])<self.maximum:
            self.lst[self.e].append(a)
        else:
            self.e+=1
            self.lst.append([])
            self.lst[self.e].append(a)
    def pop(self):
        self.lst[self.e].pop(len(self.lst[self.e])-1)
        if len(self.lst[self.e])==0:
            self.lst.pop(self.e)
            self.e-=1
    def show(self):
        return self.lst
    def size(self):
        a=0
        b=[]
        for i in range(0, self.e+1):
            a+=len(self.lst[i])
            b.append(len(self.lst[i]))
        return a,b
    def front(self):
        return self.lst[self.e][len(self.lst[self.e])-1]
    def head(self):
        return self.lst[0][0]
