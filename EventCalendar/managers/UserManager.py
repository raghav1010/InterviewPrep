from models.Team import Team 
from models.Event import Event
from models.TimeSlot import TimeSlot
from models.User import User
from dao.UserDao import UserDao

class UserManager(object):

    _userDao = None 
    def __init__(self):
        self._userDao = UserDao()
    
    def createUser(self,name,timeSlot):
        newUser = User(name,timeSlot)
        self._userDao.addUser(newUser)
        return newUser 
    
    def getUser(self,name):
        return self._userDao.getUser(name)
    
    def setTeam(self,user,team):
        self._userDao.setTeam(user,team)
    
    def addEvent(self,user,event):
        self._userDao.addEvent(user,event)
    