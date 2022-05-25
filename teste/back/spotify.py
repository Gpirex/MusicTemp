import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="9b40b39fd4cd4fc29d4a33a6d56ad377",client_secret="fee39f10acd941af80ac03ed87b6e65b"))

results = sp.search(q='party', limit=5)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])


