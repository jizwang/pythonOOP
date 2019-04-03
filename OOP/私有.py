class Person():
    name = "Liuying"
    __age = 18
p = Person()
print(p.name)

# __age是私有变量
# p._Person__age = 19
print(p.age())
print(p._Person__age)
