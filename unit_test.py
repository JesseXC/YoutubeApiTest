import unittest
from googleapiclient.discovery import build

from youtubeApi import ChannelStats

api_key = ''
channels = ["CNN", "FoxNews"]


class ChannelStatsTest(unittest.TestCase):

    def setUp(self):
        self.youtube = build('youtube', 'v3', developerKey=api_key)
        self.channel_stats = ChannelStats(api_key, channels)

    def test_get_channel_statistics(self):
        channel_statistics = self.channel_stats.get_channel_statistics()
        self.assertEqual(len(channel_statistics), len(channels))

    def test_add_channel(self):
        initial_channel_count = len(self.channel_stats.channels)
        self.channel_stats.add_channel("BBC")
        new_channel_count = len(self.channel_stats.channels)
        self.assertEqual(new_channel_count, initial_channel_count + 1)  # Assuming one channel was added


if __name__ == '__main__':
    unittest.main()
