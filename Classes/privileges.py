# Write a separate Privileges class. The class should have one
# attribute, privileges, that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class. Make a Privileges instance
# as an attribute in the Admin class. Create a new instance of Admin and use your
# method to show its privileges.

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
    
class Admin(User):
    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Privileges()
        
class Privileges:
    def __init__(self,):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
        
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)
            
admin = Admin("Ileri", "Abolade", 20, "Female")
admin.privileges.show_privileges()
