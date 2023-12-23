# Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test. Your code should look something like this:
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')

# Test 1
bird = 'Flamingo'
print('Is a Flamingo a bird? I definitely think so.')
print(bird == 'Flamingo')

# Test 2
bird = 'pigeon'
print("Is a Cadiilac a bird? I disagree, it's a car.")
print(bird == 'Cadillac')

# Test 3
cola_drink = 'Pepsi'
print('Is Pepsi a cola drink? I predict True.')
print(cola_drink == 'Pepsi')

# Test 4
number = 5
print('Is the number equal to 5?')
print(number == 5)

# Test 5
number = 6
print('Is the number less than 5?')
print(number < 5)

# Test 6
city = ['London', 'Lagos', 'Cardiff', 'Abuja']
print('Is Lagos a city? I think it is.')
print('Lagos' in city)

# Test 7
print("What about Antarctica? I don't think so though.")
print('Antarctica' in city)

# Test 8
print("Antarctica has to be continent then.")
print('Antarctica' not in city)

# Test 9
age = 18
print('Are you old enough to drive?')
if age >= 18:
    print('Yes')
else:
    print('No')
    
# Test 10
cars = ['VOLVO', 'Mercedes', 'BMW', 'Tesla', 'Lucid']
for car in cars:
    if car == 'VOLVO':
        print(car.title())
    else:
        print(car)
        
# Test 11
age_1 = 19
(age_1 >=12) and (age_1 < 18) 

# Test 12
chocolate = 'Snickers'
print('Are marshmellows a type of chocolate?')
print(chocolate == 'marshmellow')