# Ask user input for the name, age, hair colour, and eye colour
name = input("Enter your name: ")
age = int(input("Enter your age: "))
hair_color = input("Enter your hair color: ")
eye_color = input("Enter your eye color: ")

# Create an Adult class with the following attributes and method
class Adult():
    def __init__(self, name, age, eye_color, hair_color):
        self.name = name
        self.age = age
        self.eye_color = eye_color
        self.hair_color = hair_color

    def can_drive(self):
        print(self.name, "is old enough to drive.")

# Create a subclass Child of the Adult class and overrides the can_drive method
class Child(Adult):
    def can_drive(self):
        print(self.name, "is too young to drive.")

# Create age 18 logic criterion to print out wether the person is old enought to drive or not
if age >= int(18):
    user1 = Adult(name, age, eye_color, hair_color)
    user1.can_drive()
else:
    user1 = Child(name, age, eye_color, hair_color)
    user1.can_drive()
         



