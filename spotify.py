import spotipy as s
from spotipy.oauth2 import SpotifyOAuth


class Spotify:
    def __init__(self, songs, date, year):
        self._client_id = "8b01c42ca5034577925dd72467958145"
        self._client_secret = "7fa687b5c9cf4841b29d54be8907dfde"
        self.auth = SpotifyOAuth(
            client_id=self._client_id,
            client_secret=self._client_secret,
            scope="playlist-modify-public",
            redirect_uri="http://localhost:8080",
            cache_path="token.txt"
        )
        self.auth.get_auth_response()
        self.sp = s.Spotify(auth_manager=self.auth)
        self.songs = songs
        self.year = year
        self.date = date
        self.song_uris = []

    def searchSongs(self):
        for song in self.songs:
            song_uri = self.get_song_details(song, self.year, 0)
            if song_uri is not None:
                self.song_uris.append(song_uri)

    def get_song_details(self, name, year, search_time):
        global song_data
        if search_time > 5: return None
        try:
            song_data = self.sp.search(q=f"track:{name} year:{self.year}", type="track")["tracks"]["items"][0]["uri"]
        except:
            song_data = self.get_song_details(name, year - 1, search_time + 1)
        return song_data

    def create_playlist(self):
        playlist_data = self.sp.user_playlist_create(
            user=self.sp.current_user()["id"],
            name=f"Time Machine {self.date}",
            public=True,
            collaborative=False,
            description=f"A Playlist of Top 100 Billboard songs on the date {self.date}."
        )
        self.sp.playlist_add_items(playlist_data['id'], items=self.song_uris)
        print("Playlist Created.")
