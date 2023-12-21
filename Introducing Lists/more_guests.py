# You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.

# Start with your program from Exercise 3-4 or Exercise 3-5. Add a print() call to the end of your program informing people that you found a bigger dinner table.

# Use insert() to add one new guest to the beginning of your list.

# Use insert() to add one new guest to the middle of your list.

#Use append() to add one new guest to the end of your list.

#Print a new set of invitation messages, one for each person in your list.

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