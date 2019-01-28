# Loop examples in python
# __author__ = Emmanuel DE LEON
# __license__ =
# __version__ = 0.1


aList = [123, 'xyz', 'zara', 'abc', 123]
bist1 = [3, 5, 6, 7]

# Display elements with for
for elem in aList :
    print(elem)

for i, a in enumerate(aList):
    print(i, a)

# zip function to enumerate two lists

for day, weather in zip(["monday", "thuesday"], ["sunny", "snowy"]):
    print("%s will be %s" %(day.capitalize(), weather))


# Simple while loop
i = 1
val_stop = 60
while i < 100:
    i += 1
    if i > val_stop:
        break




