import os

import constants
import settings

def get_path(save):
    return os.path.join(
        constants.DIR_SAVE,
        save)

def save():
    data = 'test'

    with open(get_path(settings.SAVE_NAME), 'w') as file:
        file.write(data)

def load(filename):
    with open(get_path(filename)) as file:
        data = file.read()

    settings.SAVE_NAME = os.path.basename(filename)
    print(f'Welcome back, {settings.SAVE_NAME}!')
    print("Tyoe 'help' for a list of commands.")

def new():
    settings.SAVE_NAME = input('Enter a name for your save:\n> ')
    print('Welcome to zmyth!')
    print("Tyoe 'help' for a list of commands.")
