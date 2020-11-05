# SpotiCover
A script to get the cover image for the song, and displaying it on Windows. Locked to one corner of the screen. 
# Usage
On the Spotify Developers Dashboard you will need to create a new 'app'. You will get a client id and a client secret. 
Edit the run.py file and change the variables client_id and client_secret. Also change the username, which is not the same as your email. You can find it at spotify.com > account > username. It is often a long string of random letters and numbers. 

Now just run the script, and it should work! (Well, after installing the requirements)
# API
I will be using Spotify's API
# Language 
Will be using Python 
# Requirements 
  - pywin32
  - spotipy
  - wget
  - tkinter
  - Pillow
# Music Player
 For now you will need to use Spotify
# Issues
 - Currently the image shows up, centers, and if you have your mouse over it, it will say 'not responding'. This has something to do with root.mainloop() .. I'm using root.update() otherwise the rest of the code won't run. I have to find a workaround for it. 
 If you experience other issues, report them!
# To-Do
I will be using some code of SpotiPlay
- [X] Getting the current song thats being played
- [X] Making code for detecting where the song ends, and restarting the script
- [X] Downloading the album cover. Spotifys API gives me the image, but without extension so need to add it myself automatically.
- [X] Chaning the extention of the file downloaded, to a .jpg so i can display it. 
- [X] Displaying the image, but not with the Windows 10 photos app. Need to find a better way. 
- [X] Centering it to a corner. 
# Maybe in the future
- [ ] Showing the name of the song below the cover image. 
- [ ] Making it more user friendly
