#在python中，任何类都有一个共同的父类叫object
class Person():
    name = "NoName"
    age = 0
    def sleep(self):
        print("Sleeping....")
    def work(self):
        print("make some money")

#父类写在括号内
class Teacher(Person):
    teacher_id = "9527"
    name = "DaNa"
    def make_test(self):
        print("attention")
    def work(self):
        # 扩充父类的功能只需要调用父类相应的函数
        # Person.work()
        # 扩充父类的另一种方法
        super().work()
        self.make_test()

t = Teacher()
print(t.name)
print(Teacher.name)
t.work()