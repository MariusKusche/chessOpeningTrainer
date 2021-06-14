# chessOpeningTrainer
A simple opening trainer for the game chess, where the user provides the opening

This trainer needs pygame (see https://www.pygame.org/news) to function.

Short description:

In this chess opening trainer one plays the main line of an opening, provided by the user, and then play the variation starting by the first deviation from the 
mainline or variations in this variation and so on.

How to use:

The pieces have to be dragged, two times clicking doesn't work yet. If you finished the current line correctly you will recieve a "Done!" message on the right side
behind the moves. To start with the next variation you then have to click somewhere in the window.

The opening txt-file you provide (or the one that is here given) must be named in the main file "chessOpeningTrainer.py" and the format is as indicated by the
example file. The main line is the first line and the variations come afterwards in new rows.  At the move where the respective variation deviate from the main line you 
need to put a "." inbetween the moves. This marks the move (the one after the ".") from which the student has to continue.

Some Remarks:

Also there are some little inconveniences, which are partially declared in the files, e.g. one player can move to times in a row if the conditions are met like 
e4 e5 both with white. 
Changes in future updates will be: 
- solve the issue if there are more lines than space on the screen
- visualise dragging of the pieces
- more...


Note on the graphics:

The numbers and the logo are designed by myself, the squares are pictures of mine and the pieces are taken from a free stockphoto.
