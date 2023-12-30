# An ice cream stand is a specific kind of restaurant. Write
# a class called IceCreamStand that inherits from the Restaurant class you wrote
# in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of
# the class will work; just pick the one you like better. Add an attribute called
# flavors that stores a list of ice cream flavors. Write a method that displays
# these flavors. Create an instance of IceCreamStand, and call this method

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type,):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)
        
    def open_restaurant(self):
        print(self.restaurant_name + " " + "is now open!")
        
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
        
    def ice_cream_flavors(self):
        print("These are the available ice cream flavors:")
        for flavor in self.flavors:
            print(flavor)
            
ice_cream_stand = IceCreamStand("Tee's place", "African")
ice_cream_stand.flavors = ['mint', 'strawberry', 'vanilla']
ice_cream_stand.describe_restaurant()
ice_cream_stand.ice_cream_flavors()
        