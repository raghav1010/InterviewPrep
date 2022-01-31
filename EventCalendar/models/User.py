from Participant import Participant

class User(Participant):

    _team = None 
    _events = None 
    _workingHours = None 

    def __init__(self,name,workingHours):
        super.__init__(name)
        self._workingHours = workingHours
        self._events = dict() 
    
    def setTeam(self,team):
        self._team = team 
    
    def getTeam(self):
        return self._team 
    
    def getEvents(self):
        return self._events 
    
    def getWorkingHours(self):
        return self._workingHours 

    