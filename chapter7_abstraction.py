from random import randint
from abc import ABC, abstractmethod


class base(ABC):
    def __init__(self):
        self.code=[0]*20
        self.word=""
    @abstractmethod
    def generate():
        pass

class d1(base):
    def generate(self):
        for i in range(20):
            a=randint(0,1)
            if(a==0):
                self.code[i]=chr(randint(65, 90))
            elif(a==1):
                self.code[i]=chr(randint(97,122))
            else:
                print("error in class d1*************")
        self.word="".join(self.code)
                
class d2(base):
    def generate(self):
        for i in range(20):
            self.code[i]=str(randint(0,9))
        self.word="".join(self.code)

class d3(base):
    def generate(self):
        for i in range(20):
            a=randint(0,2)
            if(a==0):
                self.code[i]=chr(randint(65, 90))
            elif(a==1):
                self.code[i]=chr(randint(97,122))
            elif a==2:
                self.code[i]=str(randint(0,9))
            else:
                print("error in d3******)))))")
        self.word="".join(self.code)
            
            
print("**********")
ob3=d3()
ob3.generate();
print("ob3: ", ob3.word)

ob2=d2()
ob2.generate()
print("ob2: ", ob2.word)

ob1=d1()
ob1.generate()
print("ob1: ", ob1.word)
