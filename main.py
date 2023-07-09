from bs4 import BeautifulSoup as bs
import requests
import re
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year do you want to travel to ? Type the date in this format YYYY-MM-DD:")
URL =f"https://www.billboard.com/charts/hot-100/{date}/"
CLIENT_ID = "f28ac597e24a4cd9963097da9293c353"
CLIENT_SECRET ="9e97e6cd61d44b23a4dc4f6773312550"
response = requests.get(URL)
website_html = response.text

soup = bs(website_html,"html.parser")

# print(soup.prettify())
print(soup.title)

songs_title_tag = soup.find_all(name="h3",id="title-of-a-story")
# print(songs_title_tag)
# find all the songs html tags

song_desc = []

for song in songs_title_tag:
    song_desc.append(song.getText().strip())
# """ getText to get only the text and ignore the html tags,
# strip will remove the escape characters
# like  \n \t for each element in list """

song_names = []
for i in range(6,406,4):
    song_names.append(song_desc[i])
    # when going through the list, the first song name is at 6th element,
    # and after every 4 elements next song name is found.
    # 100th song name is at 406th element ==> (100*4 + 6)

print(song_names)


with open("top-100songs.txt",mode="w", encoding="utf-8") as file:
    # create a txt file and write the song names
    # add encoding = "utf-8" to remove UnicodeEncodeError: 'charmap' codec can't encode characters in position 28-29:
    for song in song_names:
        file.write(f"{song}\n")
        # \n to add each song titles in different lines



# 10,14,18,22,



sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    redirect_uri="http://example.com",
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    show_dialog= True ,
    cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
