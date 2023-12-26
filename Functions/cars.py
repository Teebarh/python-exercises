# Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. 
#  It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a color or an optional feature.
# Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True). Print the dictionary that’s returned to make sure all the information was stored correctly.

# first approach
import cars_function

car = cars_function.make_car('subaru', 'outback', color='blue', tow_package='True')
print(car)

# second approach
from cars_function import make_car

car = make_car('subaru', 'outback', color='blue', tow_package='True')
print(car)

# third approach
from cars_function import make_car as mc
car = mc('subaru', 'outback', color='blue', tow_package='True')
print(car)

# fourth approach
import cars_function as cf
cars = cf.make_car('subaru', 'outback', color='blue', tow_package='True')
print(car)

# fifth approach
from cars_function import *

car = make_car('subaru', 'outback', color='blue', tow_package='True')
print(car)