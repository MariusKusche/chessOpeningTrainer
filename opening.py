import pygame
import string
import math
import drag


# maybe

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
        with open("./data/" + name+".txt", "r") as f:
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
            return False
        elif (self.firstIndex + 1) <= len(self.moves):
            self.firstIndex += 1
            self.secondIndex = 0
            return True

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
            return list(range(8,16))+list(range(24,32)), Opening.abcDict[move[0]], self.translate(move[2:])
        else:
            return list(range(8,16))+list(range(24,32)), 10, self.translate(move)

    def translate(self, pos):
        uno = Opening.abcDict[pos[0]]
        duo = 8-int(pos[1])
        return uno, duo
