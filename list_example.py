# List examples in python
# __author__ = Emmanuel DE LEON
# __license__ =
# __version__ = 0.1

list1 = [3, 5, 6, "True"]

# add an element at the end of the list
list1.append("False")

# insert value at index "i"
i = 0
list1.insert(i, "False")

# extract value at index "i"
print(list1.pop(i))

# extend a list
aList = [123, 'xyz', 'zara', 'abc', 123]
bList = [2009, 'manu']
aList.extend(bList)
# equivalece to
# aList = aList + bList
print("Extended List : ", aList)


# reverse list order
# list1.reverse()
print("Reversed List : ", aList)

# get index from value
print(list1.index("True"))

# get count from value
print(aList.count(123))

# remove element from list + example of casting
aList.remove(123)
print("Count : " + str(aList.count("123")))

# range list selection
print(list1[0:2])

# list last element
print(list1[-1])

# list last 3 elements
print(list1[-3:])

# list creation on comprehension !!!!!!!!!!!!!!SMART!!!!!!!!
list_init = [4, 6, 7, 8]
# create list of square value from even numbers from "list_init"
list_comp = [val**2 for val in list_init if val % 2 == 0]
print(list_comp)

