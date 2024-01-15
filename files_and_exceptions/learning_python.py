# Open a blank file in your text editor and write a few
# lines summarizing what you’ve learned about Python so far. Start each line
# with the phrase In Python you can. . . . Save the file as learning_python.txt in
# the same directory as your exercises from this chapter. Write a program that
# reads the file and prints what you wrote three times. Print the contents once by
# reading in the entire file, once by looping over the file object, and once by storing the lines in a list and then working with them outside the with block.

# Case 1
with open('learning_python.txt') as lp:
    file = lp.read()
print(file)

# Case 2
with open('learning_python.txt') as l_p:
    for line in l_p:
        print(line.strip())
        
# Case 3
with open('learning_python.txt') as learning_python:
    lines = learning_python.readlines()
    
content = ''
for line in lines:
    content += line.lstrip()
    
print(content)
print(len(content))