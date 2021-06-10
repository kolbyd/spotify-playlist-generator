import os
import spotipy
from datetime import date
from dotenv import load_dotenv
from termcolor import colored


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]


# Check if the environment file exists
if os.path.exists('.env'):
    load_dotenv()
    pass
else:
    with open('.env', 'x') as f:
        f.write("# .env\n"
                "SPOTIFY_CLIENT_ID=\n"
                "SPOTIFY_CLIENT_SECRET=")
    print(colored("Fill in the required fields in '.env'.", "yellow"))
    exit(1)

# Ensure we have our ID and secret from Spotify's API
if os.getenv("SPOTIFY_CLIENT_ID") is None or os.getenv("SPOTIFY_CLIENT_SECRET") is None:
    print(colored("Ensure you have included your Spotify credentials. If you don't have them, please make an app at "
          "developer.spotify.com", "red"))
    exit(1)

print("Connecting to Spotify. " + colored("Check your browser in case there is a login prompt.", "yellow"))

spotify = spotipy.Spotify(auth_manager=spotipy.oauth2.SpotifyOAuth(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
    redirect_uri="http://localhost:8080/callback/",
    scope="user-library-read playlist-modify-public playlist-modify-private")
)

print("Connected to Spotify successfully. Starting the converter.")

flag = True  # Spotify doesn't want to return all liked songs. Set to false when done.
offset = 0  # Offset to spotify songs
tracks = []

while flag:
    chunk = spotify.current_user_saved_tracks(50, offset)

    for track in chunk['items']:
        tracks.append(track['track']['uri'])

    if chunk['next'] is None:
        flag = False

    offset += 50

# Check if the user wants the playlist to be public
playlist_public = input(colored("Do you want the playlist to be public? (y/n)", "green") +
                        colored(" [n] ", "yellow")).lower() == "y"

new_playlist = spotify.user_playlist_create(spotify.current_user()['id'],
                                            "Liked Songs - " + date.today().strftime("%m-%d-%Y"),
                                            playlist_public,
                                            description="Auto generated from this user's liked songs.")

# Use chunks of 100 due to Spotify limitations
for chunk in chunks(tracks, 100):
    spotify.playlist_add_items(new_playlist['id'], chunk)

print("Complete! Check out your new playlist at " + new_playlist['external_urls']['spotify'])
