class nonrestore:
    def __init__(self,a,q,m):
        self.a = a
        self.q = q
        self.m = m
        self.cm = self.comp(m)
    def leftshift(self):
        for i in range(len(a)-1):
            self.a[i] = self.a[i+1]     
        self.a[-1] = self.q[0]
        for i in range(len(a)-1):
            self.q[i] = self.q[i+1]     
        self.q[-1] = 0       
    def comp(self,m):
        carry = 0
        j=-1
        for i in range(len(m)):
            if m[i] == 0:
                m[i] = 1
            else:
                m[i] = 0
        while m[j] == 1:
            m[j] = 0
            j = j - 1
        m[j] = 1
        return m
    def add(self):
        carry = 0
        for i in range(-1,-len(self.a)-1,-1):
            self.a[i]=int((self.a[i] + self.m[i] + carry) % 2)
            carry=int((self.a[i] + self.m[i] + carry) / 2)
    def sub(self):
        carry = 0
        for i in range(-1,-len(self.a)-1,-1):
            temp = (self.a[i]+self.cm[i]+carry)
            if ((self.a[i]+self.cm[i]+carry)%2) == 0:
                self.a[i] = 0
            else:
                self.a[i] = 1
            if temp >= 2:
                carry = 1
            else:
                carry = 0
    def calc(self):
        for i in range(len(self.a)):
            self.leftshift()
            self.display()
            if self.a[0] == 0:
                self.sub()
                if self.a[0] == 0:
                    self.q[-1] = 1
                else:
                    self.q[-1] = 0
                self.display()
            else:
                self.add()
                if self.a[0] == 0:
                    self.q[-1] = 1
                else:
                    self.q[-1] = 0
                self.display()
        if self.a[0] == 1:
            self.add()    
    def display(self):
        print(f"A={self.a} Q={self.q}")

a = [0,0,0,0]
q = [1,0,1,0]
m = [0,0,1,1]
d = nonrestore(a,q,m)
d.calc()
d.display()