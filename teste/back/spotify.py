import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
class Tracks():
    def __init__(self,category):
        self.category = self.tracks(category)
        
    def tracks(self,category):

        sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="9b40b39fd4cd4fc29d4a33a6d56ad377",client_secret="fee39f10acd941af80ac03ed87b6e65b"))
        listTracks = []
        results = sp.search(q=category, limit=5)
        for idx, track in enumerate(results['tracks']['items']):
            listTracks.append(track['name'])

        return listTracks

