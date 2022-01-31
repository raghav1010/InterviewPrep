class PlayerData:
    
    def __init__(self):
        self.score = 0 
        self.wicketsTaken = 0
        self.numberOfSix = 0 
        self.numberOfFour = 0
        self.numberOfBallsFaced = 0

    def getScore(self):
        return self.score 
    
    def getWicketsTaken(self):
        return self.wicketsTaken 

    def getNumberOfSix(self):
        return self.numberOfSix
    
    def getNumberOfFour(self):
        return self.numberOfFour
    
    def getNumberOfBallFaced(self):
        return self.getNumberOfBallFaced
    
    def updateScore(self,score):
        self.score = score
    
    # def updateWicketsTaken(self):
    #     return self.wicketsTaken 

    def updateNumberOfSix(self):
        self.numberOfSix+=1
    
    def updateNumberOfFour(self):
        self.numberOfFour+=1
    
    def updateNumberOfBallFaced(self):
        self.getNumberOfBallFaced+=1
    

    def updatePlayerScore(self,score):
        self.updateScore(score)
        self.updateNumberOfBallFaced()
        if score ==4:
            self.updateNumberOfFour()
        elif score == 6:
            self.updateNumberOfSix()
    