from GameBoard import GameBoard
from Player import Player


class PlayGame:

    def main(self):
        p1 = Player("Raghav",1)
        p1.setSymbol("X")

        p2 = Player("Mayank",2)
        p2.setSymbol("0")

        players = list()
        players.append(p1)
        players.append(p2)

        Game = GameBoard(3,players)
        Game.startGame()
        
play = PlayGame()
play.main()