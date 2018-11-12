import argparse


class TweetScrapper:
    def __init__(self):
        pass

    def main(self):
        args = self.parser().parse_args()
        raise NotImplementedError

    def parser(self):
        parser = argparse.ArgumentParser(description='Tweet Scraper')
        parser.add_argument('-V', '--verbose', action='store_true', help='Print debug information')
        return parser

    def scrape(self):
        """Scrapes tweets to a local database"""
        raise NotImplementedError


if __name__ == '__main__':
    TweetScrapper().main()
