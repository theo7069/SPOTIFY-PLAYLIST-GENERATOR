import requests
from bs4 import BeautifulSoup
import spotipy
import os
from spotipy import SpotifyException
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="https://example.com/callback",
                                               scope="playlist-modify-private playlist-modify-public"))


user_id = sp.current_user()["id"]


date = input("Enter the date of the playlist in YYYY-MM-DD: ")

playlist = sp.user_playlist_create(user=user_id, name="My Playlist", public=True)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'}
url = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

song_names_spans = soup.select("li ul li h3")
song_names = [song.get_text().strip() for song in song_names_spans]

for song in song_names:
    try:
        result = sp.search(q=song, type="track", limit=1)
        items = result["tracks"]["items"]

        if not items:
            print(f"❌ No match found on Spotify: {song}")
            continue

        track_uri = items[0]["uri"]
        sp.playlist_add_items(playlist_id=playlist["id"], items=[track_uri])
        print(f"✅ Added: {song}")

    except SpotifyException as e:
        print(f"🚫 Spotify API error with {song}: {e}")
    except Exception as e:
        print(f"❗ Unexpected error with {song}: {e}")




