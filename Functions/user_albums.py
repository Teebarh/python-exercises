# Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. 
# Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.

def make_album(artist_name, album_title,):
    """This function collects information about an artist, and their album."""
    music_album = {'name': artist_name, 'album title': album_title}
    return music_album

while True:
    print("Please tell me the artist's information")
    print("\nType 'q' at any time to quit.")
    
    a_name = input("What is the artist's name? ")
    if a_name == 'q':
        break
    
    a_title = input("What is the title of the album? ")
    if a_title == 'q':
        break
    
    output = make_album(a_name, a_title)
    print(f"This is a profile of the artist: {output}")