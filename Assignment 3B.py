# Assigning values to the variables
string1 = "apple"
string2 = "cat"
string3 = "tree"

# Using if-statements to print the strings in alphabetical order
if string1 < string2 and string1 < string3:
    print(string1)
    if string2 < string3:
        print(string2)
        print(string3)
    else:
        print(string3)
        print(string2)
elif string2 < string1 and string2 < string3:
    print(string2)
    if string1 < string3:
        print(string1)
        print(string3)
    else:
        print(string3)
        print(string1)
else:
    print(string3)
    if string1 < string2:
        print(string1)
        print(string2)
    else:
        print(string2)
        print(string1)