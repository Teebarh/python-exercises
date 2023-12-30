# An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
# or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list
# of strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of
# privileges. Create an instance of Admin, and call your method.

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
        self.privileges = ['can add post', 'can delete post', 'can ban user']
        
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)
            
admin = Admin("Ileri", "Abolade", 20, "Female")
admin.show_privileges()