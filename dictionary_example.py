# Dictionary examples in Python
# __author__ = Emmanuel DE LEON
# __license__ =
# __version__ = 0.1

# very useful structure for data parameters for example

dict1 = {"key1": "value1", "key2": "value2", "key3": "value3"}

# access to element by key
print(dict1["key2"])

# get all keys
#dict1.keys

# get all values
print(dict1.items())

# modify value or key
dict1["key3"] = "modified value"

#  add key + value
dict1["key4"] = "value4"

# delete key
del dict1["key1"]

print(dict1.items())



