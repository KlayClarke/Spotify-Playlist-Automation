import requests
from bs4 import BeautifulSoup

# year = input('What year would you like to travel back to? Type the date in this format YYYY-MM-DD\n')
# print(year)

response = requests.get(url='https://www.billboard.com/charts/hot-100/')
billboard_web_content = response.text

soup = BeautifulSoup(billboard_web_content, 'html.parser')
songs_tag = soup.select('li h3')
song_titles = [song.text.strip() for song in songs_tag]
print(song_titles)
