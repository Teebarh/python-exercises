#  Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 162). Write a method called increment_login
# _attempts() that increments the value of login_attempts by 1. Write another
# method called reset_login_attempts() that resets the value of login_attempts to 0.

# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts(). Print login_attempts again to
# make sure it was reset to 0.

class User:
    def __init__(self, first_name, last_name, age, gender, ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0
        
    def describe_user(self):
        print("This is the information contained in your user profile:")
        print( "\t" +"First Name: " + self.first_name)
        print("\t" + "Last Name: " + self.last_name)
        print("\t" + "Age: " + str(self.age))
        print("\t" + "Gender: " + self.gender)
        
    def greet_user(self):
        full_name = f"Hello {self.first_name} {self.last_name}"
        return full_name
    
    def show_login_attempts(self):
        print(f"The user tried to login {self.login_attempts} times.")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        
user = User("Ileri", "Abolade", 20, "Female",)
print(user.show_login_attempts())
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.show_login_attempts())
user.reset_login_attempts()
print(user.show_login_attempts())
