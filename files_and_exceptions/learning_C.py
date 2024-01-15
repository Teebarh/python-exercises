# You can use the replace() method to replace any word in a
# string with a different word.

with open('learning_python.txt') as file_object:
    lines = file_object.readlines()
    
content = ''
for line in lines:
    content += line.lstrip()
    
content.replace('Python', 'C')
