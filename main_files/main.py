from twitch_listener import listener
import counter
import os
from dotenv import load_dotenv
load_dotenv()

print('Insert twitch streamers:')
twitch_streamers = input()
print('How long would you like to listen to chat?')
duration = int(input())

# Connect to Twitch
bot = listener.connect_twitch(os.environ['ID'], os.environ['OAUTH'], os.environ['CLIENTID'])

# List of channels to connect to
channels_to_listen_to = [twitch_streamers]

# Scrape live chat data into raw log files. (Duration is seconds)
bot.listen(channels_to_listen_to, duration)

print(counter.foo(channels_to_listen_to, 'poggers'))
