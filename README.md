# pixoo64-spotify-integration
Displays album art of currently playing songs from Spotify on Pixoo 64 screen.

- Like mentioned before, when run, this displays album art of a currently playing song from Spotify on the Pixoo 64's screen.
- Also, in the bottom right hand corner, the time in am/pm format is shown.

Setup:
- Navigate to the "main.py" file
- Replace PIXOO64-IP-ADDRESS with your Pixoo 64's ip address
- Replace SPOTIFY-CLIENT-ID with your developer Spotify client's id
- Replace SPOTIFY-CLIENT-URI with your developer Spotify client's uri
- When changing all of these, please keep the quotations surrounding the text

Additional Things to Note:
- If the program is first run without a song currently playing from Spotify, a placeholder image will be shown until a song is played
- If playback of a song is stopped, the program will still display the most recent album art of the last song played on the Pixoo screen
- This program can't currently display art from podcast episodes, as such if a podcast episode from Spotify is played, a placeholder image will be shown

Credits:
- This project utilizes the Spotipy and the SomethingWithComputers Pixoo Python library
- Spotipy library: https://github.com/plamere/spotipy
- Pioo library: https://github.com/SomethingWithComputers/pixoo
