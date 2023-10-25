from abc import ABC

class Participant(ABC):
    __name = None 
    def __init__(self,name):
        self.__name = name 
    
    def getName(self):
        return self.__name
    