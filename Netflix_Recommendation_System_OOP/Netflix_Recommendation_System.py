import random

class Movie:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    def __str__(self):
        return f"{self.title} ({self.genre}) - {self.rating}"


class User:
    def __init__(self, name):
        self.name = name
        self.__watched = []
        self.__preferred_genres = []

    def add_watched(self, movie):
        self.__watched.append(movie)

    def add_preference(self, genre):
        if genre not in self.__preferred_genres:
            self.__preferred_genres.append(genre)

    def get_watched(self):
        return self.__watched

    def get_preferences(self):
        return self.__preferred_genres


class RecommendationEngine:
    def __init__(self, movies):
        self.movies = movies

    def recommend(self, user, limit=3):
        recommendations = []
        watched = user.get_watched()
        preferences = user.get_preferences()

        for movie in self.movies:
            if movie not in watched and movie.genre in preferences:
                recommendations.append(movie)

        recommendations.sort(key=lambda m: m.rating, reverse=True)

        pool = recommendations[:limit * 2]

        if len(pool) <= limit:
            return pool

        return random.sample(pool, limit)


if __name__ == "__main__":
    m1 = Movie("Inception", "Sci-Fi", 9)
    m2 = Movie("Interstellar", "Sci-Fi", 8.5)
    m3 = Movie("Titanic", "Romance", 8)
    m4 = Movie("Avengers", "Action", 8.7)
    m5 = Movie("The Notebook", "Romance", 7.5)
    m6 = Movie("John Wick", "Action", 8.2)
    m7 = Movie("Matrix", "Sci-Fi", 8.8)

    movies = [m1, m2, m3, m4, m5, m6, m7]

    user = User("Atharva")
    user.add_preference("Sci-Fi")
    user.add_preference("Action")
    user.add_watched(m1)

    engine = RecommendationEngine(movies)

    print(f"\nRecommendations for {user.name}:")
    for movie in engine.recommend(user, limit=3):
        print(movie)