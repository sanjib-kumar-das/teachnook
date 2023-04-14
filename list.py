# Collection datatypes in python
# List -> [],ordered collection of datatypes,  is mutable , it contains duplicate values
mylist=[1,2,3,4,5,6,7,3.04,"Data",1]
print(mylist)
# index number
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[3])
print(mylist[4])
print(mylist[5])
print(mylist[6])
print(mylist[7])

# update
a=[3.05,3.06,3.07]
mylist[-3]=a
print("The values are ",mylist)

# Append/add
mylist.append(8)
print("The values are ",mylist)

# insert
mylist.insert(7,8)
print("The values are ",mylist)

# delete
del mylist[-1]
print("The updated values are ",mylist)

del mylist
print(mylist)
