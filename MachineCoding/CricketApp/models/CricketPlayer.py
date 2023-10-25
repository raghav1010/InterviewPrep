import Player,PlayerData

class CricketPlayer(Player):
    
    def __init__(self,playerName,playerAge):
        super(playerName,playerAge)
        self.playerData = PlayerData()
        self.isOnStrike = False 
        self.isOut = False 
    
    def getPlayerData(self):
        return self.playerData
    
    def updatePlayerScore(self,score):
        self.getPlayerData.updatePlayerScore(score)


