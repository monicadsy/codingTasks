#  Read the data from the text file DOB.txt and print it out in two different sections
name = []
birthday = []

f = open('DOB.txt', 'r')
data = f.readlines()

for line in data:
    parts = line.split()
    name.append(parts[:2])
    birthday.append(parts[2:])
f.close()

print("Name")
for i, name in enumerate(name, start=1):
    print("{}. {}".format(i, " ".join(name)))

print("")

print("Birthdate")
for i, birthday in enumerate(birthday, start=1):
    print("{}. {}".format(i, " ".join(birthday)))