from MachineCoding.EventCalendar.dao.TeamDao import TeamDao
from MachineCoding.EventCalendar.models.Team import Team


class TeamManager:

    _teamDao = None 
    _userDao = None 

    def __init__(self,userManager):
        self._userDao = userManager 
        self._teamDao = TeamDao()

    def createTeam(self,teamName,userlist):
        self._validateUsers(userlist)
        team = Team()
        