import requests
import json

# Load Xtream Login Details
with open("xtream_login.json", "r") as file:
    login = json.load(file)

XTREAM_HOST = login["host"]
USERNAME = login["username"]
PASSWORD = login["password"]

# API URLs
BASE_API_URL = f"{XTREAM_HOST}/player_api.php"
LIVE_CATEGORY_URL = f"{BASE_API_URL}?username={USERNAME}&password={PASSWORD}&action=get_live_categories"
STREAMS_URL = f"{BASE_API_URL}?username={USERNAME}&password={PASSWORD}&action=get_live_streams"

# Target categories
TARGET_CATEGORIES = ["India", "Telugu"]

# Fetch live categories
categories_response = requests.get(LIVE_CATEGORY_URL)
categories = categories_response.json()

# Get category IDs for target categories
category_ids = {}
for category in categories:
    if category["category_name"] in TARGET_CATEGORIES:
        category_ids[category["category_name"]] = category["category_id"]

if not category_ids:
    print("Target categories not found!")
    exit()

# Fetch all live streams
streams_response = requests.get(STREAMS_URL)
streams = streams_response.json()

# Filter streams by target categories
filtered_streams = []
for stream in streams:
    if stream["category_id"] in category_ids.values():
        filtered_streams.append(stream)

# Generate M3U playlist
m3u_lines = ["#EXTM3U"]
for stream in filtered_streams:
    tvg_logo = stream.get("stream_icon", "")
    tvg_name = stream.get("name", "Unknown")
    stream_url = f"{XTREAM_HOST}/live/{USERNAME}/{PASSWORD}/{stream['stream_id']}.m3u8"
    m3u_lines.append(f'#EXTINF:-1 tvg-logo="{tvg_logo}" tvg-name="{tvg_name}",{tvg_name}')
    m3u_lines.append(stream_url)

# Save the playlist
output_file = "filtered_playlist.m3u"
with open(output_file, "w") as file:
    file.write("\n".join(m3u_lines))

print(f"Filtered M3U playlist saved as {output_file}")
