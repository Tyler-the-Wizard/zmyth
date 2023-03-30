import os

import constants
import settings

def get_path(save):
    return os.path.join(
        constants.DIR_SAVE,
        save)

def save():
    data = '!Item\n'
    for item in settings.GAME.items:
        data += item.name + ':' + str(item.amount) + '\n'

    data += '\n!tools\n'
    for tool in settings.GAME.tools:
        data += tool.name + ':' + str(tool.level) + '\n'

    data += '\n!Machine\n'
    for machine in settings.GAME.machines:
        data += machine.name + ':' + str(machine.level) + '\n'

    with open(get_path(settings.SAVE_NAME), 'w') as file:
        file.write(data)

def load(filename):
    with open(get_path(filename)) as file:
        data = file.read()

    data = data.split('!')

    items = data[0].split('\n')
    print(items)

    tools = data[1].split('\n')
    print(tools)

    machines = data[2].split('\n')
    print(machines)

    settings.GAME.items = items
    settings.GAME.tools = tools
    settings.GAME.machines = machines

    settings.SAVE_NAME = os.path.basename(filename)
    print(f'Welcome back, {settings.SAVE_NAME}!')
    print("Tyoe 'help' for a list of commands.")

def new():
    settings.SAVE_NAME = input('Enter a name for your save:\n> ')
    print('Welcome to zmyth!')
    print("Tyoe 'help' for a list of commands.")
