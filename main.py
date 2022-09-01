import pygame
import board
import screen

myscreen = screen.screen()
brd = board.board()
myscreen.drawGrid()
myscreen.fillScreen(brd)

turn = 'X'
running = True
prevMove = (None, None)
while running:
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        if turn != 'E':
          for i in range(9):
            for j in range(9):
              theRect = brd.position[i][j].rectangle
              if theRect.collidepoint(pygame.mouse.get_pos()):
                if brd.userInput(i, j, turn, prevMove, myscreen) == True:
                  print(i, j)
                  if turn == 'X':
                    turn = 'O'
                  else:
                    turn = 'X'
                  prevMove = (i, j)
                  if (brd.checkBigBoard() == 'WX') or (brd.checkBigBoard() == 'WO') or (brd.checkBigBoard() == 'D'):
                    print("Someone on or the game was drawn")
                    turn = 'E'
                else:
                  print(brd.userInput(i, j, turn, prevMove, myscreen))
                  print("Invalid move. Try again.")

      if event.type == pygame.QUIT:
          running = False
      if running == False:
          pygame.quit()