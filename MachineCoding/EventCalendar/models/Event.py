from time import time


class Event(object):

    _name = None 
    _userParticipants = None 
    _timeSlot = None 

    def __init__(self,name,userParticipants,timeSlot):
        self._name = name 
        self._userParticipants = userParticipants 
        self._timeSlot = timeSlot 
    
    def getName(self):
        return self._name 
    
    def getUserParticipants(self):
        return self._userParticipants 
    
    def getTimeSlot(self):
        return self._timeSlot 
    
