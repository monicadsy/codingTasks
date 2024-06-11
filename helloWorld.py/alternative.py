# A program that reads a string and makes each alternate character into an upper case and each other alternate a lower case
string = "Hello World"
new_string = " "
char = 1

for i in string:
    if char % 2 == 0:
        new_string += i.lower()
    else:
        new_string += i.upper()
    char += 1

print(new_string)

# A program that reads the same string but making each alternative word in reverse lower/upper case
string = "Hello World"
reverse_string = " "
char = 1

for i in string:
    if char % 2 == 0:
        reverse_string += i.upper()
    else:
        reverse_string += i.lower()
    char += 1

print(reverse_string)




