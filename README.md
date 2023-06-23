# Channel Statistics Obtainer

This project allows you to obtain channel statistics for any YouTube channel using the YouTube Data API.

## Prerequisites

- Acquire an API key from Google. You can obtain it from the Google Developers Console.
- Install the `google-api-python-client` package. You can do this by running the following command:

## Usage

1. Place your API key in the `api_key` variable provided in the code.
2. Create an instance of the `YTstats` class, passing your API key and the channel ID as parameters. For example:

```python
channel_id = "YOUR_CHANNEL_ID"
yt = YTstats(api_key, channel_id)
```
## Methods
1. get_subcribers(): Obtain the number of subscribers for the channel.
2. get_channel_statistics(): Obtain a dictionary containing various channel statistics.
```python
get_subscribers(self):
get_channel_statistics(self):
```