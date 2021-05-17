import pygame
from board import Board


def setBoard():

    # initialize the pygame module
        pygame.init()
        # load and set the logo
        logo = pygame.image.load("gfx/GU_logo.png")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("Schach Schach Schach")

        # Create screen
        screen_width = 1300#self.width
        screen_height = 925#self.height

        # create a surface on screen that has the size of 1300 x 900
        screen = pygame.display.set_mode((screen_width, screen_height))

        # background
        screen.fill((105, 105, 105))
        pygame.display.flip()

        # initialize board and figures
        board1 = Board()
        sqLength = board1.make_board(screen)
        pList = board1.putPiecesFromPieces(screen, sqLength)

        return pList, screen, sqLength

def relocate(pList, screen):

    boardRelocate = Board()
    # we first have to resize the pieces otherwise traded pieces will not be blited correctly
    # that is an artifact of drag.pieceCollision, maybe find another way how to handle collisions
    for piece in pList:
        if piece.type == 0:
            piece.rect.h = piece.h
            piece.rect.w = piece.w

    boardRelocate.pieceLocation(pList, 110)
    boardRelocate.blitBoard(screen, 110)

    for piece in pList:
        piece.type = 1
        piece.draw(screen)

    pygame.display.flip()

