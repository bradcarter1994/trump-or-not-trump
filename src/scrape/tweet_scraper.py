import argparse
import tweepy
import csv


class TweetScrapper:
    def __init__(self, screen_name):
        self.screen_name = screen_name
        self.consumer_key = "3QxC9iZXRyIXCCscEYbFqTxte"
        self.consumer_secret = "UO29uocaqpS9a3prhSToGzMjgCAXd3Z4bCAepCuxAkse96cy5H"
        self.access_key = "424518011-stIwYNC9NMWrZAbEoxKepMpJ39pGoB2Rxilct4h9"
        self.access_secret = "HH3vMTzXTvmy3WNskoJBk81jvy6j1pqLlvOBOWZDRB4O4"

    def main(self):
        args = self.parser().parse_args()
        self.scrape()

    def parser(self):
        parser = argparse.ArgumentParser(description='Tweet Scraper')
        parser.add_argument('-V', '--verbose', action='store_true', help='Print debug information')
        return parser

    def scrape(self):
        """Scrapes tweets to a local database"""
        # Twitter only allows access to a users most recent 3240 tweets with this method

        # authorize twitter, initialize tweepy
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_key, self.access_secret)
        api = tweepy.API(auth)

        # initialize a list to hold all the tweepy Tweets
        alltweets = []

        # make initial request for most recent tweets (200 is the maximum allowed count)
        new_tweets = api.user_timeline(screen_name=self.screen_name, count=200, tweet_mode='extended')

        # save most recent tweets
        alltweets.extend(new_tweets)

        # save the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        # keep grabbing tweets until there are no tweets left to grab
        while len(new_tweets) > 0:
            print("getting tweets before: ")
            print(oldest)

            # all subsiquent requests use the max_id param to prevent duplicates
            new_tweets = api.user_timeline(screen_name=self.screen_name, count=200, max_id=oldest, tweet_mode='extended')

            # save most recent tweets
            alltweets.extend(new_tweets)

            # update the id of the oldest tweet less one
            oldest = alltweets[-1].id - 1

            print("tweets downloaded so far: ")
            print(len(alltweets))

        # transform the tweepy tweets into a 2D array that will populate the csv
        outtweets = [[tweet.id_str, tweet.created_at, tweet.full_text.encode("utf-8")] for tweet in alltweets]

        # write the csv
        with open('%s_tweets.csv' % self.screen_name, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["id", "created_at", "text"])
            writer.writerows(outtweets)

        pass



if __name__ == '__main__':
    TweetScrapper("realDonaldTrump").main()
