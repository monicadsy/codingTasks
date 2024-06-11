# Request a user to register students for an exam venue
# 1st ask the user how many students are registering
# 2nd use for loop to request the student ID number based on the number of students registered
# Last, write each of the ID number to the txt file reg_form use " with as", include a dotted line after ID for register


students_num = int(input("How many students are registering: "))
student_id = ""

for i in range (students_num):
    student_id = int(input("Please enter student ID number: "))
    with open('reg_form.txt', 'a+') as f:
        f.write("Student ID numbers: \n" + str(student_id))
        f.write("--------- \n")
print ("Thank you, Student ID numbers saved to reg_form.txt.")



