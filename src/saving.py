import os
import zlib

import constants
import game
import settings

def get_path(save):
    return os.path.join(
        constants.DIR_SAVE,
        save)

def save():
    data = ''

    data += '!Items\n'
    for item in settings.GAME.items:
        data += item.name + ':' + str(item.amount) + '\n'

    data += '\n!Tools\n'
    for tool in settings.GAME.tools:
        data += tool.name + ':' + str(tool.level) + '\n'

    data += '\n!Machines\n'
    for machine in settings.GAME.machines:
        data += machine.name + ':' + str(machine.level) + '\n'

    with open(get_path(settings.SAVE_NAME), 'wb') as file:
        file.write(zlib.compress(data.encode()))

def parse_category(category):
    return [entry for entry in category[1:] if entry]

def parse_data(data):
    for category in [c.split('\n') for c in data if c]:
        if category[0] == 'Items':
            items_str = parse_category(category)
        elif category[0] == 'Tools':
            tools_str = parse_category(category)
        elif category[0] == 'Machines':
            machines_str = parse_category(category)

    items = []
    tools = []
    machines = []

    try:
        for s in items_str:
            items.append(game.Item.from_string(s))
        for s in tools_str:
            tools.append(game.Tool.from_string(s))
        for s in machines_str:
            machines.append(game.Machine.from_string(s))

    except UnboundLocalError:
        print(color.RED('Error:'), 'unable to load save')
        raise

    return items, tools, machines

def load(filename):
    with open(get_path(filename), 'rb') as file:
        data = zlib.decompress(file.read()).decode()

    data = data.split('!')

    items, tools, machines = parse_data(data)

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
