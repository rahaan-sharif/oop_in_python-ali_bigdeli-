class person():
    def __init__(self, age, name):
        self.age=age
        self.name=name
    def display(self):
        print(self.name, self.age)
class student(person):
    def __init__(self, age, name, major):
        super().__init__(age, name)
        self.major=major
    def student_display(self):
        self.display()
        print(self.major)

ob=student(10, "amir", "math")
ob.student_display()
