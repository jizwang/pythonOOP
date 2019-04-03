class Teacher():
    name = "dana"
    age  = 18
    def say(self):
        self.name = "yaona"
        self.age = 17
        print("My name is {0}".format(self.name))
        print("My age is {0}".format(self.age))
    def sayAgain():
        print("hello,nice to see you again")
        #调用类的成员变量需要用__class__
        print(__class__.age)
        print(__class__.name)
        #调用
t = Teacher()
t.say()
Teacher.sayAgain()