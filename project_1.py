class Dog():
    intity=0;
    def __init__(self, name, counter):
        self.name=name;
        self.counter=counter;
        Dog.intity+=1
    def show(self):
        print("***")
        print(self.name, ":", self.counter)
        print("intity:", self.intity)
        print("***")
ob1=Dog("hoskey",2)
ob2=Dog("galle",3)

ob1.show()
ob2.show()