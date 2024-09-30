# Create a function which takes string password as a parameter and checks the length of password. If the length longer
# than 8 character it returns True otherwise returns False.

#Example:
# password_controller("custompassword")
# output:
# True

def password_controller(password):
    if len(password) > 8:
        return True
    else:
        return False

user_password = input("Enter the password: ")
result = password_controller(user_password)
print(result)
