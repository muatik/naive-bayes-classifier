from __future__ import division

class Classifier(object):
    """docstring for Classifier"""
    def __init__(self, trainedData, tokenizer):
        super(Classifier, self).__init__()
        self.data = trainedData
        self.tokenizer = tokenizer
        self.defaultProb = 0.00000000001

    # ali ata bak
    def classify(self, text):
        
        documentCount = self.data.getDocCount()
        classes = self.data.getClasses()
        tokens = self.tokenizer.tokenize(text)
        probsByClasses = {}

        for className in classes:
            #P(Token_1|Class_i), P(Token_2|Class_i),..., P(Token_n|Class_i)
            tokenProbs = [self.getTokenProb(token, className) for token in tokens]
            
            #P(Token_1|Class_i) * P(Token_2|Class_i) * ... * P(Token_n|Class_i)
            probInClass = reduce(lambda a,b: a*b, {i for i in tokenProbs if i} ) 
            
            probsByClasses[className] = probInClass / self.getPrior(className)

        return probsByClasses


    def getPrior(self, className):
        return self.data.getClassDocCount(className) /  self.data.getDocCount()

    def getTokenProb(self, token, className):
        #p(token|Class_i)
        classDocumentCount = self.data.getClassDocCount(className)
        tokenFrequency = self.data.getFrequency(token, className)
        if not tokenFrequency:
            return self.defaultProb

        probablity =  tokenFrequency / classDocumentCount
        return probablity