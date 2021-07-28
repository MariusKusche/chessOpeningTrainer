import pygame
import pieces

class Board:

    # def __init__(self, width, height):
    #    self.height = height
    #    self.width = width

    #sLength = 0
    #coordLength = 0

    def make_board(self, screen):
        woodSquare = pygame.image.load("gfx/white_square.png")
        greySquare = pygame.image.load("gfx/dark_square.png")

        coords = []
        letters = "ABCDEFGH"

        for i in range(len(letters) * 2):
            if i < len(letters):
                coords.append(pygame.image.load("gfx/" + str(i + 1) + ".png"))
            else:
                coords.append(pygame.image.load("gfx/" + letters[i - len(letters)] + ".png"))

        squareLength = woodSquare.get_rect().size[0]
        coordsLength = coords[0].get_rect().size[0]

        windRect = pygame.Surface((squareLength * 8 + coordsLength, squareLength * 8 + coordsLength))
        windRect.fill((255, 255, 255))

        screen.blit(windRect, (0, 0))
        pygame.display.flip()

        for k in range(len(coords)):
            if k < len(coords) / 2:
                screen.blit(coords[k], (8 * squareLength, (7 - k) * squareLength))
                pygame.display.flip()
            else:
                screen.blit(coords[k], ((k - 8) * squareLength, 8 * squareLength))
                pygame.display.flip()

        for k in range(8):
            for kk in range(8):
                if kk % 2 == 0:
                    if k % 2 == 0:
                        screen.blit(woodSquare, (k * squareLength, kk * squareLength))
                        pygame.display.flip()
                    else:
                        screen.blit(greySquare, (k * squareLength, kk * squareLength))
                        pygame.display.flip()
                else:
                    if k % 2 == 0:
                        screen.blit(greySquare, (k * squareLength, kk * squareLength))
                        pygame.display.flip()
                    else:
                        screen.blit(woodSquare, (k * squareLength, kk * squareLength))
                        pygame.display.flip()

        return squareLength

    def putAllPieces(self, squareLength, screen):
        pieceList = self.loadPieces(squareLength)

        for k in range(6):  # len(pieceList)):
            if k < 3:
                for kk in range(2):
                    screen.blit(pieceList[0][k], (
                    pieceList[1][k] + (1 - kk) * k * squareLength + kk * (7 - k) * squareLength, 7 * squareLength))
                    screen.blit(pieceList[0][int(len(pieceList[0]) / 2) + k],
                                (pieceList[1][k] + (1 - kk) * k * squareLength + kk * (7 - k) * squareLength, 0))
                    pygame.display.flip()
            elif k < 5:
                screen.blit(pieceList[0][k], (
                    pieceList[1][k] + k * squareLength, 7 * squareLength))
                screen.blit(pieceList[0][int(len(pieceList[0]) / 2) + k],
                            (pieceList[1][k] + k * squareLength, 0))
                pygame.display.flip()
            else:
                for kk in range(8):
                    screen.blit(pieceList[0][k], (pieceList[1][k] + kk * squareLength, 6 * squareLength))
                    screen.blit(pieceList[0][int(len(pieceList[0]) / 2) + k],
                                (pieceList[1][k] + kk * squareLength, squareLength))
                    pygame.display.flip()

    def pieceLocation(self, pieList, squareLength):
        for k in range(5):
            if k < 4:
                pieList.sprites()[2 * k].rect.center = (squareLength / 2 + k * squareLength, 7.5 * squareLength)
                pieList.sprites()[2 * k + 1].rect.center = (7.5 * squareLength - k * squareLength, 7.5 * squareLength)
                pieList.sprites()[2 * k + 16].rect.center = (squareLength / 2 + k * squareLength, 0.5 * squareLength)
                pieList.sprites()[2 * k + 16 + 1].rect.center = (7.5 * squareLength - k * squareLength, 0.5 * squareLength)
            else:
                for kk in range(8):
                    pieList.sprites()[2 * k + kk].rect.center = (squareLength / 2 + kk * squareLength, 6.5 * squareLength+10)
                    pieList.sprites()[2 * k + 16 + kk].rect.center = (squareLength / 2 + kk * squareLength, 1.5 * squareLength+10)

    def blitBoard(self, screen, squareLength):
        for x in range(8):
            for y in range(8):
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

    def putPiecesFromPieces(self, screen, squareLength):
        pieceList = []

        pieceList.append(pieces.Piece("wR"))
        pieceList.append(pieces.Piece("wR"))
        pieceList.append(pieces.Piece("wN"))
        pieceList.append(pieces.Piece("wN"))
        pieceList.append(pieces.Piece("wB"))
        pieceList.append(pieces.Piece("wB"))
        pieceList.append(pieces.Piece("wQ"))
        pieceList.append(pieces.Piece("wK"))

        for k in range(8):
            pieceList.append(pieces.Piece("wP"))

        pieceList.append(pieces.Piece("bR"))
        pieceList.append(pieces.Piece("bR"))
        pieceList.append(pieces.Piece("bN"))
        pieceList.append(pieces.Piece("bN"))
        pieceList.append(pieces.Piece("bB"))
        pieceList.append(pieces.Piece("bB"))
        pieceList.append(pieces.Piece("bQ"))
        pieceList.append(pieces.Piece("bK"))

        for k in range(8):
            pieceList.append(pieces.Piece("bP"))

        all_sprites = pygame.sprite.Group()
        for fig in pieceList:
            all_sprites.add(fig)

        self.pieceLocation(all_sprites, squareLength)

        all_sprites.draw(screen)
        pygame.display.flip()

        return all_sprites#pieceList

    def loadPieces(self, squareSize):
        # maybe rename to w1-w6 and do the same for black pieces to be able to loop
        wPawn = pygame.image.load("gfx/white_pawn.png")
        wRook = pygame.image.load("gfx/white_rook.png")
        wKnight = pygame.image.load("gfx/white_knight.png")
        wBishop = pygame.image.load("gfx/white_bishop.png")
        wQueen = pygame.image.load("gfx/white_queen.png")
        wKing = pygame.image.load("gfx/white_king.png")

        bPawn = pygame.image.load("gfx/black_pawn.png")
        bRook = pygame.image.load("gfx/black_rook.png")
        bKnight = pygame.image.load("gfx/black_knight.png")
        bBishop = pygame.image.load("gfx/black_bishop.png")
        bQueen = pygame.image.load("gfx/black_queen.png")
        bKing = pygame.image.load("gfx/black_king.png")

        pieces = [wRook, wKnight, wBishop, wQueen, wKing, wPawn, bRook, bKnight, bBishop, bQueen, bKing, bPawn]

        pieceWidth = []
        for k in range(len(pieces)):
            pieceWidth.append(squareSize / 2. - pieces[k].get_rect().size[0] / 2.)

        return [pieces, pieceWidth]
