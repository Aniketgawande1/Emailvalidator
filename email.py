import re

def email_validator():
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    while True:
        email = input("Enter the Email (or 'quit' to exit ): ")
        if email.lower() == 'quit':
            print("Goodbye Buddy !")
            break
            
        if re.match(pattern, email):
            print(f"{email} is a valid email!")
        else:
            print(f"{email} is not a valid email. Please try again.")

email_validator()