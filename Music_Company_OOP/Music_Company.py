class Song:
    def __init__(self, song_id, title, duration):
        self.__song_id = song_id
        self.__title = title
        self.__duration = duration

    def get_title(self):
        return self.__title

    def get_duration(self):
        return self.__duration

    def get_song_id(self):
        return self.__song_id


class Playlist:
    def __init__(self, playlist_name):
        self.__playlist_name = playlist_name
        self.__song_list = []

    def add_song(self, song):
        self.__song_list.append(song)

    def get_song_list(self):
        return self.__song_list

    def get_playlist_name(self):
        return self.__playlist_name


class PremiumUser:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__playlist_list = []

    def create_playlist(self, playlist):
        self.__playlist_list.append(playlist)

    def get_playlist_list(self):
        return self.__playlist_list

    def get_name(self):
        return self.__name





song1 = Song(1, "Believer", 3.5)
song2 = Song(2, "Perfect", 4.2)
song3 = Song(3, "Faded", 3.8)


playlist1 = Playlist("Workout Hits")
playlist1.add_song(song1)
playlist1.add_song(song2)

playlist2 = Playlist("Chill Vibes")
playlist2.add_song(song3)


user = PremiumUser(101, "Atharva")

user.create_playlist(playlist1)
user.create_playlist(playlist2)


print("User:", user.get_name())
for playlist in user.get_playlist_list():
    print("\nPlaylist:", playlist.get_playlist_name())
    for song in playlist.get_song_list():
        print("  Song ID:", song.get_song_id(),
              "| Title:", song.get_title(),
              "| Duration:", song.get_duration(), "mins")
