# 元类写法固定，必须继承自type
# 元类一般命名以MetaClass结尾
class TulingMetaClass(type):
    def __new__(cls,name,bases,attrs):
        # 自己的业务处理
        print("我是元类")
        attrs['id'] = '00000'
        attrs['addr'] = "北京"
        return type.__new__(cls,name,bases,attrs)

class Teacher(object,metaclass=TulingMetaClass):
    pass
t = Teacher()
print(t.id)
