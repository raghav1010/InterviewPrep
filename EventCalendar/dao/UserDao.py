from models.Team import Team 
from models.Event import Event
from models.TimeSlot import TimeSlot
from models.User import User

class UserDao(object):

    __userMap = None 
    def __init__(self):
        self.__userMap = dict()
    
    def addUser(self,user):
        if user.getName() in self.__userMap:
            raise RuntimeError("User already exists")
        self.__userMap[user.getName()]= user 
    
    def getUser(self,userName):
        user = self.__userMap.get(userName,-1)
        if user ==-1:
            raise RuntimeError("User Not Found")
        return user 
    
    def setTeam(self,user,team):
        user.setTeam(team)

    def addEvent(self,user,event):
        user.getEvents().append(event)
