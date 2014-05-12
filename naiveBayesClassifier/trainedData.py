from ExceptionNotSeen import NotSeen

class TrainedData(object):
    def __init__(self):
        self.docCountOfClasses = {}
        self.frequencies = {}

    def increaseClass(self, className, byAmount = 1):
        self.docCountOfClasses[className] = self.docCountOfClasses.get(className, 0) + 1

    def increaseToken(self, token, className, byAmount = 1):
        if not token in self.frequencies:
                self.frequencies[token] = {}

        self.frequencies[token][className] = self.frequencies[token].get(className, 0) + 1

    def decreaseToken(self, token, className, byAmount = 1):
        # will be implemented
        pass

    def getDocCount(self):
        """
        returns all documents count
        """
        return sum(self.docCountOfClasses.values())

    def getClasses(self):
        """
        returns the names of the available classes as list
        """
        return self.docCountOfClasses.keys()

    def getClassDocCount(self, className):
        """
        returns document count of the class. 
        If class is not available, it returns None
        """
        return self.docCountOfClasses.get(className, None)

    def getFrequency(self, token, className):

        try:
            foundToken = self.frequencies[token]
        except:
            raise NotSeen(token)

        try:
            return foundToken[className]
        except:
            return None
