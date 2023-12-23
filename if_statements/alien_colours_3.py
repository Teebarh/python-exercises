#: Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.

# If the alien is green, print a message that the player earned 5 points.

# If the alien is yellow, print a message that the player earned 10 points.

# If the alien is red, print a message that the player earned 15 points.

# Write three versions of this program, making sure each message is printed for the appropriate color alien.

# Case 1
alien_colour = 'green'
if alien_colour == 'green':
    print('You earned 5 points for shooting the alien!')
elif alien_colour == 'yellow':
    print('You earned 10 points for shooting the alien!')
else:
    print('You got 15 points for shooting the red alien!')
    
# Case 2
alien_colour = 'yellow'
if alien_colour == 'green':
    print('You earned 5 points for shooting the alien!')
elif alien_colour == 'yellow':
    print('You earned 10 points for shooting the alien!')
else:
    print('You got 15 points for shooting the red alien!')
    
# Case 3
alien_colour = 'red'
if alien_colour == 'green':
    print('You earned 5 points for shooting the alien!')
elif alien_colour == 'yellow':
    print('You earned 10 points for shooting the alien!')
else:
    print('You got 15 points for shooting the red alien!')