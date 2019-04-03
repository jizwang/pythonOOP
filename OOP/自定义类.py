# #自己组装一个类
# class A():
#     pass
# def say(self):
#     print("saying")
# say(9)
#
# A.say = say
# a = A()
# a.say()

# 自定义类
# def say(self):
#     print("Saying ")
# def talk(self):
#     print("talking")
# A = type("AName",(object,),{"class_say":say,"class_talk":talk})
# a = A()
#
# a.class_say()
# a.class_talk()
# A.__dict__

from types import MethodType
class A():
    pass
def say(self):
    print("Saying")
a = A()
a.say = MethodType(say,A)
a.say()
