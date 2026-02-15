class Movie:
    def __init__(self, movie_id, title, genre):
        self.movie_id = movie_id
        self.title = title
        self.genre = genre
        self.available = True

    def get_movie_id(self):
        return self.movie_id

    def get_title(self):
        return self.title

    def check_availability(self):
        return self.available

    def set_availability(self, status):
        self.available = status



class User:
    def __init__(self, user_id, user_name, subscription_active):
        self.user_id = user_id
        self.user_name = user_name
        self.subscription_active = subscription_active
        self.watched_movies = []  

    def get_user_id(self):
        return self.user_id

    def get_user_name(self):
        return self.user_name

    def watch_movie(self, movie):
        if not self.subscription_active:
            return -1 
        if not movie.check_availability():
            return -1 
        self.watched_movies.append(movie)
        return "Movie started"

    def cancel_subscription(self):
        if not self.subscription_active:
            return -1  
        self.subscription_active = False
        return "Subscription cancelled"



class StreamingPlatform:
    def __init__(self, platform_name):
        self.platform_name = platform_name

    def play_movie(self, user, movie):
        return user.watch_movie(movie)

    def deactivate_user(self, user):
        return user.cancel_subscription()






m1 = Movie("M101", "Inception", "Sci-Fi")
m2 = Movie("M102", "Titanic", "Drama")


u1 = User(501, "Charlie", True)
u2 = User(502, "Dana", True)


platform = StreamingPlatform("StreamFlix")


print(platform.play_movie(u1, m1))  
print(platform.play_movie(u1, m2))  


print(platform.deactivate_user(u1)) 


print(platform.play_movie(u1, m1))  


m2.set_availability(False)


print(platform.play_movie(u2, m2))  

print([movie.get_title() for movie in u1.watched_movies])  


print([movie.get_title() for movie in u2.watched_movies]) 
