# In this project, you will visualize the feelings and language used in a set of Tweets. This starter code loads the appropriate libraries and the Twitter data you'll need!
print("Hello World")
import json

from textblob import TextBlob

import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("tweets.json", "r")

tweetData = json.load(tweetFile)

tweetFile.close()


# create a sentiment list
polarity = []

#Use a for loop to get the sentiment data (text data)
for x in tweetData:
    tb = TextBlob(x["text"])
    # print(tb)
    print(tweetData(x["text"])
    # polarity = polarity.append([tb])

print("Hello World")

# print your final sentiment lists
# You know it's working if you get a bunch of numbers back

# # Textblob sample:
# tb = TextBlob("You are a brilliant computer scientist.")
#
# print(tb.polarity)
