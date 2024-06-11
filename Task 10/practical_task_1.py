"""
Task: 
------------------
1. Add another method in the Course class that prints the head office location: Cape Town
2. Create a subclass of the Course class named OOPCourse
3. Create a constructor that initialises the following attributes and assigns these values:
    --- "description" with a value "OOP Fundamentals"
    --- "trainer" with a value "Mr Anon A. Mouse"
4. Create a method in the subclass named "trainer_details" that prints what the 
   course is about and the name of the trainer by using the description and trainer attributes.
5. Create a method in the subclass named "show_course_id" that prints the ID number of the course: #12345
6. Create an object of the subclass called course_1 and call the following methods
   contact_details
   trainer_details
   show_course_id
   These methods should all print out the correct information to the terminal

Note: this task covers single inheritance. Multiple inheritance is also possible in Python and 
we encourage you to do some research on multiple inheritance when you have finished this course.
"""
class Course:
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"
#Add another method in the course class that prints the head office location
    location = "Cape Town"
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    def head_office(self):
        print("Head Office Location: ", self.location)

# A subclass of the Course class named OOPCourse with two attributes
class OOPCourse(Course):
    # Constructor
    def __init__(self, description, trainer):
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"
        self.identity_num = "12345"

# create a method trainer_details under subclass
    def trainer_details(self):
        print("Course description: " + self.description + "\nTrainer: " + self.trainer)

# create a method show_course_id under subclass
    def show_course_id(self):
        print("ID No: " + self.identity_num)

# create an object of the subclass called course_1 & print all the info
course_1 = OOPCourse("OOP Foundatmentals", "Mr Anon A. Mouse")
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()


    




