class A():
    def __init__(self):
        self.name = "haha"
        self.age = 18
    def fget(self):
        print("我被读取了")
        return self.name
    def fset(self,name):
        print("我被写入了")
        self.name = "图灵学院" + name
    def fdel(self):
        pass
    name2 = property(fget,fset,fdel,"这是一个property的例子")

a = A()
print(a.name)
print(a.name2)
