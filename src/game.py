import color

class Game:
    def __init__(self):
        self.items = []
        self.tools = [Tool('hands', 0)]
        self.machines = []

class Item:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __str__(self):
        return f'{self.name} x{self.amount}'

class Tool:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __str__(self):
        return (self.name + ' ' + color.YELLOW('(') +
             str(self.level) + color.YELLOW(')'))

class Machine:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __str__(self):
        return (self.name + ' ' + color.GREEN('[') +
            str(self.level) + color.GREEN(']'))