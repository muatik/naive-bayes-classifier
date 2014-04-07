class Classifier(object):
    """docstring for Classifier"""
    def __init__(self, trainData, tokenizer):
        super(Classifier, self).__init__()
        self.trainData = trainData
        self.tokenizer = tokenizer

    # ali ata bak
    def classify(self, text):
                
        documentCount = sum(self.trainData['classCounts'].values())
        

        tokens = self.tokenizer.tokenize(text)
        for token in tokens:
            tokenTrain = self.trainData[token]
            pCs[token] = self.findProbInClass(token, tokenTrain)


        for pC in pCs:
            for classProb in pC:

                

    def findProbInClass(self, token, tokenTrainData):
        pCs = {}
        for className, tokenFrequency in enumerate(tokenTrainData):
            classDocumentCount = self.trainData['classCounts'][className
]g            pCs[className] = tokenFrequency / classDocumentCount

        return Pcs