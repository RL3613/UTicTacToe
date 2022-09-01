import pygame
import square
import board


class evaluatedPosition:

   eval = 0

   def __init__(self, currentPos, changedTile, turn, prevMove, boardStatus): # changedTile ( boardNum, boardPos, letter )
        self.nPos = currentPos # numerated position
        self.boardStatus = boardStatus
        if changedTile != None:
            (boardNum, boardPos, letter) = changedTile
            self.nPos[boardNum][boardPos] = letter
        self.turn = turn
        self.prevMove = prevMove
        self.changedTile = changedTile

   def legalMoves(self):
        legalList = []
        prevTile = self.prevMove[1]
        if self.prevMove == (None, None):
            return None
        if self.boardStatus[prevTile] == 0:
            print("prevTile is", str(prevTile))
            for i in range(9):
                if self.nPos[prevTile][i] == 0:
                    print("hello")
                    legalList.append(evaluatedPosition(self.nPos, (prevTile, i, self.turn), self.flipTurn(), (prevTile, i), self.checkPotentialWin((prevTile, i, self.turn)), ))
            return legalList


   def flipTurn(self):
        if self.turn == 'X':
            return 'O'
        else:
            return 'X'

   def checkPotentialWin(self, changed):
        newPos = []
        newStatus = []
        for i in range(9):
            newPos.append([])
            for j in range(9):
                newPos[i].append(self.nPos[i][j])
        (changedBoard, changedTile, letter) = changed
        newPos[changedBoard][changedTile] = letter

        for i in range(9):
            newStatus = self.boardStatus

        if ((newPos[changedBoard][0] == 'X' and newPos[changedBoard][1] == 'X' and newPos[changedBoard][2] == 'X')
            or (newPos[changedBoard][3] == 'X' and newPos[changedBoard][4] == 'X' and newPos[changedBoard][5] == 'X')
            or (newPos[changedBoard][6] == 'X' and newPos[changedBoard][7] == 'X' and newPos[changedBoard][8] == 'X')
            or (newPos[changedBoard][0] == 'X' and newPos[changedBoard][3] == 'X' and newPos[changedBoard][6] == 'X')
            or (newPos[changedBoard][1] == 'X' and newPos[changedBoard][4] == 'X' and newPos[changedBoard][7] == 'X')
            or (newPos[changedBoard][2] == 'X' and newPos[changedBoard][5] == 'X' and newPos[changedBoard][8] == 'X')
            or (newPos[changedBoard][0] == 'X' and newPos[changedBoard][4] == 'X' and newPos[changedBoard][8] == 'X')
            or (newPos[changedBoard][2] == 'X' and newPos[changedBoard][4] == 'X' and newPos[changedBoard][6] == 'X')
        ):
            newStatus[changedBoard] = 'WX'
            

        if ((newPos[changedBoard][0] == 'O' and newPos[changedBoard][1] == 'O' and newPos[changedBoard][2] == 'O')
            or (newPos[changedBoard][3] == 'O' and newPos[changedBoard][4] == 'O' and newPos[changedBoard][5] == 'O')
            or (newPos[changedBoard][6] == 'O' and newPos[changedBoard][7] == 'O' and newPos[changedBoard][8] == 'O')
            or (newPos[changedBoard][0] == 'O' and newPos[changedBoard][3] == 'O' and newPos[changedBoard][6] == 'O')
            or (newPos[changedBoard][1] == 'O' and newPos[changedBoard][4] == 'O' and newPos[changedBoard][7] == 'O')
            or (newPos[changedBoard][2] == 'O' and newPos[changedBoard][5] == 'O' and newPos[changedBoard][8] == 'O')
            or (newPos[changedBoard][0] == 'O' and newPos[changedBoard][4] == 'O' and newPos[changedBoard][8] == 'O')
            or (newPos[changedBoard][2] == 'O' and newPos[changedBoard][4] == 'O' and newPos[changedBoard][6] == 'O')
        ):
            newStatus[changedBoard] = 'WO'

        return newStatus
