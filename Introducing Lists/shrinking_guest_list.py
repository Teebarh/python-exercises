# You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

# Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.

# Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.

# Print a message to each of the two people still on your list, letting them know they’re still invited.

# Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

guests = ['Ileri', 'Kaycee', 'Muslimah']
print(f"Hey {guests[0]}! I'll be having a dinner at my place later today and I'd love you to come by.")
print(f"Hey {guests[1]}! I'll be having a dinner at my place later today and I'd love you to come by.")
print(f"Hey {guests[2]}! I'll be having a dinner at my place later today and I'd love you to come by.")

print("I found a bigger dinner table so we'll be having more people join us!")

guests.insert(0, 'Radiya')
guests.insert(2, 'Maryam')
guests.append('Rahma')

print(f"Hey {guests[0]}! I'll be having a dinner at my place later today and I'd love you to come by.")
print(f"Hey {guests[1]}! I'll be having a dinner at my place later today and I'd love you to come by.")
print(f"Hey {guests[2]}! I'll be having a dinner at my place later today and I'd love you to come by.")
print(f"Hey {guests[3]}! I'll be having a dinner at my place later today and I'd love you to come by.")
print(f"Hey {guests[4]}! I'll be having a dinner at my place later today and I'd love you to come by.")
print(f"Hey {guests[5]}! I'll be having a dinner at my place later today and I'd love you to come by.")

print("Oops, just found out the new dinner table won't get here in time, apologies guys.")

popped_guest = guests.pop()
print(f"I'm sorry {popped_guest}, I won't get to host you today.")

popped_guest = guests.pop()
print(f"I'm sorry {popped_guest}, I won't get to host you today.")

popped_guest = guests.pop()
print(f"I'm sorry {popped_guest}, I won't get to host you today.")

popped_guest = guests.pop()
print(f"I'm sorry {popped_guest}, I won't get to host you today.")

print(f"You're still invited {guests[0]}! The dinner starts at 7.")
print(f"You're still invited {guests[1]}! The dinner starts at 7.")

del guests[1]
del guests[0]

print(guests)
