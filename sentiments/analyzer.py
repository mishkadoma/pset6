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
            if item.startswith(";") == item.startswith(" "):
                item = item.strip().split(' ')
                for word in item:
                    self.positive_list.append(word.strip())

        for item_2 in self.negatives:
            if item_2.startswith(';') == item_2.startswith(" "):
                item_2 = item_2.strip().split(' ')
                for word_2 in item_2:
                    self.negative_list.append(word_2.strip())


    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        text = text.split(' ')
        word_array = {}

        for word in text:
            word_array[word] = 0
            if word in self.positive_list:
                word_array[word] += 1
            elif word in self.negative_list:
                word_array[word] -= 1

        for word in word_array:
            self.score += word_array[word]

        return self.score
