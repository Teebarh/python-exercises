# Make a class Die with one attribute called sides, which has a default
# value of 6. Write a method called roll_die() that prints a random number
# between 1 and the number of sides the die has. Make a 6-sided die and roll it 10 times.

from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides
        
    def roll_die(self):
        number = randint(1, self.sides)
        return number

# first roll    
roll_1 = Die()
roll_1.roll_die() # 1
roll_1.roll_die() # 2
roll_1.roll_die() # 3
roll_1.roll_die() # 4
roll_1.roll_die() # 5
roll_1.roll_die() # 6
roll_1.roll_die() # 7
roll_1.roll_die() # 8
roll_1.roll_die() # 9
roll_1.roll_die() # 10

# second roll
roll_2 = Die(10)
roll_2.roll_die() # 1
roll_2.roll_die() # 2
roll_2.roll_die() # 3
roll_2.roll_die() # 4
roll_2.roll_die() # 5
roll_2.roll_die() # 6
roll_2.roll_die() # 7
roll_2.roll_die() # 8
roll_2.roll_die() # 9
roll_2.roll_die() # 10

# third roll
roll_3 = Die(20)
roll_3.roll_die() # 1
roll_3.roll_die() # 2
roll_3.roll_die() # 3
roll_3.roll_die() # 4
roll_3.roll_die() # 5
roll_3.roll_die() # 6
roll_3.roll_die() # 7
roll_3.roll_die() # 8
roll_3.roll_die() # 9
roll_3.roll_die() # 10