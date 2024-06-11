class Email():
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    def mark_as_read(self):
        self.has_been_read = True

Inbox = []

def populate_inbox():
    email1 = Email("senderone@example.com", "Welcome", "The program will start.")
    email2 = Email("sendertwo@example.com", "Note", "You are enrolled.")
    email3 = Email("sender3@example.com", "Dates", "Please check course schedule.")
    Inbox.extend([email1, email2, email3])

def list_emails():
    for index, email in enumerate(Inbox):
        print(f"{index} {email.subject_line}")    

def read_email(i):
    email = Inbox[i]
    print(f"\nEmail from {email.email_address}\nSubject: {email.subject_line}\n\n{email.email_content}")
    email.mark_as_read()
    print(f"\nEmail from {email.email_address} marked as has been read.\n")

def list_unread_emails():
    unread_emails =  [email for email in Inbox if not email.has_been_read]
    for index, email in enumerate(unread_emails):
        print(f"{index} {email.subject_line}")   

# Populate the initial Inbox with sample emails
populate_inbox()

# Main program loop
while True:
    print("Welcome, please choose an option:\n1. Read an email\n2. View unread emails\n3. Quit application")

    choice = input("Enter your choice by 1,2 or 3: ")
    if choice == "1":
        list_emails()
        email_index = int(input("Enter the email index to read: "))
        read_email(email_index)

    elif choice == "2":
        list_unread_emails()
      
    elif choice == "3":
        print("Quit and see you next time!")
        break
    else:
        print("Oops - incorrect input.")
        




