import pygame
import string
import math
import drag


class Opening:
    # there has to be a better way to get such a dictionary?!
    abcDict = dict.fromkeys(string.ascii_lowercase, range(26))
    counterAbc = 0
    for key in abcDict:
        abcDict[key] = counterAbc
        counterAbc += 1
    counterAbc = 0
    counterVariations = 0

    piecesDict = {"R": (0, 1, 16, 17), "N": (2, 3, 18, 19), "B": (4, 5, 20, 21), "Q": (6, 22), "K": (7, 23)}

    def __init__(self, moves=None):
        if moves is None:
            self.moves = {}
        self.firstIndex = 0
        self.secondIndex = 0

    def readMoves(self, name):
        index = 0
        with open("./data/" + name + ".txt", "r") as f:
            for line in f:
                words = line.split()
                self.moves[index] = words
                index += 1

    def tellMove(self):
        return self.moves[self.firstIndex][self.secondIndex]

    # at the moment white can move in some cases two times in a row without causing an error
    def checkMove(self, index, event, screen):
        indPiec, line, square = self.whichMove(self.moves[self.firstIndex][self.secondIndex])
        indPiec = list(indPiec)
        if len(square) == 2:
            if index in indPiec and Opening.detectSquare(self, event.pos[0], event.pos[1]) == square:
                return True
            else:
                return False
        else:
            if index in indPiec and Opening.detectSquare(self, event.pos[0], event.pos[1]) == (square[0], square[1]):
                return True
            elif index in indPiec and Opening.detectSquare(self, event.pos[0], event.pos[1]) == (square[0], square[2]):
                return True
            else:
                return False

    def updateIndex(self):
        if (self.secondIndex + 1) < len(self.moves[self.firstIndex]):
            self.secondIndex += 1
        elif (self.firstIndex + 1) < len(self.moves):
            self.firstIndex += 1
            self.secondIndex = 0

    def isLastMove(self):
        if self.secondIndex == 0 and self.firstIndex > 0:
            return True
        else:
            return False

    def detectSquare(self, mouseX, mouseY):
        # hard coded square length
        return (math.floor(mouseX / 110), math.floor(mouseY / 110))

    # return is as follows: the kind of piece as a tuple of indices for pieceList, the row where the piece was
    # if not needed than this equals 10 and a tuple to which square the piece will move
    # also note this can be done better!! not all cases are covered
    def whichMove(self, move):
        # special case with tuple of len 3 means someone castled
        if move == "0-0":
            return Opening.piecesDict["K"], 10, (6, 7, 0)
        elif move == "0-0-0":
            return Opening.piecesDict["K"], 10, (2, 7, 0)
        elif move[0].isupper():
            if move[0] == "N":
                if move[1] == "x":
                    return Opening.piecesDict[move[0]], 10, self.translate(move[2:])
                elif len(move) > 3:
                    if move[2] == "x":
                        return Opening.piecesDict[move[0]], Opening.abcDict[move[1]], self.translate(move[3:])
                    else:
                        return Opening.piecesDict[move[0]], Opening.abcDict[move[1]], self.translate(move[2:])
                else:
                    return Opening.piecesDict[move[0]], 10, self.translate(move[1:])
            if move[0] == "R":
                if move[1] == "x":
                    return Opening.piecesDict[move[0]], 10, self.translate(move[2:])
                elif len(move) > 3:
                    if move[2] == "x":
                        return Opening.piecesDict[move[0]], Opening.abcDict[move[1]], self.translate(move[3:])
                    else:
                        return Opening.piecesDict[move[0]], Opening.abcDict[move[1]], self.translate(move[2:])
                else:
                    return Opening.piecesDict[move[0]], 10, self.translate(move[1:])
            else:
                if move[1] == "x":
                    return Opening.piecesDict[move[0]], 10, self.translate(move[2:])
                else:
                    return Opening.piecesDict[move[0]], 10, self.translate(move[1:])
        elif move[1] == "x":
            return list(range(8, 16)) + list(range(24, 32)), Opening.abcDict[move[0]], self.translate(move[2:])
        else:
            return list(range(8, 16)) + list(range(24, 32)), 10, self.translate(move)


    def translate(self, pos):
        uno = Opening.abcDict[pos[0]]
        duo = 8 - int(pos[1])
        return uno, duo

    # this is work in progress
    # method which puts the pieces on the board according to the next line
    def arrangePieces(self, pieceList, screeni):
        line = self.moves[self.firstIndex]
        dotIndex = 0
        for i in range(len(line)):
            if line[i] == ".":
                dotIndex = i
                break

        for i in range(dotIndex):
            pieceKind, row, square = self.whichMove(line[i])
            self.updatePiecePosition(i, pieceKind, row, square, pieceList, screeni)

        return dotIndex


    def newCenter(self, square):
        squareLength = 110
        return squareLength / 2 + square[0] * squareLength, (square[1] + 0.5) * squareLength

    def updatePiecePosition(self, moveIndex, kindOfPiece, row, square, piecList, screeni):
        pieceIndex = self.identifyPiece(moveIndex, kindOfPiece, row, square, piecList)

        center = self.detectSquare(piecList.sprites()[pieceIndex].rect.center[0], piecList.sprites()[pieceIndex].rect.center[1])
        drag.blitSquare(center[0], center[1], screeni)

        moveX = self.newCenter(square)[0] - piecList.sprites()[pieceIndex].rect.center[0]
        moveY = self.newCenter(square)[1] - piecList.sprites()[pieceIndex].rect.center[1]
        piecList.sprites()[pieceIndex].updateMove((moveX, moveY))

        self.takePiece(piecList, square)
        drag.blitSquare(square[0], square[1], screeni)
        piecList.update()
        for piece in piecList:
            if piece.type == 1:
                piece.draw(screeni)
        pygame.display.flip()


    def identifyPiece(self, moveIndex, kindOfPiece, row, square, pieceList):
        if moveIndex % 2 == 0:
            # white to play
            if len(kindOfPiece) == 2:
                return kindOfPiece[0]
            elif len(kindOfPiece) == 4:
                if row != 10:
                    for i in range(2):
                        if self.identifyMove(self.rNorB(kindOfPiece), pieceList.sprites()[kindOfPiece[i]].rect.center, square):
                            return kindOfPiece[i]
                else:
                    if self.identifyMove(self.rNorB(kindOfPiece), pieceList.sprites()[kindOfPiece[0]].rect.center, square):
                        return kindOfPiece[0]
                    else:
                        return kindOfPiece[1]
            else:
                if row == 10:
                    for i in range(8, 16):
                        if math.floor(pieceList.sprites()[i].rect.center[0] / 110) == square[0]:
                            return i
                else:
                    for i in range(8, 16):
                        if math.floor(pieceList.sprites()[i].rect.center[0] / 110) == row:
                            # Warning: this is not bulletproof, think of doubled pawns etc, but for no this should be ok
                            return i
        else:
            if len(kindOfPiece) == 2:
                return kindOfPiece[1]
            elif len(kindOfPiece) == 4:
                if row != 10:
                    for i in range(2, 4):
                        if self.identifyMove(self.rNorB(kindOfPiece), pieceList.sprites()[kindOfPiece[i]].rect.center, square):
                            return kindOfPiece[i]
                else:
                    if self.identifyMove(self.rNorB(kindOfPiece), pieceList.sprites()[kindOfPiece[2]].rect.center, square):
                        return kindOfPiece[2]
                    else:
                        return kindOfPiece[3]
            else:
                if row == 10:
                    for i in range(24, 32):
                        if math.floor(pieceList.sprites()[i].rect.center[0] / 110) == square[0]:
                            return i
                else:
                    for i in range(24, 32):
                        if math.floor(pieceList.sprites()[i].rect.center[0] / 110) == row:
                            # Warning: this is not bulletproof, think of doubled pawns etc, but for no this should be ok
                            return i


    def rNorB(self, kindOfPiece):
        if kindOfPiece[0] == 0:
            return "R"
        elif kindOfPiece[0] == 2:
            return "N"
        else:
            return "B"


    def identifyMove(self, pieceLetter, pieceCenter, square):
        pieceSquare = (math.floor(pieceCenter[0] / 110), math.floor(pieceCenter[1] / 110))
        if pieceLetter == "R" and ((pieceSquare[0] - square[0]) == 0 or (pieceSquare[1] - square[1]) == 0):
            # Warning! this is not bulletproof but should suffice for an opening trainer
            return True
        elif pieceLetter == "B" and (abs(pieceSquare[0] - square[0]) == abs(pieceSquare[1] - square[1])):
            return True
        elif pieceLetter == "N":
            if abs(pieceSquare[0] - square[0]) == 1 and abs(pieceSquare[1] - square[1]) == 2:
                return True
            elif abs(pieceSquare[0] - square[0]) == 2 and abs(pieceSquare[1] - square[1]) == 1:
                return True
        else:
            return False

    def takePiece(self, piecList, square):
        for piece in piecList.sprites():
            if self.detectSquare(piece.rect.center[0], piece.rect.center[1]) == square:
                # instead of removing the sprite we set its type to 0 which means it won't be drawn
                piece.type = 0

                # not very pretty, we want this sprite to be a placeholder such that the order in the group isn't changed
                # therefore we set it to the topleft corner of the screen and set its size to 1
                piece.rect.topleft = (0, 0)
                piece.rect.width = 1
                piece.rect.height = 1
                break
