import json
import requests

# Load Xtream credentials
with open("xtream_login.json", "r") as file:
    credentials = json.load(file)

# Xtream API credentials
host = credentials["host"]
username = credentials["username"]
password = credentials["password"]

# Base URL for API requests
base_url = f"{host}/player_api.php?username={username}&password={password}"

# Fetch all live categories
categories_url = f"{base_url}&action=get_live_categories"
categories_response = requests.get(categories_url)

# Check for a valid response
if categories_response.status_code != 200:
    raise Exception("Failed to fetch categories. Check your API credentials.")

categories = categories_response.json()

# Fetch all streams and group by category
playlist = []

for category in categories:
    category_name = category["category_name"]
    category_id = category["category_id"]

    # Fetch streams for the current category
    streams_url = f"{base_url}&action=get_live_streams&category_id={category_id}"
    streams_response = requests.get(streams_url)

    if streams_response.status_code != 200:
        print(f"Failed to fetch streams for category: {category_name}")
        continue

    streams = streams_response.json()

    # Append category header
    playlist.append(f"# Category: {category_name}")

    # Add streams to the playlist
    for stream in streams:
        stream_name = stream["name"]
        stream_id = stream["stream_id"]
        stream_icon = stream.get("stream_icon", "")
        stream_url = f"{host}/live/{username}/{password}/{stream_id}.m3u8"

        # Add stream details to the playlist
        playlist.append(f"#EXTINF:-1 tvg-logo=\"{stream_icon}\" group-title=\"{category_name}\",{stream_name}")
        playlist.append(stream_url)

# Save the playlist to a file
with open("filtered_playlist.m3u", "w") as file:
    file.write("\n".join(playlist))

print("Playlist generated successfully!")
