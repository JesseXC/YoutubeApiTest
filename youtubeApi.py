import requests
from googleapiclient.discovery import build

base_url = "https://www.googleapis.com/youtube/v3"
api_key = 'AIzaSyAUTGuVJmt1eCA33Se8Nvu1Pl8_KYi8RdU'
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
# if "items" in response_json:
#   title = response_json["items"][0]["snippet"]["title"]
#   print("Video title:", title)
# else:
#   print("Video not found.")

youtube = build(
  'youtube',
  'v3',
  developerKey = api_key
)

class YTstats:
  def __init__(self,apikey,channel_id):
    self.api_key = apikey
    self.channel_id = channel_id
    self.channel_statistics = None
    self.youtube = build('youtube','v3', developerKey = self.api_key)  

  def get_channel_statistics(self):
    request = youtube.channels().list(
      part = 'statistics',
      forUsername = f'{self.channel_id}'
    )
    response = request.execute()
    self.channel_statistics = response['items'][0]['statistics']
    return self.channel_statistics
  
  def get_subscribers(self):
    return self.channel_statistics['subscriberCount']

CNN_Channel = YTstats(api_key,"CNN")

print(CNN_Channel.get_channel_statistics())
print(CNN_Channel.get_subscribers())
