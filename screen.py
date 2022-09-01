import pygame
import square
import board

class screen:

  scr = pygame.display.set_mode((729, 729))

  def drawGrid(self):
    scr = screen.scr
    scr.fill((255, 255, 255))
    pygame.display.flip()
    pygame.draw.line(scr, "black", (243, 20), (243, 709), 5)
    pygame.draw.line(scr, "black", (486, 20), (486, 709), 5)
    pygame.draw.line(scr, "black", (20, 243), (709, 243), 5)
    pygame.draw.line(scr, "black", (20, 486), (709, 486), 5)

    for i in range(3):
        for j in range(3):
            pygame.draw.line(scr, "black", (243 * i + 30, 243 * j + 90),
                             (243 * (i + 1) - 30, 243 * j + 90), 4)
            pygame.draw.line(scr, "black",
                             (243 * i + 30, 243 * j + 153),
                             (243 * (i + 1) - 30, 243 * j + 153), 4)
            pygame.draw.line(scr, "black", (243 * i + 90, 243 * j + 30),
                             (243 * i + 90, 243 * (j + 1) - 30), 4)
            pygame.draw.line(scr, "black",
                             (243 * i + 153, 243 * j + 30),
                             (243 * i + 153, 243 * (j + 1) - 30), 4)
    screen.scr = scr
    pygame.display.update()


  def fillBoard(self, x, y, boardnum, brd):
    scr = screen.scr
    for i in range(3):
        for j in range(3):
            sqr = square.square(0, boardnum, (j*3)+i, pygame.Rect(x + 63*i, y + 63*j, 58, 58))
            brd.position[boardnum][(j*3)+i] = sqr
            pygame.draw.rect(scr, (255, 255, 255), sqr.rectangle)
    screen.scr = scr
    pygame.display.update()

  def fillScreen(self, brd):
    for i in range(3):
        for j in range(3):
            self.fillBoard(30 + 243 * i, 30 + 243 * j, (j*3)+i, brd)

  def replaceRect(self, sqr, letter):
    scr = screen.scr
    if letter == 'x':
        scr.blit(sqr.x_image, sqr.rectangle)
    if letter == 'o':
        scr.blit(sqr.o_image, sqr.rectangle)
    screen.scr = scr
    pygame.display.update()

  def bigXbigO(self, boardNum, letter):
    scr = screen.scr
    x_image_fs = pygame.image.load("ttt_x.png")
    x_image = pygame.transform.scale(x_image_fs, (220, 220))
    o_image_fs = pygame.image.load("ttt_o.png")
    o_image = pygame.transform.scale(o_image_fs, (220, 220))

    brdrectangle = pygame.Rect(boardNum % 3 * 243 + 10, boardNum//3 * 243 + 17, 120, 120)

    if letter == 'WX':
      scr.blit(x_image, brdrectangle)
    if letter == 'WO':
      scr.blit(o_image, brdrectangle)

    screen.scr = scr
    pygame.display.update()

    


            