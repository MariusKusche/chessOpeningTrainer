import pygame

white = (255, 255, 255)
black = (0, 0, 0)
grey = (105, 105, 105)

class Messages:

    rows = 0

    def __init__(self, name):
        self.opening = name
        self.firstIndex = 0
        self.secondIndex = 0

    def xCenter(self, screeni):
        x = screeni.get_size()[0] - 8 * 110 - 25
        x /= 2
        x += 8 * 110 + 25
        return x

    def setUpMessage(self, screeni):

        x = self.xCenter(screeni)

        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(self.opening, True, black, white)
        textRect = text.get_rect()
        textRect.center = (x, textRect.h/2)

        font2 = pygame.font.Font('freesansbold.ttf', 28)
        text2 = font2.render('Please play the main line.', True, black, white)
        textRect2 = text2.get_rect()
        textRect2.center = (x, textRect.h/2+textRect2.h)

        screeni.blit(text, textRect)
        screeni.blit(text2, textRect2)

        pygame.display.flip()

        return textRect.h+textRect2.h

    def tryAgain(self, screeni, height):

        x = self.xCenter(screeni)

        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("Please try again.", True, black, white)

        textRect = text.get_rect()
        whiteRect = pygame.Rect(0, 0, 261, 34)

        textRect.center = (x, height + textRect.h / 2)
        whiteRect.center = (x, height + whiteRect.h / 2 -1)

        pygame.draw.rect(screeni, white, whiteRect)
        screeni.blit(text, textRect)
        pygame.display.flip()

    def correct(self, screeni, height):

        x = self.xCenter(screeni)

        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("That is correct.", True, black, white)
        textRect = text.get_rect()
        whiteRect = pygame.Rect(0, 0, 261, 34)

        textRect.center = (x, height + textRect.h / 2)
        whiteRect.center = (x, height + whiteRect.h / 2)

        pygame.draw.rect(screeni, white, whiteRect)
        screeni.blit(text, textRect)
        pygame.display.flip()

        return height + whiteRect.h

    def displayMove(self, screeni, opning, height, width):

        moveIndex = opning.secondIndex
        lineIndex = opning.firstIndex
        move = opning.moves[lineIndex][moveIndex]

        if self.firstIndex != opning.firstIndex:
            self.firstIndex += 1
            self.secondIndex = 0
            Messages.rows += 40
            width = 0

        if self.secondIndex == moveIndex and moveIndex%2 == 0:
            font = pygame.font.Font('freesansbold.ttf', 25)
            text = font.render(str(int(moveIndex/2)+1) + "." + move, True, black, grey)
            textRect = text.get_rect()
            if 8 * 110 + 25 + 5 + width + textRect.w < screeni.get_size()[0]:
                textRect.topleft = (8 * 110 + 25 + 5 + width, height + 5 + Messages.rows)
            else:
                Messages.rows += textRect.h + 5
                width = 0
                textRect.topleft = (8 * 110 + 25 + 5, height + 5 + Messages.rows)
            screeni.blit(text, textRect)
            pygame.display.flip()
            self.secondIndex += 1

            return textRect.w + width

        elif self.secondIndex == moveIndex and moveIndex%2 != 0:
            font = pygame.font.Font('freesansbold.ttf', 25)
            text = font.render(move, True, black, grey)
            textRect = text.get_rect()
            if 8 * 110 + 25 + 5 + width + textRect.w < screeni.get_size()[0]:
                textRect.topleft = (8 * 110 + 25 + 5 + width, height + 5 + Messages.rows)
            else:
                Messages.rows += textRect.h + 5
                width = 0
                textRect.topleft = (8 * 110 + 25 + 5, height + 5 + Messages.rows)
            screeni.blit(text, textRect)
            pygame.display.flip()
            self.secondIndex += 1

            return textRect.w + width + 5


