# -*- coding: utf-8 -*-
from twitterscraper import query_tweets

if __name__ == '__main__':
    list_of_tweets = query_tweets("BTS OR KPOP", 10)

    #print the retrieved tweets to the screen:
    for tweet in query_tweets("BTS OR KPOP", 10000):
        print(tweet)

    #Or save the retrieved tweets to file:
    file = open("BTSoutput.json","w")
    for tweet in query_tweets("BTS OR KPOP", 10000):
        # file.write(tweet.encode("utf-8
        file.write(str(tweet.text.encode('utf-8')))
    file.close()
