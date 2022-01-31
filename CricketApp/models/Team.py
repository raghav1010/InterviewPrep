import CricketPlayer
from collections import deque

class Team:

    def __init__(self,teamName):
        self.teamName = teamName
        self.players = list()
        self.availablePlayers = deque()
        self.totalTeamScore = 0
        self.currentBatsman = None
        self.strikeBatsman = None
        self.totalWickets = 0
    
    def getTeamScore(self):
        self.totalTeamScore
    
    def getTeamName(self):
        return self.teamName

    def getPlayers(self):
        return self.players
    
    def addPlayersToTeam(self,player):
        if (player in self.players):
            print("Player already in the Team")
        else:
            self.players.append(player)
            self.availablePlayers.append(player)
    
    def initializePlayers(self):
        if (len(self.availablePlayers)>=2):
            self.currentBatsman = self.availablePlayers.popleft()
            self.strikeBatsman = self.availablePlayers.popleft()
    

    def isNextBatsmanAvailable(self):
        if (len(self.availablePlayers)!=0):
            return True 
        else:
            return False 

    def wicketFallen(self):
        player = self.availablePlayers.popleft()
        self.currentBatsman = player 
    
    def swapStrike(self):
        temp = self.currentBatsman
        self.currentBatsman = self.strikeBatsman
        self.strikeBatsman = temp 
    
    def updateStrike(self,score):
        if (score!=0 and score%2 != 0):
            self.swapStrike()
    
    def updateScore(self,score):
        self.currentBatsman.updatePlayerScore(score)
        self.updateStrike(score)
        self.totalTeamScore+=score 
    
    def getTotalWickets(self):
        return self.totalWickets
    
    def updateWickets(self):
        self.totalWickets+=1 
        if (self.isNextBatsmanAvailable()):
            self.wicketFallen()
            self.updateScore(0)
            return True 
        else:
            print("No Batsman to play")
            return False 
            