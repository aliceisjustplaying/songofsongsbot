import tweepy
import random
from dotenv import load_dotenv
import os


# To choose the line to tweet
def random_line(possible_output):
    lines = possible_output
    return random.sample(lines, 1)[0]  # n= the number of items to print


# print(random_line(possible_output))


all_lines = open("songofsongs.txt", "r").read().splitlines()
already_tweeted = open("tweeted.txt", "r").read().splitlines()
possible_output = [item for item in all_lines if item not in already_tweeted]
print(possible_output)
if len(possible_output) == 0:
    os.system("mv tweeted.txt tweeted.bak && touch tweeted.txt")
    possible_output = all_lines

myline = random_line(possible_output)

file_object = open("tweeted.txt", "a")
file_object.write(myline + "\n")
file_object.close()

load_dotenv()

auth = tweepy.OAuthHandler(
    os.getenv("TWITTER_CONSUMER_KEY"), os.getenv("TWITTER_CONSUMER_SECRET")
)
auth.set_access_token(
    os.getenv("TWITTER_REQUEST_TOKEN"),
    os.getenv("TWITTER_REQUEST_TOKEN_SECRET"),
)
api = tweepy.API(auth)
api.update_status(myline)

"""
# To test access to Twitter
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

api.update_status("Test tweet from Tweepy Python")
"""
