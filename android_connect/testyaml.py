import jsonpath
import yaml

data = {
    "name":"Fide",
    "phone":"18276762767",
    "address":"金享楼2栋",
    "number":700,
    "salary":200000,
    "department":"研发/测试部"
}

#dump() 把Python中的dict数据写入文件当中
# with open('./yaml_test.yaml', 'w',encoding="utf-8") as f:
#     y = yaml.dump(data,f,allow_unicode=True)
#     print(y)
#load() 读取文件中的json数据
with open('./yaml_test.yaml', 'r',encoding='utf-8') as f:
    x = yaml.load(f,Loader=yaml.SafeLoader)
    print(x)
    print(type(x))
    print(jsonpath.jsonpath(x,'$..[name,salary]'))