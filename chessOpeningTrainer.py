# import the pygame module, so you can use it
import pygame
import settingUp
import drag
from opening import Opening
from messages import Messages


# define a main function
def main():
     
    pieceList, screen, sLength = settingUp.setBoard()
    opn = Opening()
    opn.readMoves("random_opening")

    # define a variable to control the main loop
    running = True
    index = 0
    #dragging = False

    mes = Messages("Random Opening")
    hei = mes.setUpMessage(screen)
    # hardcoded but the first messages have fixed height
    # which might be a problem for openings with long names
    height2 = hei + 34
    wid = 0

    xOld = 0
    yOld = 0

    ### On a general note, this needs to be more compact, I thinkt we should introduce another file/class which
    ### incorporates the actions
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

            # leave the game by pressing esc
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    index, xOld, yOld = drag.detectFigure(pieceList, event, screen)
                    if index == 100:
                        relocate = opn.isLastMove()
                        if relocate:
                            settingUp.relocate(pieceList, screen)
                            dotIndex = opn.arrangePieces(pieceList, screen)
                            opn.secondIndex = dotIndex + 1
                            mes.firstIndex += 1
                            mes.secondIndex = dotIndex + 1
                            if opn.firstIndex == 1:
                                height2 = mes.plsContinue(height2, screen)
                            wid, height2 = mes.nextLine(height2, opn, screen)
                    #dragging = True


            # doesnt work at the moment as intended, fix later
#            elif event.type == pygame.MOUSEMOTION:
#                if dragging:
#                    drag.dragging(pieceList, event, screen, index)


            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if index < 100:
                        correct = opn.checkMove(index, event, screen)

                        if correct:
                            drag.blitSquare(xOld, yOld, screen)
                            mes.correct(screen, hei)
                            drag.moveFigure(pieceList, event, screen, index)
                            wid = mes.displayMove(screen, opn, height2, wid)
                            opn.updateIndex()
                        else:
                            mes.tryAgain(screen, hei)
                        #dragging = False


     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
