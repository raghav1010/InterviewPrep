class Player:
    def __init__(self,playerName,playerAge):
        self._playerName = playerName
        self._playerAge = playerAge
    
    def get_playerAge(self):
        return self._playerAge
    
    def set_playerAge(self,age):
        self._playerAge = age 
    
    def get_playerName(self):
        return self._playerName
    
    def set_playerName(self,name):
        self._playerName = name 
