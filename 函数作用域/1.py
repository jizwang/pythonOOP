# #递归调用限制代码
# x = 0
# def fun():
#     global x
#     x +=1
#     print(x)
#     fun()
# fun()

#斐波那契额数列
# def fib(n):
#     if n ==1:
#         return 1
#     if n == 2:
#         return 1
#     return fib(n-1) + fib(n-2)
# print(fib(30))

# a = [x for x in range(1,10)]
# b = [i*1 for i in a if i%2==0]
# print(b)

# b = ["2","d","A"]
# print(max(b))

# s = "I love python"
# print(list(str(s).split(' ')))

#count:查找列表中指定值或元素的个数
# a = [1,2,3,4,5,4,5,4,4]
# print(a.count(4))

#深拷贝和浅拷贝：copy()函数是个浅拷贝函数
# a = [1,2,3,[1,2,3]]
# b = a.copy()
# print(id(a))
# print(id(b))
# print(id(a[3]))
# print(id(b[3]))

##元祖的特性：list具有的一些操作，除可修改外都一样
# s = set()
# print(type(s))

# s = {(1,2,3),("i","love","python"),(4,5,6)}
# for k in s:
#     print(k)

# add:向集合内添加元素

# s1 = {1,2,2,3,4,5}
# s2 = {5,66,9,4,2}
#
# s = frozenset()
#冰冻集合，不可以进行任何修改的集合

#字典的成员检测，检测的是key的内容
# d = {"one":1,"two":2,"three":3}
# d1 = {k:v for k,v in d.items() if v%2 == 0}
# print(type(d.keys()))

# l = ["a","b","c"]
# d = dict.fromkeys(l,"hahaha")
# print(d)

