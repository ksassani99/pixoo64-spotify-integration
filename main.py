import os
import time
from datetime import datetime
from types import NoneType
import requests
import sys
from pprint import pprint
from PIL import Image
from io import BytesIO
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import spotipy
from pixoo import Channel, ImageResampleMode, Pixoo

ipAdd = 'PIXOO64-IP-ADDRESS'
clID = "SPOTIFY-CLIENT-ID"
clSEC = "SPOTIFY-CLIENT-SECRET"
rURI = "SPOTIFY-CLIENT-URI"
scope = "user-read-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=clID, client_secret=clSEC, redirect_uri=rURI, scope=scope))
playTr = sp.current_playback()

pixoo = Pixoo(ipAdd, 64, False)

def getCurrTrkImg():
    imgURL = playTr["item"]["album"]["images"][2]["url"]
    response = requests.get(imgURL)
    img = Image.open(BytesIO(response.content))

    return img

def checkPlay():
    if playTr is None:
        isPlaying = False
    else:
        isPlaying = True

    return isPlaying

def checkPod():
    checkPodPlay = playTr["currently_playing_type"]

    if checkPodPlay == "episode":
        isPod = True
    else:
        isPod = False

    return isPod

def showTime():
    pixoo.draw_filled_rectangle((44, 56), (62, 62), (51, 51, 51))
    pixoo.draw_pixel((53, 58), (255, 255, 255))
    pixoo.draw_pixel((53, 60), (255, 255, 255))

    now = datetime.today()
    currtimeh = now.strftime("%I")
    currtimem = now.strftime("%M")
    pixoo.draw_text(currtimeh, (45, 57), (255, 255, 255))
    pixoo.draw_text(currtimem, (55, 57), (255, 255, 255))

    pixoo.push()

def main():
    fallbackImg = "NotPlaying.png"
    podcastImg = "Podcast.png"

    while True:
        if checkPlay() is False:
            pixoo.draw_image(fallbackImg)

            showTime()

            pixoo.push()
        else:
            if checkPod() is True:
                fallbackImg = podcastImg
                pixoo.draw_image(podcastImg)

                showTime()

                pixoo.push()
            else:
                fallbackImg = getCurrTrkImg()
                pixoo.draw_image(getCurrTrkImg())

                showTime()

                pixoo.push()

        time.sleep(2)

if __name__ == '__main__':
    main()