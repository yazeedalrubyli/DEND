# DROP TABLES

songplay_table_drop = "DROP table songplays"
user_table_drop = "DROP table users"
song_table_drop = "DROP table songs"
artist_table_drop = "DROP table artists"
time_table_drop = "DROP table time"

# CREATE TABLES
songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays
    (songplay_id SERIAL PRIMARY KEY NOT NULL, 
    user_id INT REFERENCES users(user_id), 
    song_id VARCHAR (255) REFERENCES songs(song_id), 
    artist_id VARCHAR (255) REFERENCES artists(artist_id), 
    start_time TIMESTAMP REFERENCES time(start_time),
    level VARCHAR (4) NOT NULL CHECK (level in ('free', 'paid')),
    location TEXT NOT NULL, 
    session_id INT NOT NULL,
    user_agent TEXT NOT NULL)
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users
    (user_id INT PRIMARY KEY,
    first_name VARCHAR (255) NOT NULL,
    last_name VARCHAR (255) NOT NULL, 
    gender VARCHAR (1) NOT NULL CHECK (gender in ('M', 'F')), 
    level VARCHAR (4) NOT NULL CHECK (level in ('free', 'paid')))
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs
    (song_id VARCHAR (255) PRIMARY KEY,
    title TEXT NOT NULL, 
    artist_id VARCHAR (20) REFERENCES artists(artist_id), 
    year INT NOT NULL, 
    duration FLOAT NOT NULL)
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists
    (artist_id VARCHAR (255) PRIMARY KEY,
    name VARCHAR (255) NOT NULL, 
    location TEXT NOT NULL, 
    latitude FLOAT, 
    longitude FLOAT)
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time
    (start_time TIMESTAMP PRIMARY KEY,
    hour INT, 
    day INT, 
    week INT, 
    month INT, 
    year INT, 
    weekday VARCHAR (10) CHECK (weekday in ('Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')))
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays (user_id, song_id, artist_id, start_time, level, location, session_id, user_agent)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT (songplay_id) DO NOTHING;
""")

user_table_insert = ("""
    INSERT INTO users VALUES (%s, %s, %s, %s, %s) ON CONFLICT (user_id) DO NOTHING;
""")

song_table_insert = ("""
    INSERT INTO songs VALUES (%s, %s, %s, %s, %s);
""")

artist_table_insert = ("""
    INSERT INTO artists VALUES (%s, %s, %s, %s, %s) ON CONFLICT (artist_id) DO NOTHING;
""")


time_table_insert = ("""
    INSERT INTO time VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (start_time) DO NOTHING;
""")

# FIND SONGS

song_select = ("""
    SELECT song_id, songs.artist_id FROM songs
    JOIN artists ON songs.artist_id = artists.artist_id
    WHERE title      = %s
    AND artists.name = %s
    AND duration     = %s
""")

# QUERY LISTS

create_table_queries = [user_table_create, artist_table_create, song_table_create, time_table_create, songplay_table_create]
drop_table_queries = [user_table_drop, song_table_drop, artist_table_drop, time_table_drop, songplay_table_drop]