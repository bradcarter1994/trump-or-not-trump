import argparse


class Experimenter:
    def __init__(self):
        pass

    def main(self):
        raise NotImplementedError

    def parser(self):
        parser = argparse.ArgumentParser(description='Machine Learning System Manager')
        parser.add_argument('-V', '--verbose', action='store_true', help='Print debug information')
        return parser

    def run_experiments(self):
        raise NotImplementedError


if __name__ == 'main':
    Experimenter().main()
