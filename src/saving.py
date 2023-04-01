import os

import constants
import game
import settings

def get_path(save):
    return os.path.join(
        constants.DIR_SAVE,
        save)

def save():
    data = '!Items\n'
    for item in settings.GAME.items:
        data += item.name + ':' + str(item.amount) + '\n'

    data += '\n!Tools\n'
    for tool in settings.GAME.tools:
        data += tool.name + ':' + str(tool.level) + '\n'

    data += '\n!Machines\n'
    for machine in settings.GAME.machines:
        data += machine.name + ':' + str(machine.level) + '\n'

    with open(get_path(settings.SAVE_NAME), 'w') as file:
        file.write(data)

def parse_category(category):
    return [entry for entry in category.split('\n'[1:] if entry)]

def parse_data(data):
    for category in data:
        if category[0] == 'Items':
            items = parse_category(category)

def load(filename):
    with open(get_path(filename)) as file:
        data = file.read()

    data = data.split('!')

    items, tools, machines = parse_data(data)

    items = [item for item in data[0].split('\n')[1:] if item]
    print(items)

    tools = [tool for tool in data[1].split('\n')[1:] if tool]
    print(tools)

    machines = [machine for machine in data[2].split('\n')[1:] if machine]
    print(machines)

    settings.GAME = game.Game()
    settings.GAME.items = items
    settings.GAME.tools = tools
    settings.GAME.machines = machines

    settings.SAVE_NAME = os.path.basename(filename)
    print(f'Welcome back, {settings.SAVE_NAME}!')
    print("Tyoe 'help' for a list of commands.")

def new():
    settings.SAVE_NAME = input('Enter a name for your save:\n> ')
    settings.GAME = game.Game()

    print('Welcome to zmyth!')
    print("Tyoe 'help' for a list of commands.")
