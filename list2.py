list1=['a','b','d','e']
print(list1)
# update
list1[2]='c'
print(list1)
# insert
list1.insert(-1,'d')
print(list1)
# append
list1.append('f')
print(list1)

# remove
list1.remove('b')
print(list1)
print(type(list1))

#delete
del list1[1]
print(list1)