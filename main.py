import json
from datetime import date

from questionary import prompt
from spotipy import SpotifyOAuth, Spotify

"""
Script to backup liked songs from Spotify to a local JSON file.
"""

CREDENTIALS_FILE = 'credentials.json'
TRACKS_PER_REQUEST = 50
SCOPE = 'user-library-read'


def load_credentials() -> dict[str, str]:
    try:
        with open(CREDENTIALS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return prompt_credentials()


def prompt_credentials() -> dict[str, str]:
    credentials = prompt(
        [
            {
                'type': 'input',
                'name': 'client_id',
                'message': 'Enter your Spotify client ID:',
            },
            {
                'type': 'input',
                'name': 'client_secret',
                'message': 'Enter your Spotify client secret:',
            },
            {
                'type': 'input',
                'name': 'redirect_uri',
                'message': 'Enter your Spotify redirect URI:',
            },
        ]
    )
    credentials = {key: value.strip() for key, value in credentials.items()}
    with open(CREDENTIALS_FILE, 'w') as file:
        json.dump(credentials, file)
    return credentials


def authenticate_spotify(credentials: dict[str, str]) -> Spotify:
    auth_manager = SpotifyOAuth(
        client_id=credentials['client_id'],
        client_secret=credentials['client_secret'],
        redirect_uri=credentials['redirect_uri'],
        scope=SCOPE,
    )
    return Spotify(auth_manager=auth_manager)


def backup_liked_songs(spotify: Spotify) -> None:
    track_backup = []
    offset = 0

    while True:
        tracks = spotify.current_user_saved_tracks(limit=TRACKS_PER_REQUEST, offset=offset)
        if not tracks['items']:
            break
        track_backup.extend(tracks['items'])
        offset += TRACKS_PER_REQUEST

    file_name = f"spotify_backup_{date.today()}.json"
    with open(file_name, 'w') as file:
        json.dump(track_backup, file, indent=4)

    print(f'Backup of {len(track_backup)} songs saved to {file_name}')


def main():
    credentials = load_credentials()
    spotify = authenticate_spotify(credentials=credentials)
    backup_liked_songs(spotify=spotify)


if __name__ == '__main__':
    main()
