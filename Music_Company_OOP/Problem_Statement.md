# Practice Problem 17

## Problem Statement

A music streaming company wants to manage playlists and premium users.\
Each premium user can create multiple playlists.\
Each playlist can contain multiple songs.

Write a python program to implement the class diagram given below.

------------------------------------------------------------------------

## Class Diagram

    +----------------------+
    |     PremiumUser      |
    +----------------------+
    | - user_id            |
    | - name               |
    | - playlist_list      |
    +----------------------+
    | + __init__(user_id,name)
    | + create_playlist(playlist)
    | + get_playlist_list()
    | + get_name()
    +----------------------+
              1
              |
              | Aggregation
              |
              | 0..*
    +----------------------+
    |       Playlist       |
    +----------------------+
    | - playlist_name      |
    | - song_list          |
    +----------------------+
    | + __init__(playlist_name)
    | + add_song(song)
    | + get_song_list()
    | + get_playlist_name()
    +----------------------+
              1
              |
              | Composition
              |
              | 0..*
    +----------------------+
    |         Song         |
    +----------------------+
    | - song_id            |
    | - title              |
    | - duration           |
    +----------------------+
    | + __init__(song_id,title,duration)
    | + get_title()
    | + get_duration()
    +----------------------+

------------------------------------------------------------------------

## Class Description

### Song class:

1.  song_id: Unique identifier of the song\
2.  title: Name of the song\
3.  duration: Duration of the song in minutes

------------------------------------------------------------------------

### Playlist class:

1.  playlist_name: Name of the playlist\
2.  song_list: List of Song objects\
3.  add_song(song): Add a song object to song_list

------------------------------------------------------------------------

### PremiumUser class:

1.  user_id: Unique identifier\
2.  name: Name of the user\
3.  playlist_list: List of Playlist objects\
4.  create_playlist(playlist): Add a playlist to playlist_list

------------------------------------------------------------------------

Create objects of Song, Playlist and PremiumUser classes, establish
relationships as per diagram and test your program.
