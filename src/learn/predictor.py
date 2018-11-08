import argparse


class Predictor:
    def __init__(self, model_file):
        """
        :param model_file: The serialized model with which to make predictions
        """
        pass

    def main(self):
        print('hello from predictor')
        args = self.parser().parse_args()
        raise NotImplementedError

    def parser(self):
        parser = argparse.ArgumentParser(description='Machine Learning System Manager')
        parser.add_argument('-V', '--verbose', action='store_true', help='Print debug information')
        return parser

    def predict(self, feature_vector: list):
        """Predicts a value for the feature vector using the model"""
        raise NotImplementedError


if __name__ == 'main':
    Predictor().main()
