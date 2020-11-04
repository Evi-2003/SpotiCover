import sys
import time
import math
import os
import spotipy
import win32gui
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
import webbrowser
from IPython.display import display, Image
from PIL import Image
from urllib.parse import urlparse
from posixpath import basename, dirname
import wget
# We need some Authentication.
# The Client_ID Client_Secret And Username needs to be set by yourself, for now.
username = "-"
scope = "user-read-currently-playing"
token = util.prompt_for_user_token(
    username,
    scope,
    client_id='-',
    client_secret='-',
    redirect_uri='http://example.com/callback/')


class SpotiCover(object):
    def EeverythingActually(self):
        # GETTING THE SONG
        if token:
            sp = spotipy.Spotify(auth=token)
            results = sp.current_user_playing_track()
            songName = results["item"]["name"]  # Collecting the name
            # Looking where the song currently is
            songTimeStamp = results['progress_ms'] / 1000
            # The full duration of the song, so we can calculate when we need to reload the script ( I can't detect
            # currently if the user was skipping a song for now)
            SpotifySongDuration = results['item']['duration_ms'] / 1000

            # We may need to round it up, but this is possible for a later version.
            # roundedSongTimeStamp = math.trunc(songTimeStamp)

            # Getting the Cover
            getImage = results["item"]["album"]["images"][0]['url']
            print(getImage)
           # display(Image(filename=getImage))
            wget.download(getImage)
            parse_object = urlparse(getImage)
            path = parse_object.path
            coverID = basename(path)
            print(coverID)



            addJPG = coverID
            file = os.path.splitext(addJPG)[0]
            os.rename(addJPG, file + ".jpg")

        # DOES CURRENTLY OPEN WITH WINDOWS 10 PHOTO'S APP, NOT WHAT I WANTED... WILL LOOK INTO IT!
            image = Image.open(coverID + '.jpg')
            image.show()
        # Looking when the song ends, and reload the script, and remove the downloaded image
            time.sleep(SpotifySongDuration - songTimeStamp)
            os.remove(addJPG + ".jpg")
            os.system("reloader.py")
            # Restarting the script ones the video ends
            # We will need another script for this one


SpotiCover.EeverythingActually(1)

while True:
    pass
