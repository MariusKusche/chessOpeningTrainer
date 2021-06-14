import pygame

white = (255, 255, 255)
black = (0, 0, 0)
grey = (105, 105, 105)


class Messages:
    rows = 0
    fontsize = 20

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
        text = font.render(self.opening, True, black, grey)
        textRect = text.get_rect()
        textRect.center = (x, textRect.h / 2)

        font2 = pygame.font.Font('freesansbold.ttf', 28)
        text2 = font2.render('Please play the main line.', True, black, grey)
        textRect2 = text2.get_rect()
        textRect2.center = (x, textRect.h / 2 + textRect2.h)

        screeni.blit(text, textRect)
        screeni.blit(text2, textRect2)

        pygame.display.flip()

        return textRect.h + textRect2.h

    def tryAgain(self, screeni, height):
        x = self.xCenter(screeni)

        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("Please try again.", True, black, white)

        textRect = text.get_rect()
        whiteRect = pygame.Rect(0, 0, 261, 34)

        textRect.center = (x, height + textRect.h / 2)
        whiteRect.center = (x, height + whiteRect.h / 2 - 1)

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

    def displayMove(self, screeni, opning, height, width):
        moveIndex = opning.secondIndex
        lineIndex = opning.firstIndex
        move = opning.moves[lineIndex][moveIndex]

        # is this the last move?
        if moveIndex == len(opning.moves[lineIndex]) - 1:
            k = 1
        else:
            k = 0

        font = pygame.font.Font('freesansbold.ttf', Messages.fontsize)
        if (moveIndex % 2 == 0 and lineIndex == 0):
            text = font.render(str(int(moveIndex / 2) + 1) + "." + move + k * " Done!", True, black, grey)
        elif (moveIndex % 2 != 0 and lineIndex > 0):
            text = font.render(str(int(moveIndex / 2) + 1) + "." + move + k * " Done!", True, black, grey)
        else:
            text = font.render(move + " " + k * " Done!", True, black, grey)
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

    # blit the next line/variation which should be played on the screen
    def nextLine(self, height, opning, screeni):
        width = 0
        font = pygame.font.Font('freesansbold.ttf', Messages.fontsize)
        for i in range(opning.secondIndex - 1):
            move = opning.moves[opning.firstIndex][i]
            if (i % 2 == 0 and i == 0) or (i % 2 == 0 and width == 0):
                text = font.render(str(int(i / 2) + 1) + "." + move, True, black, grey)
            elif i % 2 == 0 and i != 0:
                text = font.render(str(int(i / 2) + 1) + "." + move, True, black, grey)
            else:
                text = font.render(move + " ", True, black, grey)
            textRect = text.get_rect()
            # want this to be done prettier
            # Purpose: we start in a new line
            if i == 0 and opning.firstIndex > 1:
                height += textRect.h + 5
            if 8 * 110 + 25 + 5 + width + textRect.w < screeni.get_size()[0]:
                textRect.topleft = (8 * 110 + 25 + 5 + width, height + 5 + Messages.rows)
                width += textRect.w
            else:
                Messages.rows += textRect.h + 5
                width = textRect.w
                textRect.topleft = (8 * 110 + 25 + 5, height + 5 + Messages.rows)
            screeni.blit(text, textRect)
            pygame.display.flip()

        return width, height

    def plsContinue(self, height, screeni):
        x = self.xCenter(screeni)

        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("Please continue the line.", True, black, white)
        textRect = text.get_rect()
        whiteRect = pygame.Rect(0, 0, 387, 34)

        # hardcoded starting new line
        height += 30
        textRect.center = (x, height + Messages.rows + textRect.h / 2)
        whiteRect.center = (x, height + Messages.rows + whiteRect.h / 2 - 1)

        pygame.draw.rect(screeni, white, whiteRect)
        screeni.blit(text, textRect)
        pygame.display.flip()

        return height + textRect.h
