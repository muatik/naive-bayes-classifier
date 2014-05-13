from __future__ import division
import operator
from functools import reduce

from ExceptionNotSeen import NotSeen

class Classifier(object):
    """docstring for Classifier"""
    def __init__(self, trainedData, tokenizer):
        super(Classifier, self).__init__()
        self.data = trainedData
        self.tokenizer = tokenizer
        self.defaultProb = 0.000000001

    # ali ata bak
    def classify(self, text):
        
        documentCount = self.data.getDocCount()
        classes = self.data.getClasses()

        # only unique tokens
        tokens = list(set(self.tokenizer.tokenize(text)))
        
        probsOfClasses = {}

        for className in classes:
            
            # we are calculating the probablity of seeing each token 
            # in the text of this class
            # P(Token_1|Class_i)
            tokensProbs = [self.getTokenProb(token, className) for token in tokens]
            
            # calculating the probablity of seeing the the set of tokens
            # in the text of this class
            # P(Token_1|Class_i) * P(Token_2|Class_i) * ... * P(Token_n|Class_i)
            try:
                tokenSetProb = reduce(lambda a,b: a*b, (i for i in tokensProbs if i) ) 
            except:
                tokenSetProb = 0
            
            probsOfClasses[className] = tokenSetProb * self.getPrior(className)
        
        return sorted(probsOfClasses.items(), 
            key=operator.itemgetter(1), 
            reverse=True)


    def getPrior(self, className):
        return self.data.getClassDocCount(className) /  self.data.getDocCount()

    def getTokenProb(self, token, className):
        #p(token|Class_i)
        classDocumentCount = self.data.getClassDocCount(className)

        # if the token is not seen in the training set, so not indexed,
        # then we return None not to include it into calculations.
        try:
            tokenFrequency = self.data.getFrequency(token, className)
        except NotSeen as e:
            return None

        # this means the token is not seen in this class but others.
        if tokenFrequency is None:
            return self.defaultProb

        probablity =  tokenFrequency / classDocumentCount
        return probablity