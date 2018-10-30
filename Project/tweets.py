import sys
import os
import helpers
from analyzer import Analyzer
from termcolor import *
import colorama
colorama.init()

if len(sys.argv) != 2:
    sys.exit("Usage: python tweets.py @screen_name")

app = sys.argv[1]

positives = os.path.join(sys.path[0], "positive-words.txt")
negatives = os.path.join(sys.path[0], "negative-words.txt")

tweets = helpers.get_user_timeline(app, 50)

if tweets == None:
    sys.exit("Error, unable to access user's tweets")

analyzer = Analyzer(positives, negatives)

for tweet in tweets:
    c = analyzer.analyze(tweet)
    print(tweet, end=" ")
    if c > 0:
        cprint(":)", "green")
    elif c < 0:
        cprint(":(", "red")
    else:
        cprint(":|", "yellow")