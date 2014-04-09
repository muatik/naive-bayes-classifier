import tokenizer
from classifier import Classifier
from trainedData import TrainedData

class Trainer(object):
    
    """docstring for Trainer"""
    def __init__(self, tokenizer):
        super(Trainer, self).__init__()
        self.tokenizer = tokenizer
        self.data = TrainedData()

    def train(self, text, className):
        """
        enhances trained data using the given text and class
        """
        self.data.increaseClass(className)

        tokens = self.tokenizer.tokenize(text)
        for token in tokens:
            self.data.increaseToken(token, className)



t = Trainer(tokenizer)
t.train('bu yaz hava gayet iyi', 'erkek')
t.train('maraba opucem seni sevmiyorum', 'gay')
t.train('seni seviyorum mucuk mucuk opucem seni bu yaz', 'kadin')
t.train('seni bu nedenle sevmiyorum', 'kadin')

c = Classifier(t.data, tokenizer)
print c.classify("bu mucuk maraba")
