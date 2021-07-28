import pygame
import math


# see https://stackoverflow.com/questions/41332861/click-and-drag-a-rectangle-with-pygame

def detectFigure(piecList, event, screen):
    for k in range(len(piecList.sprites())):
        if piecList.sprites()[k].rect.collidepoint(event.pos):
            mx, my = detectSquare(event.pos[0], event.pos[1])
            return k, mx, my

    return 100, 100, 100

# bugged
def dragging(piecList, event, screen, pieceIndex):
    mx, my = event.pos
    square = detectSquare(mx, my)

    moveX = newCenter(square)[0] - piecList.sprites()[pieceIndex].rect.center[0]
    moveY = newCenter(square)[1] - piecList.sprites()[pieceIndex].rect.center[1]
    piecList.sprites()[pieceIndex].updateMove((moveX, moveY))

    piecList.update()
    for piece in piecList:
        if piece.type == 1:
            piece.draw(screen)
    pygame.display.flip()


def moveFigure(piecList, event, screen, pieceIndex):
    # what was this used for?
    # if not pieceIndex:
    # return

    mx, my = event.pos
    square = detectSquare(mx, my)

    # white castles
    if pieceIndex == 7 and square == (6, 7):
        moveX = newCenter(square)[0] - piecList.sprites()[pieceIndex].rect.center[0]
        blitSquare(7, 7, screen)
        moveXR = newCenter((5, 7))[0] - piecList.sprites()[1].rect.center[0]
        piecList.sprites()[pieceIndex].updateMove((moveX, 0))
        piecList.sprites()[1].updateMove((moveXR, 0))
        piecList.update()
    elif pieceIndex == 7 and square == (2, 7):
        moveX = newCenter(square)[0] - piecList.sprites()[pieceIndex].rect.center[0]
        blitSquare(0, 7, screen)
        moveXR = newCenter((3, 7))[0] - piecList.sprites()[0].rect.center[0]
        piecList.sprites()[pieceIndex].updateMove((moveX, 0))
        piecList.sprites()[0].updateMove((moveXR, 0))
        piecList.update()
    # black castles
    elif pieceIndex == 23 and square == (6, 0):
        moveX = newCenter(square)[0] - piecList.sprites()[pieceIndex].rect.center[0]
        blitSquare(7, 0, screen)
        moveXR = newCenter((5, 0))[0] - piecList.sprites()[17].rect.center[0]
        piecList.sprites()[pieceIndex].updateMove((moveX, 0))
        piecList.sprites()[17].updateMove((moveXR, 0))
        piecList.update()
    elif pieceIndex == 23 and square == (2, 0):
        moveX = newCenter(square)[0] - piecList.sprites()[pieceIndex].rect.center[0]
        blitSquare(0, 0, screen)
        moveXR = newCenter((3, 0))[0] - piecList.sprites()[16].rect.center[0]
        piecList.sprites()[pieceIndex].updateMove((moveX, 0))
        piecList.sprites()[16].updateMove((moveXR, 0))
        piecList.update()
    else:
        if 7 < pieceIndex < 16 or 23 < pieceIndex < 32:
            moveX = newCenter(square)[0] - piecList.sprites()[pieceIndex].rect.center[0]
            moveY = newCenter(square)[1] - piecList.sprites()[pieceIndex].rect.center[1] + 10
        else:
            moveX = newCenter(square)[0] - piecList.sprites()[pieceIndex].rect.center[0]
            moveY = newCenter(square)[1] - piecList.sprites()[pieceIndex].rect.center[1]

        piecList.sprites()[pieceIndex].updateMove((moveX, moveY))

        collided = pieceCollision(piecList, event)
        piecList.update()
        if collided:
            blitSquare(square[0], square[1], screen)

    for piece in piecList:
        if piece.type == 1:
            piece.draw(screen)
    pygame.display.flip()


def pieceCollision(piecList, event):
    mx, my = event.pos
    index = detectFigureIndex(piecList, event)

    if index:
        # instead of removing the sprite we set its type to 0 which means it won't be drawn
        piecList.sprites()[index].type = 0

        # not very pretty, we want this sprite to be a placeholder such that the order in the group isn't changed
        # therefore we set it to the topleft corner of the screen and set its size to 1
        piecList.sprites()[index].rect.topleft = (0, 0)
        piecList.sprites()[index].rect.width = 1
        piecList.sprites()[index].rect.height = 1

        return 1

    else:
        return 0

# this will be changed, because if you take a figure and don't point into its rect there will be two pieces on the
# same file
def detectFigureIndex(piecList, event):
    for k in range(len(piecList.sprites())):
        if piecList.sprites()[k].rect.collidepoint(event.pos):
            return k

def blitSquare(x, y, screen):
    squareLength = 110
    if x % 2 == 0 and y % 2 == 0:
        woodSquare = pygame.image.load("gfx/white_square.png")
        screen.blit(woodSquare, (x * squareLength, y * squareLength))
        pygame.display.flip()
    elif x % 2 == 0 and y % 2 != 0:
        greySquare = pygame.image.load("gfx/dark_square.png")
        screen.blit(greySquare, (x * squareLength, y * squareLength))
        pygame.display.flip()
    elif x % 2 != 0 and y % 2 == 0:
        greySquare = pygame.image.load("gfx/dark_square.png")
        screen.blit(greySquare, (x * squareLength, y * squareLength))
        pygame.display.flip()
    else:
        woodSquare = pygame.image.load("gfx/white_square.png")
        screen.blit(woodSquare, (x * squareLength, y * squareLength))
        pygame.display.flip()


def newCenter(square):
    squareLength = 110
    return squareLength / 2 + square[0] * squareLength, (square[1] + 0.5) * squareLength


def moveSprite(piece, square):
    squareLength = 110
    piece_ = piece
    piece.rect.center = (squareLength / 2 + square[0] * squareLength, (square[1] + 0.5) * squareLength)
    return piece_


def detectSquare(mouseX, mouseY):
    return (math.floor(mouseX / 110), math.floor(mouseY / 110))
