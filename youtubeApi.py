import requests

base_url = "https://www.googleapis.com/youtube/v3"
api_key = "AIzaSyAUTGuVJmt1eCA33Se8Nvu1Pl8_KYi8RdU"  # Replace with your actual API key

headers = {
    "Content-Type": "application/json",
}
url = f"{base_url}/videos"
params = {
  "part": "snippet",
  "id": 'iUMgIPlWHO8',
  "key": api_key
}
response = requests.get(url, headers=headers, params=params)
response_json = response.json()
if "items" in response_json:
  title = response_json["items"][0]["snippet"]["title"]
  print("Video title:", title)
else:
  print("Video not found.")

