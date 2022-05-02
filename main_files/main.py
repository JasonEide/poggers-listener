from twitch_listener import listener
import counter
import os
from dotenv import load_dotenv
load_dotenv()

# Connect to Twitch
bot = listener.connect_twitch(os.environ['ID'], os.environ['OAUTH'], os.environ['CLIENTID'])

# List of channels to connect to
channels_to_listen_to = ['HasanAbi']

# Scrape live chat data into raw log files. (Duration is seconds)
bot.listen(channels_to_listen_to, duration=5)

print(counter.foo(channels_to_listen_to, 'k'))
