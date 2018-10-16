import json

tweetsFile = open("tweets.json", "r")

data = json.load(tweetsFile)

print(data[1]["hashtags"])

for tweet in data:
    print(tweet["hashtags"])

# for x in range(len(data)):
#     print(data[x]["id"])
