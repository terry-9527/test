
# list1 = [1,4,33,2,8]
# print(list1)

# print(list1.pop(2))
# print(list1)
# print(list1.remove(111))
# print(list1)
# print(list1.index("aaa"))
# print(list1.index(111))
# print(list1.count(111))
# list1.sort()
# print(list1)
# list1.reverse()
# print(list1)


# list1 = [name,age]
# print("\n".join(list1))
# def test():
#     name = input("请输入名字：")
#     age = input("请输入年龄：")
#     print("您输入的名字是{},年龄是{}".format(name,age))
#
# test()

# dict1 = {
#     'student1':{'name1':'terry','number':'100110','score':'89','hobby':'play basketball'},
#     'student2':{'name1':'maxi','number':'234324','score':'95','hobby':'reading'}
#          }
dict1 = {'name':'terry','number':'100110','score':'89','hobby':'play basketball'}
print(dict1["name"])
print(dict1.values())
print(dict1.keys())
print(dict1.items())

dict2 = {"name":"Terry","age":26,"marry":False}

list1 = ['name', 'number', 'score', 'hobby']

dict2 = dict.fromkeys(list1,11)
print(dict2)