import argparse
import tweepy
import json
from src.tweet_dao import TweetDAO


class TweetScrapper:
    def __init__(self):
        pass

    def main(self):
        args = self.parser().parse_args()
        self.scrape(handles=args.handle, hashtags=args.hashtag, database=args.database, clear=args.clear)

    def parser(self):
        parser = argparse.ArgumentParser(description='Tweet Scraper')
        parser.add_argument('-V', '--verbose', action='store_true', help='Print debug information')
        parser.add_argument('-D', '--database', default='data/tweet_db.sqlite', help='The database to scrape tweets to')
        parser.add_argument('-H', '--handle', default=[], nargs='+', help='Twitter handles to scrape')
        parser.add_argument('--hashtag', default=[], nargs='+', help='Twitter hashtags to scrape')
        parser.add_argument('-C', '--clear', action='store_true', help='Print debug information')
        return parser

    def scrape(self, handles: list, hashtags: list, database: str, clear: bool):
        """Scrapes tweets to a local database"""
        api = self.authenticate()
        dao = TweetDAO(database, clear_db=clear)

        for handle in handles:
            tweets = list()
            for tweet in tweepy.Cursor(api.user_timeline, id=handle, lang='en', tweet_mode='extended').items():
                if (not tweet.retweeted) and ('RT @' not in tweet.full_text):
                    tweets.append(tweet)
            dao.insert_tweets(tweets)

        for hashtag in hashtags:
            tweets = list()
            for tweet in tweepy.Cursor(api.search, q=hashtag, lang='en', tweet_mode='extended').items():
                if (not tweet.retweeted) and ('RT @' not in tweet.full_text):
                    tweets.append(tweet)
            dao.insert_tweets(tweets)

    def authenticate(self, cred_path='definitely_not_our_api_keys.json'):
        """Logs into the Twitter API using the credentials stored at cred_path"""
        with open(cred_path) as json_file:
            data = json.load(json_file)
            auth = tweepy.OAuthHandler(data['consumer_key'], data['consumer_secret'])
            auth.set_access_token(data['access_key'], data['access_secret'])
            return tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


if __name__ == '__main__':
    TweetScrapper().main()
