class Classifier(object):
    """docstring for Classifier"""
    def __init__(self, trainData, tokenizer):
        super(Classifier, self).__init__()
        self.trainData = trainData
        self.tokenizer = tokenizer
        self.defaultProb = 0.00000000001

    # ali ata bak
    def classify(self, text):
        
        documentCount = self.getDocumentCount()
        

        tokens = self.tokenizer.tokenize(text)

        classTokenProbs = {}

        for token in tokens:
            classes = self.trainData['classCounts'].keys()
            for classes_i in classes:
                
                tokenProb = self.getTokenProb(token, classes_i)

                if classTokenProbs.get(classes_i) is None:
                    classTokenProbs[classes_i] = {}

                if (tokenProb is not None):
                    classTokenProbs[classes_i][token] = self.getTokenProb(token, classes_i)
                else:
                    classTokenProbs[classes_i][token] = self.defaultProb

        
        #p(S|Class_i)
        probablities = {}
        print 
        print classTokenProbs
        for className, tokenProbs in classTokenProbs.items():
            for tokenProb in tokenProbs.values():
                if probablities.get(className, None) is None:
                    probablities[className] = tokenProb
                else:
                    probablities[className] *= tokenProb

        for className, probablity in probablities.items():
            probablities[className] = float(probablity) * self.getPrior(className)

        return probablities

    def getClassDocumentCount(self, className):
        return self.trainData['classCounts'][className]

    def getDocumentCount(self):
        return sum(self.trainData['classCounts'].values())

    def getPrior(self, className):
        return float(self.getClassDocumentCount(className)) /  float(self.getDocumentCount())

    def getTokenProb(self, token, className):
        if self.trainData['frequencies'].get(token) is None:
            return None
            
        for tclassName, tokenFrequency in self.trainData['frequencies'][token].items():
            if (className is not tclassName):
                continue

            classDocumentCount = self.getClassDocumentCount(className)
            #p(token|Class_i)
            probablity = float(tokenFrequency) / float(classDocumentCount)
            return probablity

        return None