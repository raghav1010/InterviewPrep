from Participant import Participant 

class Team(Participant):

    _teamMembers = None 

    def __init__(self,name):
        super().__init__(name)
        self._teamMembers = list() 
    
    def getTeamMembers(self):
        return self._teamMembers 
    
    def addTeamMember(self,user):
        self._teamMembers.append(user) 
        