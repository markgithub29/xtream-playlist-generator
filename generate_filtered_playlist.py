import requests
import re
import json

# Load Xtream login details from xtream_login.json
with open("xtream_login.json", "r") as file:
    config = json.load(file)

XTREAM_HOST = config["host"]
USERNAME = config["username"]
PASSWORD = config["password"]

# M3U Playlist URL
M3U_PLAYLIST_URL = f"{XTREAM_HOST}/get.php?username={USERNAME}&password={PASSWORD}&type=m3u_plus&output=ts"

# Target categories to filter
TARGET_CATEGORIES = ["India", "Telugu"]

# Fetch the M3U playlist
try:
    response = requests.get(M3U_PLAYLIST_URL)
    if response.status_code != 200:
        print(f"Failed to fetch the M3U playlist. Status code: {response.status_code}")
        exit()

    m3u_content = response.text
except Exception as e:
    print(f"Error fetching the playlist: {e}")
    exit()

# Parse and filter M3U content
lines = m3u_content.splitlines()
filtered_playlist = ["#EXTM3U"]
current_category = None

for line in lines:
    if line.startswith("#EXTINF"):
        # Extract the category from the EXTINF line
        category_match = re.search(r'group-title="([^"]+)"', line)
        if category_match:
            current_category = category_match.group(1)

        # Add line if category matches
        if current_category in TARGET_CATEGORIES:
            filtered_playlist.append(line)
    elif line.startswith("http") and current_category in TARGET_CATEGORIES:
        # Add the stream URL
        filtered_playlist.append(line)

# Save the filtered playlist
output_file = "filtered_playlist.m3u"
with open(output_file, "w") as file:
    file.write("\n".join(filtered_playlist))

print(f"Filtered playlist saved as {output_file}")
