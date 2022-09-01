from tkinter import Variable
import pygame
import square
import evaluatedPosition

class board:

    position = [] # 2D list of square objects
    for i in range(9):
        position.append([])
        for j in range(9):
            position[i].append(0)
        
    boardStatus = [0, 0, 0, 0, 0, 0, 0, 0, 0] # Each 0 represents the big board, and boardStatus[boardNum] gets the status of a specific board
    # Each board can be 0 = incomplete, WX = x wins, WO = o wins, D = draw

    # self.position[boardnum][boardposition] # retrieves the square at the position
    # board number corresponds to the big board, going left to right and top to bottom 0-8,
    # and board position corresponds to the location of the square in the smaller board

    def userInput(self, boardNum, boardPos, turn, prevMove, screen):
        print("the previous move's qualities are:", prevMove[0], prevMove[1])
        if prevMove[0] == None or (prevMove[1] == boardNum and self.boardStatus[prevMove[1]] == 0) or (self.boardStatus[prevMove[1]] != 0 and (self.boardStatus[boardNum] == 0 and boardNum != prevMove[1])):
            # if the board the user is directed to is incomplete, they can make a move; otherwise, they can move anywhere
            mySquare = self.position[boardNum][boardPos]
            result = mySquare.isChosen(turn, screen)
            self.checkResult(boardNum, turn, screen)
            # self.convertBoard(turn, (boardNum, boardPos))
            # L = self.evalBoard.legalMoves()
            # if L != None:
            #     for thing in L:
            #         print(thing.changedTile)
            return result
        else:
            return False
    
    def checkResult(self, boardNum, turn, screen):
        fullBoard = True
        for pos in range(9):
            if self.position[boardNum][pos].value == 0:
                fullBoard = False
        if fullBoard == True:
            self.boardStatus[boardNum] = 'D'
            print("Draw on board", boardNum)
            return True

        if turn == 'X':
            if (self.position[boardNum][0].value == 'X' and self.position[boardNum][1].value == 'X' and self.position[boardNum][2].value == 'X') or (self.position[boardNum][3].value == 'X' and self.position[boardNum][4].value == 'X' and self.position[boardNum][5].value == 'X') or (self.position[boardNum][6].value == 'X' and self.position[boardNum][7].value == 'X' and self.position[boardNum][8].value == 'X') or (self.position[boardNum][0].value == 'X' and self.position[boardNum][3].value == 'X' and self.position[boardNum][6].value == 'X') or (self.position[boardNum][1].value == 'X' and self.position[boardNum][4].value == 'X' and self.position[boardNum][7].value == 'X') or (self.position[boardNum][2].value == 'X' and self.position[boardNum][5].value == 'X' and self.position[boardNum][8].value == 'X') or (self.position[boardNum][0].value == 'X' and self.position[boardNum][4].value == 'X' and self.position[boardNum][8].value == 'X') or (self.position[boardNum][2].value == 'X' and self.position[boardNum][4].value == 'X' and self.position[boardNum][6].value == 'X'):
                self.boardStatus[boardNum] = 'WX'
                screen.bigXbigO(boardNum, 'WX')
                print("X wins on board", boardNum)
                return True
               
        else:
            if (self.position[boardNum][0].value == 'O' and self.position[boardNum][1].value == 'O' and self.position[boardNum][2].value == 'O') or (self.position[boardNum][3].value == 'O' and self.position[boardNum][4].value == 'O' and self.position[boardNum][5].value == 'O') or (self.position[boardNum][6].value == 'O' and self.position[boardNum][7].value == 'O' and self.position[boardNum][8].value == 'O') or (self.position[boardNum][0].value == 'O' and self.position[boardNum][3].value == 'O' and self.position[boardNum][6].value == 'O') or (self.position[boardNum][1].value == 'O' and self.position[boardNum][4].value == 'O' and self.position[boardNum][7].value == 'O') or (self.position[boardNum][2].value == 'O' and self.position[boardNum][5].value == 'O' and self.position[boardNum][8].value == 'O') or (self.position[boardNum][0].value == 'O' and self.position[boardNum][4].value == 'O' and self.position[boardNum][8].value == 'O') or (self.position[boardNum][2].value == 'O' and self.position[boardNum][4].value == 'O' and self.position[boardNum][6].value == 'O'):
                self.boardStatus[boardNum] = 'WO'
                screen.bigXbigO(boardNum, 'WO')
                print("O wins on board", boardNum)
                return True
        return False
    
    def checkBigBoard(self):
        fullBoard = True
        for pos in range(9):
            if self.boardStatus[pos] == 0:
                fullBoard = False
        if fullBoard == True:
            return 'D'

        
        if ((self.boardStatus[0] == 'WX' and self.boardStatus[1] == 'WX' and self.boardStatus[2] == 'WX')
            or (self.boardStatus[3] == 'WX' and self.boardStatus[4] == 'WX' and self.boardStatus[5] == 'WX')
            or (self.boardStatus[6] == 'WX' and self.boardStatus[7] == 'WX' and self.boardStatus[8] == 'WX')
            or (self.boardStatus[0] == 'WX' and self.boardStatus[3] == 'WX' and self.boardStatus[6] == 'WX')
            or (self.boardStatus[1] == 'WX' and self.boardStatus[4] == 'WX' and self.boardStatus[7] == 'WX')
            or (self.boardStatus[2] == 'WX' and self.boardStatus[5] == 'WX' and self.boardStatus[8] == 'WX')
            or (self.boardStatus[0] == 'WX' and self.boardStatus[4] == 'WX' and self.boardStatus[8] == 'WX')
            or (self.boardStatus[2] == 'WX' and self.boardStatus[4] == 'WX' and self.boardStatus[6] == 'WX')
        ):
            return 'WX'


        if ((self.boardStatus[0] == 'WO' and self.boardStatus[1] == 'WO' and self.boardStatus[2] == 'WO')
            or (self.boardStatus[3] == 'WO' and self.boardStatus[4] == 'WO' and self.boardStatus[5] == 'WO')
            or (self.boardStatus[6] == 'WO' and self.boardStatus[7] == 'WO' and self.boardStatus[8] == 'WO')
            or (self.boardStatus[0] == 'WO' and self.boardStatus[3] == 'WO' and self.boardStatus[6] == 'WO')
            or (self.boardStatus[1] == 'WO' and self.boardStatus[4] == 'WO' and self.boardStatus[7] == 'WO')
            or (self.boardStatus[2] == 'WO' and self.boardStatus[5] == 'WO' and self.boardStatus[8] == 'WO')
            or (self.boardStatus[0] == 'WO' and self.boardStatus[4] == 'WO' and self.boardStatus[8] == 'WO')
            or (self.boardStatus[2] == 'WO' and self.boardStatus[4] == 'WO' and self.boardStatus[6] == 'WO')
        ):
            return 'WO'
        return None

    def convertBoard(self, turn, currentMove): # converts sqr to -1,1,0
        returnList = []
        for i in range(9):
            returnList.append([])
            for j in range (9):
                if self.position[i][j].value == 'O':
                    returnList[i].append(-1)
                elif self.position[i][j].value == 'X':
                    returnList[i].append(1)
                else:
                    returnList[i].append(0)
        self.evalBoard = evaluatedPosition.evaluatedPosition(returnList, None, turn, currentMove, self.boardStatus)
        return returnList