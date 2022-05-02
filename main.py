from twitch_listener import listener
import counter
import secrets

# Connect to Twitch
bot = listener.connect_twitch(secrets.id, secrets.oAuth, secrets.clientID)

# List of channels to connect to
channels_to_listen_to = ['HasanAbi']

# Scrape live chat data into raw log files. (Duration is seconds)
bot.listen(channels_to_listen_to, duration = 5)

# Convert log files into .CSV format
bot.parse_logs(timestamp = True)

print(counter.foo(channels_to_listen_to, 'poggers'))
#ok