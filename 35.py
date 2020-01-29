
import matplotlib.pyplot as plt

class Prostokat():
    def __init__(self, a, b, c, d):
        self.a =a
        self.b=b
        self.c=c
        self.d=d
        self.bokA = b[0] - a[0]
        self.bokB = d[1] - a[1]
        
    def pole(self):
        return self.bokA*self.bokB
    def obwod(self):
        return 2*self.bokA + 2*self.bokB
    
    def boki(self):
        return [self.bokA, self.bokB]
        

class ProstyProstokat():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def obwod(self):
        return 2*self.a+2*self.b
    def pole(self):
        return self.a*self.b
class ProstyKwadrat(ProstyProstokat):
    def __init__(self, a):
        super().__init__(a,a)