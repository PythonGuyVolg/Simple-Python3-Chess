#!/usr/bin/env python
import os
import sys

if sys.version_info[0] == 2:
    print("This game runs on python 3 only")


from board import *

# Load a save if it exists

if os.path.exists("state.fen"):
    with open("state.fen") as save:
        game = board.Board(save.read())
else:
    game = Board()

# Choose display method
howtodisplay = input('HOW TO RUN CHESS? IN GUI OR CONSOLE? input your choise(gui, console) \n')
if howtodisplay.lower() in ['gui', '1']:
    
    from gui_tkinter import *
    display(game)
    exit(0)
elif howtodisplay.lower() in ['console', '2']:
    from gui_console import *

  
display(game)
