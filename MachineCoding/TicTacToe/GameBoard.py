from collections import deque


class GameBoard:
    board = None 
    boardSize = None 
    nextTurn = None 

    def __init__(self,size,players):
        self.boardSize = size
        self.board = [[None for i in range(size)] for j in range(size)]
        self.nextTurn = deque()
        self.nextTurn.append(players[0])
        self.nextTurn.append(players[1])

        self.__inBoard()
    
    def __inBoard(self):
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                self.board[i][j] = "-"
    
    def __printBoard(self):
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                print(self.board[i][j],end = " ")
                if (j<self.boardSize-1):
                    print("|",end="")
            print()
    
    def startGame(self):
        count = 0 
        while(True):
            count+=1 
            if (count == (self.boardSize*self.boardSize)+1):
                print("Match Draw")
                return 
            p = self.nextTurn.popleft()
            row,col = self.__getUserInput(p)
            self.board[row][col] = p.getSymbol()
            self.__printBoard()
            print("Board after the move")
            if (count>= 2*self.boardSize and self.__checkEndGame(p,row,col)):
                break 
            self.nextTurn.append(p)
    
    def __getUserInput(self,player):
        self.__printBoard()
        print("Board before the move")
        print(player.getName() + " please enter the indices(i,j) considering 1 indexing ")
        r,c = map(int,input().split())
        while (self.__validateInput(r,c)==False):
            print("Wrong Position")
            r,c = map(int,input().split())
        return r-1,c-1

    def __validateInput(self,r,c):
        if (r-1<0 or r-1>=self.boardSize or c-1<0 or c-1>=self.boardSize):
            return False 
        if (self.board[r-1][c-1]!="-"):
            return False
        return True 
    
    def __checkEndGame(self,p,r,c):
        winString = p.getSymbol()*self.boardSize
        rowString = ""
        columnString = ""
        diagonalString = ""
        reverseDiaString = ""

        for i in range(self.boardSize):
            rowString=rowString+self.board[r][i]
            columnString=columnString+self.board[i][c]

            if (r==c):
                diagonalString=diagonalString+self.board[i][i]
            if (r+c == self.boardSize -1):
                reverseDiaString= reverseDiaString+self.board[self.boardSize-1-i][i]

        if (winString==rowString or winString==columnString or winString==diagonalString or winString==reverseDiaString):
            print(p.getName()+" has won")
            return True 
        return False 

