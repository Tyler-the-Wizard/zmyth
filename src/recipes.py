import os

import constants
import game
import settings

def get_path(recipe):
    return os.path.join(
        constants.DIR_RECIPE,
        recipe)

class Recipe:
    def __init__(self, tool, inputs, outputs):
        self.tool = tool
        self.inputs = inputs
        self.outputs = outputs

    def __str__(self):
        return (self.tool.recipe_str() + '\n  '
            + ', '.join([str(item) for item in self.inputs]) + '\n    => '
            + ', '.join([str(item) for item in self.outputs])) + '\n'

def load_file(filename):
    with open(get_path(filename)) as file:
        data = [line.strip() for line in file.readlines() if len(line)]

    for line in data:
        if line.startswith('#'):
            continue

        tool_str, inputs_str, outputs_str = line.split('&')

        settings.RECIPES.append(Recipe(
            game.Tool.from_string(tool_str),
            [game.Item.from_string(s) for s in inputs_str.split(',')],
            [game.Item.from_string(s) for s in outputs_str.split(',')]))

def load():
    for filename in os.listdir(constants.DIR_RECIPE):
        load_file(filename)
