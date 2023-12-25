# Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the album information correctly.

# Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. If the calling line includes a value for the number of songs, add that value to the album’s dictionary. Make at least one new function call that includes the number of songs on an album.

# Function one
def make_album(artist_name, album_title,):
    """This function collects information about an artist, and their album."""
    music_album = {'name': artist_name, 'album title': album_title}
    return music_album

make_album('ileri', 'React')
make_album('kaycee', 'Javascript')
make_album('muslimah', 'PHP')   

# function two
def make_album(artist_name, album_title, no_of_songs=None):
    """This function collects information about an artist, their album and optionally, the number of songs in the album."""
    music_album = {'name': artist_name, 'album title': album_title}
    if no_of_songs:
        music_album['no_of_songs'] = no_of_songs
    return music_album 

make_album('muslimah', 'PHP', no_of_songs=3) 