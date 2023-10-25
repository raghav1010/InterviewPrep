class Player:
    _playerName = None
    _playerId = None 
    _playerSymbol = None 

    def __init__(self,playerName,playerId):
        self._playerName = playerName
        self._playerId = playerId
    
    def getName(self):
        return self._playerName
    
    def getId(self):
        return self._playerId 
    
    def getSymbol(self):
        return self._playerSymbol
    
    def setSymbol(self,symbol):
        self._playerSymbol = symbol