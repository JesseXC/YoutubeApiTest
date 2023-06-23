import requests
from googleapiclient.discovery import build


api_key = 'YOUR_API_KEY'

youtube = build('youtube', 'v3', developerKey=api_key)


class ChannelStats:
    def __init__(self, apikey, channels=['Youtube']):
        self.api_key = apikey
        self.channels = [channel for channel in channels]
        self.channel_statistics = []
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)

    def get_channel_statistics(self):
        for channel in self.channels:
            request = self.youtube.channels().list(
                part='statistics',
                forUsername=channel
            )
            response = request.execute()
            self.channel_statistics.append(response['items'][0]['statistics'])
        return self.channel_statistics

    def get_subscribers(self, channel_name):
        return int(self.channel_statistics[self.channels.index(channel_name)]['subscriberCount'])

    def battle_subcriberCount(self):
        if len(self.channels) == 1:
            return self.get_subscribers(self.channels[0])
        max_info = [self.get_subscribers(self.channels[0]), self.channels[0]]
        for i in range(1, len(self.channels)):
            if self.get_subscribers(self.channels[i]) > max_info[0]:
                max_info = [self.get_subscribers(self.channels[i]), self.channels[i]]
        print(f"The Winner of the Subscriber Battle is: {max_info[1]} with {max_info[0]} subscribers!")
        return max_info

    def add_channel(self, channel_name):
        self.channels.append(channel_name)


CNN_Fox_Info = ChannelStats(api_key, ["CNN", "FoxNews"])

print(CNN_Fox_Info.get_channel_statistics())
print(CNN_Fox_Info.get_subscribers("CNN"))
max_subscribed = CNN_Fox_Info.battle_subcriberCount()
