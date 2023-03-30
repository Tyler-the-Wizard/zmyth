import os
import sys

import command
import constants
import prompt
import saving
import settings

settings.init()

try:
    os.mkdir(constants.DIR_SAVE)
except FileExistsError:
    pass

saves = os.listdir(constants.DIR_SAVE)

if len(saves) == 0:
    # Create a new save
    saving.new()
else:
    # Select a save
    print('Enter a selection:')
    print(' 1 - Start a new save')
    for i, entry in enumerate(saves):
        print(f' {i + 2} - {entry}')

    sel = prompt.get_int((1, 1+len(saves)))

    if sel == 1:
        saving.new()
    else:
        saving.load(saves[sel - 2])

# Begin the main loop
try:
    while settings.IS_RUNNING:
        command.do()
except KeyboardInterrupt:
    print('\nPerforming emergency save.')
else:
    print('Saving...')
finally:
    saving.save()
    print('Done.\nSee you soon...')

    sys.exit(0)
