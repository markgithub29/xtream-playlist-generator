import json
import requests

# Load Xtream credentials
with open("xtream_login.json", "r") as file:
    credentials = json.load(file)

# Xtream API endpoints
host = credentials["host"]
username = credentials["username"]
password = credentials["password"]

# Fetch categories
categories_url = f"{host}/player_api.php?username={username}&password={password}&action=get_live_categories"
categories_response = requests.get(categories_url)
categories = categories_response.json()

# Filter for desired category (e.g., "India Channels")
filtered_category_id = None
for category in categories:
    if category["category_name"] == "India Channels":
        filtered_category_id = category["category_id"]
        break

if not filtered_category_id:
    raise Exception("Category not found!")

# Fetch streams for the category
streams_url = f"{host}/player_api.php?username={username}&password={password}&action=get_live_streams&category_id={filtered_category_id}"
streams_response = requests.get(streams_url)
streams = streams_response.json()

# Generate playlist
playlist = []
for stream in streams:
    playlist.append(f"#EXTINF:-1 tvg-logo=\"{stream['stream_icon']}\" group-title=\"{stream['category_name']}\",{stream['name']}")
    playlist.append(f"{host}/live/{username}/{password}/{stream['stream_id']}.m3u8")

# Save to file
with open("filtered_playlist.m3u", "w") as file:
    file.write("\n".join(playlist))
