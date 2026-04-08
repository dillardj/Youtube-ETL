import requests
import json

import os
from dotenv import load_dotenv

# Always resolve .env relative to this file, not the launch working directory.
ENV_PATH = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path=ENV_PATH)


API_KEY = os.getenv("YOUTUBE_API_KEY")
CHANNEL_HANDLE = "MrBeast"

def get_playlist_id():

    try:
        if not API_KEY:
            raise ValueError(f"Missing YOUTUBE_API_KEY. Checked: {ENV_PATH}")

        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"

        response = requests.get(url)

        response.raise_for_status()  # Check if the request was successful

        data = response.json()

        #print(json.dumps(data, indent=4))

        channel_items = data["items"][0]

        channel_playlistId = channel_items["contentDetails"]["relatedPlaylists"]["uploads"]

        print(channel_playlistId)
        
        return channel_playlistId
    except (requests.exceptions.RequestException, ValueError) as e:
        raise e
        #print("An error occurred while fetching the playlist ID.")


#Can call this from another file by setting __name__ = name of the file and then calling the function get_playlist_id()
if __name__ == "__main__":
    get_playlist_id()
