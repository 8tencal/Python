# Examples of string in python
# __author__ = Emmanuel DE LEON
# __license__ =
# __version__ = 0.1

string1 = "Python for noobs like me "

# extraction of a characters like a list
print(string1[0:6])

# Transform a string into a list of elements
list1 = string1.split()
print(list1)

# Create string from list with .join to separate with spaces
string2 = " ".join(list1)
print(string2)

# .upper() . lower() change to capital letters or lower letters
print(string2.upper())

# count the number of elements
print(string2.count("o"))

# find an element index from string else 0
print(string2.find("y"))

# .lstrip() .rstrip() .strip() Space deletion beginning of string, end of string , both
path = " Test "
new_path = path.strip()
print(new_path)

# replace element in string
string3 = "Cemputer"
print(string3.replace("e", "o", 1))
