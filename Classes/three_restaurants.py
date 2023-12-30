# Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type,):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)
        
    def open_restaurant(self):
        print(self.restaurant_name + " " + "is now open!")
   
# Instance one     
restaurant_1 = Restaurant("Tee's place", "African")
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

# Instance two
restaurant_2 = Restaurant("Kaycee's place", "Italian")
restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()

# Instance three
restaurant_3 = Restaurant("Ileri's place", "Chinese")
restaurant_3.describe_restaurant()
restaurant_3.open_restaurant()