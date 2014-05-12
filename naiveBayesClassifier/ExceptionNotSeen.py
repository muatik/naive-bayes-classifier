class NotSeen(Exception):
    """
    Exception for tokens which are not indexed 
    because never seen in the trainin data
    """
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return "Token '{}' is never seen in the training set.".format(self.value)