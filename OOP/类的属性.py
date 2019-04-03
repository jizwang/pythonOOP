class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.setName(name)
    def intro(self):
       print("hai,my name is {0}".format(self.name))
    def setName(self,name):
        self.name = name.upper()

s1 = Student("LIU Ying",18)
s2 = Student("sin",32)
s1.intro()
s2.intro()
