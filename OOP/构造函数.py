# class Dog():
#     # __init__就是构造函数
#     # 第一个被调用
#     主要工作是进行初始化
#     def __init__(self):
#         print("It's a dog")
# kaka = Dog()

# class Animal():
#     pass
# class BuRuAni(Animal):
#     pass
# class Dog(BuRuAni):
#     def __init__(self):
#         print("It's a dog")
# kaka = Dog()

class A():
    def __init__(self):
        print('A')
class B(A):
    def __init__(self,name):
        print('B')
        print(name)
class C(B):
    # C中想扩展B的构造函数
    # 即调用B的构造函数后再添加一些功能
    # 由两种方法实现
    # 第一种是通过父类名调用
    # 第二种是通过super调用
   def __init__(self):
       # 首先调用父类构造函数
        B.__init__(self.name)
       # 其次，在增加自己的功能
        print("这是C中附加的功能")
c = C()