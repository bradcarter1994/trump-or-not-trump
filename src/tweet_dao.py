import sqlite3
import tweepy


class TweetDAO:
    def __init__(self, db_path, clear_db=True):
        # Create the database file if it doesn't exist
        open(db_path, 'w+').close()
        self.connection = sqlite3.connect(db_path)
        c = self.connection.cursor()
        if clear_db:
            c.execute('DROP TABLE IF EXISTS tweet')
        c.execute('''CREATE TABLE IF NOT EXISTS tweet (
                        tweet_id INTEGER PRIMARY KEY, 
                        handle TEXT, 
                        creation_time DATETIME, 
                        full_text TEXT)''')
        self.connection.commit()

    def __del__(self):
        self.connection.close()

    def insert_tweets(self, tweets: [tweepy.Status]):
        c = self.connection.cursor()
        fields = [(tweet.author.screen_name, tweet.created_at, tweet.full_text) for tweet in tweets]
        c.executemany('INSERT INTO tweet (handle, creation_time, full_text) VALUES (?, ?, ?)', fields)
        self.connection.commit()




