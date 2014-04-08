import tokenizer
from classifier import Classifier
class Trainer(object):
    
    """docstring for Trainer"""
    def __init__(self, tokenizer):
        super(Trainer, self).__init__()
        self.tokenizer = tokenizer
        self.data = {
            'classCounts' : {},
            'frequencies' : {}
        }

    def train(self, text, className):
        
        self.data['classCounts'][className] = self.data['classCounts'].get(className, 0) + 1

        tokens = self.tokenizer.tokenize(text)
        for token in tokens:

            if self.data['frequencies'].get(token) is None:
                self.data['frequencies'][token] = {}

            try:
                self.data['frequencies'][token][className] += 1

            except:
                self.data['frequencies'][token][className] = 1

