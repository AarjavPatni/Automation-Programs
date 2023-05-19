from mutagen.easyid3 import EasyID3
from os import listdir

# Get all mp3 files in "C:\Users\Aarjav\Downloads\New Songs"
new_songs = [rf"C:\\Users\\Aarjav\\Downloads\\New Songs\\{x}" for x in listdir(
    "C:\\Users\\Aarjav\\Downloads\\New Songs") if x.endswith(".mp3")]
old_songs = [rf'C:\\Users\\Aarjav\\Downloads\\Old Songs\\{x}' for x in listdir(
    "C:\\Users\\Aarjav\\Downloads\\Old Songs") if x.endswith(".mp3")]

all_songs = new_songs + old_songs

for i in all_songs:
    # Load the mp3 file
    audio = EasyID3(i)

    # Create a new field for each artist
    artists = audio['artist'][0].split(', ') if ', ' in audio['artist'][0] else audio['artist']
    # if any(',' in i for i in artists):
    #     for i in artists:

    audio['artist'] = artists

    try:
        albumartists = audio['albumartist'][0].split(', ') if ', ' in audio['albumartist'][0] else audio['albumartist']
        audio['albumartist'] = albumartists
    except Exception:
        pass

    # Save the changes to the file
    audio.save()
