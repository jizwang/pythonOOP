# # __call__举例
# class A():
#     # def __init__(self):
#     #     print("哈哈")
#     def __call__(self):#对象当函数使用的时候触发
#         print("我被调用了")
#     # def __str__(self):#当对象被当做字符串使用的时候可以触发这个函数
#     #     return "图灵学院"
#     def __repr__(self):
#         return "图灵"
# a = A()
# a
# # print(a)

#__getattr__
# class A():
#     name = "NoName"
#     age = 18
#     def __getattr__(self,name):
#         print("没找到啊")
#         print(name)
#
# a = A()
# print(a.name)
# print(a.addr)

# #setattr案例
# class Person():
#     def __init__(self):
#         pass
#     def __setattr__(self, name, value):
#         print("设置属性：{0}".format(name))
#         # self.name = value
#         super().__setattr__(name,value)
# p = Person()
# print(p.__dict__)
# p.age = 18

#__gt__
class Student():
    def __init__(self,name):
        self._name = name
    def __str__(self):
        return self._name
    def __gt__(self, obj):
        print("哈哈哈，{0}会大于{1}吗".format(self,obj))
        return self._name>obj._name
stu1 = Student("one")
stu2 = Student("two")
print(stu1>stu2)