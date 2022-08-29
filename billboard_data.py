import requests
from bs4 import BeautifulSoup
from spotify import Spotify
import lxml


class Billboard:
    songs = []

    def __init__(self):
        self.search_date = input("Enter date as YYYY-MM-DD: ")
        request = requests.get(url=f"https://www.billboard.com/charts/hot-100/{self.search_date}")
        soup = BeautifulSoup(request.text, parser="lxml", features="lxml")
        song_names = soup.select(selector=".o-chart-results-list__item .c-title")
        for song in song_names:
            self.songs.append(song.getText().strip())

        self.sp = Spotify(self.songs, self.search_date, int(self.search_date.split("-")[0]))
        self.sp.searchSongs()
        self.sp.create_playlist()