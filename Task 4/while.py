# The following example shows a program whose while statement calculate average of numbers input by the suer until the user enters "-1"
# An update satement increments i input by the user
num = 0
inputs = []

while True:
    num = int(input("Please enter a number:"))
    if num == -1:
        break
    else:
        inputs.append(num)

print(sum(inputs) / len(inputs))

