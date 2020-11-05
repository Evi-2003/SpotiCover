import sys
import time
import math
import os
import spotipy
import win32gui
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
from urllib.parse import urlparse
from posixpath import basename, dirname
import wget

# maybe delete later
from tkinter import *
from PIL import ImageTk
from PIL import Image
import threading
# We need some Authentication.
# The Client_ID Client_Secret And Username needs to be set by yourself, for now.
username = "xw4dm4tsfaduaewklngslmilj"
scope = "user-read-currently-playing"
token = util.prompt_for_user_token(
    username,
    scope,
    client_id='75eb854eddec4ea0a3f02b6de123c2bc',
    client_secret='d07026c49b1640139858a3ba7bbc3254',
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
            # Downloads image without extension
            wget.download(getImage)
            parse_object = urlparse(getImage)
            path = parse_object.path
            coverID = basename(path)
            print(coverID)  # Printing out the name of the downloaded file.
            addJPG = coverID
            file = os.path.splitext(addJPG)[0]
            os.rename(addJPG, file + ".jpg")  # Adding the .jpg extension to the extension-less file.
            # Resizing to a better size
            cover = coverID + ".jpg"
            coverImages = Image.open(cover)
            doingResize = coverImages.resize((300, 300))
            doingResize.save('resized.jpg')
            os.remove(cover)
            # Showing the Cover
            root = Tk()
            canvas = Canvas(root, width=300, height=300)
            canvas.pack()
            coverIMG = ImageTk.PhotoImage(Image.open('resized.jpg'))
            canvas.create_image(0,0,anchor=NW, image=coverIMG)
            root.update()
            findWindow = win32gui.FindWindow(None, "tk")
            win32gui.MoveWindow(findWindow, -7, 0, 300, 300, True)
            root.update()
            # Looking when the song ends, and reload the script, and remove the downloaded image
            time.sleep(SpotifySongDuration - songTimeStamp)
            root.destroy()
            os.remove('resized.jpg')
            os.system("reloader.py")
            # Restarting the script ones the video ends
            # We will need another script for this one


SpotiCover.EeverythingActually(1)

while True:
    pass
