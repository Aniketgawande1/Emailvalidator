import re

def email_validator():
    email =input("Enter the Email: ")
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    
    if re.match(pattern , email):
        print(f"{email}  is a vaild email !")
    
    else:
        print(f"{email} is an email is not valid . Please try again .")
        


email_validator()