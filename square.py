import pygame

class square:

    x_image_fs = pygame.image.load("ttt_x.png")
    x_image = pygame.transform.scale(x_image_fs, (55, 55))
    o_image_fs = pygame.image.load("ttt_o.png")
    o_image = pygame.transform.scale(o_image_fs, (55, 55))

    def __init__(self, value, brdNumber, brdPosition, rectangle):
        self.value = value
        self.brdNumber = brdNumber
        self.brdPosition = brdPosition
        self.rectangle = rectangle

    # value: X = O, 0 = None, X = X
    
    def getRectangle(self):
        return self.rectangle

    def isChosen(self, turn, screen):
        if self.value == 0:
            if turn == "X":
                screen.replaceRect(self,"x")
                self.value = "X"
            else:
                screen.replaceRect(self,"o")
                self.value = "O"
            return True
        else:
            return False


            
