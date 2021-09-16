import re


strings = "hello word!"
# 表达式编译成为pattern对象
pattern = re.compile(r"((he)|(hhe))l(lo) (word)(?P<sign>.*)")
# 查找匹配的字符串，没有找到则直接返回None，返回re.Match object对象
m = pattern.match(strings)
print(m)
# print(m.string)
print(m.group())  # 输出匹配的字符串
print(m.groups())
print(m.start(2))
print(m.end(2))
print(m.span(4))
print(m.pos,m.endpos)  #搜索文本的开始位置，搜索文本结束位置
print(m.expand(r'\5 \4\1'))
print(m.groupdict())

print(pattern.pattern)
print(pattern.flags)
print(pattern.groups)
print(pattern.groupindex)