
Problem Statement

StreamFlix is a movie streaming platform that manages users, movies, and subscriptions. Users can watch movies, and the system should track which movies are watched, subscription status, and movie availability.  

You are required to implement this system using Python **OOP concepts**, following the class diagram and rules provided.

---

## Class Diagram

                 +-------------------------------+
                 |            Movie              |
                 +-------------------------------+
                 | - movie_id : str              |
                 | - title : str                 |
                 | - genre : str                 |
                 | - available : bool            |
                 +-------------------------------+
                 | + __init__(id, title, genre)  |
                 | + get_movie_id() : str        |
                 | + get_title() : str           |
                 | + check_availability() : bool|
                 | + set_availability(status)    |
                 +-------------------------------+

                         1
                         |
                         | Aggregation (Has-A)
                         ◇
                         |
                         |
                 +-------------------------------+
                 |             User              |
                 +-------------------------------+
                 | - user_id : int               |
                 | - user_name : str             |
                 | - subscription_active : bool  |
                 | - watched_movies : list       |
                 +-------------------------------+
                 | + __init__(id, name, subscription) |
                 | + get_user_id() : int          |
                 | + get_user_name() : str        |
                 | + watch_movie(movie)           |
                 | + cancel_subscription()        |
                 +-------------------------------+

                         ^
                         |
                         | Association (Uses)
                         |
                 +-------------------------------+
                 |          StreamingPlatform    |
                 +-------------------------------+
                 | - platform_name : str         |
                 +-------------------------------+
                 | + __init__(name)              |
                 | + play_movie(user, movie)     |
                 | + deactivate_user(user)       |
                 +-------------------------------+


---

## Class Descriptions

### Movie Class

**Attributes:**
- `movie_id` – Unique identifier for the movie.  
- `title` – Title of the movie.  
- `genre` – Movie genre (e.g., Action, Drama).  
- `available` – Boolean indicating whether the movie is available to stream.  

**Methods:**
1. `__init__(id, title, genre)` – Initializes movie and sets `available = True`.  
2. `get_movie_id()` – Returns movie ID.  
3. `get_title()` – Returns movie title.  
4. `check_availability()` – Returns `True` if movie is available.  
5. `set_availability(status)` – Updates movie availability.  

---

### User Class

**Attributes:**
- `user_id` – Unique user ID.  
- `user_name` – Name of the user.  
- `subscription_active` – Boolean indicating if the subscription is active.  
- `watched_movies` – List of Movie objects watched by the user.  

**Methods:**
1. `__init__(id, name, subscription)` – Initializes user with subscription status and empty `watched_movies`.  
2. `get_user_id()` – Returns user ID.  
3. `get_user_name()` – Returns user name.  
4. `watch_movie(movie)` – Allows user to watch movie if:  
   - Subscription is active.  
   - Movie is available.  
   Returns `"Movie started"` if successful, else `-1`.  
5. `cancel_subscription()` – Deactivates subscription and prevents watching movies.  

---

### StreamingPlatform Class

**Attributes:**
- `platform_name` – Name of the streaming platform.  

**Methods:**
1. `__init__(name)` – Initializes platform name.  
2. `play_movie(user, movie)` – Uses User and Movie objects to start movie. Returns `"Movie started"` or `-1`.  
3. `deactivate_user(user)` – Cancels user subscription. Returns `"Subscription cancelled"` or `-1` if already inactive.  

---

## Rules and Constraints

1. User cannot watch movies if **subscription is inactive**.  
2. Movie must be **available** to stream.  
3. Watching a movie adds it to the **user’s watched_movies list**.  
4. Users can cancel subscription anytime, which prevents streaming.  
5. Aggregation: User “has-a” Movie.  
6. StreamingPlatform uses association to interact with User and Movie.  

---

## Expected Behavior

| Scenario | Output |
|----------|--------|
| Successful watch | `"Movie started"` |
| Watching without subscription | `-1` |
| Watching unavailable movie | `-1` |
| Successful subscription cancellation | `"Subscription cancelled"` |
| Cancelling already inactive subscription | `-1` |

---

## Sample Usage

```python
# Create Movies
m1 = Movie("M101", "Inception", "Sci-Fi")
m2 = Movie("M102", "Titanic", "Drama")

# Create User
u1 = User(501, "Charlie", True)

# Create Streaming Platform
platform = StreamingPlatform("StreamFlix")

# Play movies
print(platform.play_movie(u1, m1))  # Movie started
print(platform.play_movie(u1, m2))  # Movie started

# Cancel subscription
print(platform.deactivate_user(u1)) # Subscription cancelled
print(platform.play_movie(u1, m1))  # -1 (subscription inactive)

# Set movie unavailable
m2.set_availability(False)
u2 = User(502, "Dana", True)
print(platform.play_movie(u2, m2)) # -1 (movie unavailable)