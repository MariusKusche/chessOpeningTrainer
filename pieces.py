import pygame


class Piece(pygame.sprite.Sprite):

    def __init__(self, kind):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("gfx/"+kind+".png")
        self.rect = self.image.get_rect()
        self.moveX = 0
        self.moveY = 0
        self.type = 1
        self.w = self.rect.w
        self.h = self.rect.h


    def update(self):
        self.rect.center = (self.rect.center[0] + self.moveX, self.rect.center[1] + self.moveY)
        self.moveX = 0
        self.moveY = 0

    def updateMove(self, coords):
        self.moveX = coords[0]
        self.moveY = coords[1]

    def updateImage(self, x, y):
        return 0

    # https://stackoverflow.com/questions/22361249/pygame-draw-currently-draws-all-sprites-in-a-group-
    # how-can-i-just-draw-a-spe
    def draw(self, screen):
        screen.blit(self.image, self.rect)
