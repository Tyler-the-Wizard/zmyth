import os

import constants
import prompt
import settings

'''
Startup the program:
    - If saves exist, present menu of which save to select.
        - Include new save as an option
    - Otherwise, create a new save.

Setup:
    - Initialize game state.
        - Items
        - Tools
        - Recipes
        - Machines (?)

Main loop:
    - Ask for a command, then parse it. Some commands may have their own special parsers.
'''

try:
    os.mkdir(constants.DIR_SAVE)
except FileExistsError as _:
    pass

saves = os.listdir(constants.DIR_SAVE)

if len(saves) == 0:
    # Create a new save
    pass
else:
    # Select a save
    print('Enter a selection:')
    print(' 1 - New save')
    for i, entry in enumerate(saves):
        print(f' {i + 2} - {entry}')

    sel = prompt.get_int((1, 1+len(saves)))