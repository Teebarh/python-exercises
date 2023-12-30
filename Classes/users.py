# Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.

class User:
    def __init__(self, first_name, last_name, age, gender, ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        
    def describe_user(self):
        print("This is the information contained in your user profile:")
        print( "\t" +"First Name: " + self.first_name)
        print("\t" + "Last Name: " + self.last_name)
        print("\t" + "Age: " + str(self.age))
        print("\t" + "Gender: " + self.gender)
        
    def greet_user(self):
        full_name = f"Hello {self.first_name} {self.last_name}"
        return full_name
 
# instance one       
user_1 = User('Ileri', 'Abolade', 20, 'Female')
user_1.describe_user()
user_1.greet_user()

# instance two       
user_1 = User('Kaycee', 'Chibundu', 23, 'Female')
user_1.describe_user()
user_1.greet_user()

# instance one       
user_1 = User('Muslimah', 'Sarumi', 26, 'Female')
user_1.describe_user()
user_1.greet_user()