# You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.

# Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.

# Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

# Print a second set of invitation messages, one for each person who is still in your list

guests = ['Ileri', 'Kaycee', 'Muslimah']
print(f"Hey {guests[0]}! I'll be having a dinner at my place later today and I'd love you to come by.")
print(f"Hey {guests[1]}! I'll be having a dinner at my place later today and I'd love you to come by.")
print(f"Hey {guests[2]}! I'll be having a dinner at my place later today and I'd love you to come by.")

print('Ileri')

guests.insert(0, 'Radiya')

print(f"Hey {guests[0]}! I'll be having a dinner at my place later today and I'd love you to come by.")
print(f"Hey {guests[1]}! I'll be having a dinner at my place later today and I'd love you to come by.")
print(f"Hey {guests[2]}! I'll be having a dinner at my place later today and I'd love you to come by.")