from models.Team import Team 
from models.Event import Event
from models.TimeSlot import TimeSlot
from models.User import User

class TeamDao(object):
    _teamMap = None 

    def __init__(self):
        self._teamMap = dict()
    
    def createTeam(self,team):
        if team.getName() in self._teamMap:
            raise RuntimeError("Team exists with given name ", team.getName())
        self._teamMap[team.getName()]= team 

    def getTeam(self,teamName):
        team = self._teamMap.get(teamName,-1)
        if team == -1 :
            raise RuntimeError("Team does not exist")
        return team 
    