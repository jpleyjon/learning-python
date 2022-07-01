print("Ch02 - Variables")
print("================")

# Basic data types: Number, Strings, Booleans, Sequences, Dictionaries

myInt = 5
myFloat = 13.2
myStr = "This is a string"
myBool = True
myList = [0, 1, "Two", 3.1, False]
myTuple = (0, 1, 2)
myDict = { "one" : 1, "two" : 2}

print(myInt)
print(myFloat)
print(myStr)
print(myBool)
print(myList)
print(myDict)

# re-declaring a variable works
myInt = "abc"
print(myInt);

# to access a member of a sequence type, use []
print(myList[2])
print(myTuple[2])

# use slice to get part of a sequence
myList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(myList[0:3])
print(myList[::5])

# using slice to reverse a sequence
print(myList[::-1])

