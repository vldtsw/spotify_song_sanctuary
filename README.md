## Spotify Liked Songs Backup
This script allows you to backup your liked songs from Spotify to a local JSON file.

### Installation
1. Clone or download this repository.
2. Install the required Python packages by running the following command in the project directory:

`pip install -r requirements.txt`
3. Run the script by executing the following command:

`python main.py`

**Note**: If this is your first time running the script, you will be prompted to enter your Spotify client ID, client secret, and redirect URI. These credentials are necessary for authentication and will be securely stored in a credentials.json file.

After entering the credentials, you will be automatically redirected to a link provided by Spotify. Grant the necessary permissions and copy the redirected URL.

**Important**: Paste the redirected URL back into the terminal for successful authentication.
The script will authenticate with Spotify using the provided credentials and start backing up your liked songs. 

Once the backup is complete, a JSON file named `spotify_backup_<date>.json` will be created in the same directory. This file contains the details of your liked songs.

### Additional Information

The backup file is overwritten each time you run the script, so make sure to save a copy if needed.

The .gitignore file is configured to exclude the credentials.json file and any backup files from being committed to the repository.

### Getting Spotify Credentials

To use this script, you need to obtain the following credentials from the Spotify Developer Dashboard:

+ Client ID: Unique identifier for your application.
+ Client Secret: Secret key used for authenticating your application.
+ Redirect URI: URL where the user will be redirected after authentication.

Make sure to have these credentials ready before running the script for the first time.