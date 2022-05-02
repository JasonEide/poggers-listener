from twitch_listener import listener
import counter
import os

id = os.environ['id']
clientID = os.environ['clientID']
oAuth = os.environ['oAuth']

# Connect to Twitch
bot = listener.connect_twitch(id, oAuth, clientID)

# List of channels to connect to
channels_to_listen_to = ['Tyler1']

# Scrape live chat data into raw log files. (Duration is seconds)
bot.listen(channels_to_listen_to, duration=5)

print(counter.foo(channels_to_listen_to, 'poggers'))
