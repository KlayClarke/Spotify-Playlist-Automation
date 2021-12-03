import os
from pprint import pprint
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

SPOTIPY_CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = 'http://example.com'

scope = 'playlist-modify-private'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, redirect_uri=SPOTIPY_REDIRECT_URI))

current_user_id = sp.current_user()['id']

# using user input to acquire personalized lists

# user_input_date = input('What year would you like to travel back to? Type the date in this format YYYY-MM-DD\n')
user_input_date = '2021-05-18'
response = requests.get(url=f'https://www.billboard.com/charts/hot-100/{user_input_date}/')
billboard_web_content = response.text

soup = BeautifulSoup(billboard_web_content, 'html.parser')
songs_tag = soup.select('li h3', limit=100)
song_titles = [song.text.strip() for song in songs_tag]

tracks_info = [sp.search(q='track:' + song, type='track', limit=1) for song in song_titles]

tracks_uri = []
for track in tracks_info:
    try:
        tracks_uri.append(track['tracks']['items'][0]['uri'])
    except IndexError:
        print(f'{track} not existent in Spotify\'s inventory. Skipped!')

user_new_playlist = sp.user_playlist_create(user=current_user_id,
                                            name=f'{user_input_date} Billboard Hot 100',
                                            public=False)
