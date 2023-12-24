#  Start with the program you wrote for Exercise 6-1 (page 99). Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.

people = {
    'one' : {
        'first_name':'Ileri',
        'last_name':'Abolade',
        'age':20,
        'city':'Kwara',   
        },
    
    'two': {
        'first_name':'Kaycee',
        'last_name':'Chibundu',
        'age':20,
        'city':'Imo',
        },
    
    'three': {
        'first_name':'Muslimah',
        'last_name':'Sarunmi',
        'age':20,
        'city':'Kwara',
        }   
     
}
    


for k,v in people.items():
    print(f"\n Friend Profile: {k}")
    full_name = f"{v['first_name']} {v['last_name']}"
    city = v['city']
    age = v['age']
    
    print(f"\t Full name: {full_name.title()}")
    print(f"\t City: {city.title()}")
    print(f"\t Age: {age}")