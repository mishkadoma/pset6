# import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        self.positives = open(positives, 'r')
        self.negatives = open(negatives, 'r')
        self.score = 0

        self.positive_list = []
        self.negative_list = []

        for item in self.positives:
            if not item.startswith(';') or item.startswith(' '):
                for word in item:
                    positive_list.append(word.strip())

        for item_2 in self.negatives:
            if not item.startswith(';') or item.startswith(' '):
                for word in item_2:
                    negative_list.append(word.strip())


    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        text = text.split(' ')
        word_array = {}
        initial_score = 0
        for word in text:
            word_array[word] = 0
            if word in positive_list:
                word_array[word] += 1
            elif word in negative_list:
                word_array[word] -= 1

        for word, word_score in word_array:
            score = initial_score + word_score


        return score
