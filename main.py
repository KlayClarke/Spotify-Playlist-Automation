import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from bs4 import BeautifulSoup

SPOTIPY_CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET')

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

playlists = spotify.user_playlists('spotify')

# # using user input to acquire personalized lists
#
# user_input_date = input('What year would you like to travel back to? Type the date in this format YYYY-MM-DD\n')
# response = requests.get(url=f'https://www.billboard.com/charts/hot-100/{user_input_date}/')
# billboard_web_content = response.text
#
# soup = BeautifulSoup(billboard_web_content, 'html.parser')
# songs_tag = soup.select('li h3', limit=100)
# song_titles = [song.text.strip() for song in songs_tag]
# print(song_titles)

print(playlists)