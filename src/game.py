import color

class Game:
    def __init__(self):
        self.items = [Item('Gravel', -1)]
        self.tools = [Tool('hands', 0)]
        self.machines = []

class Item:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __str__(self):
        amount_str = color.PURPLE('Inf') if self.amount < 0 else str(self.amount)
        return f'{self.name} x{amount_str}'

    def __add__(self, lhs):
        if self.amount >= 0:
            self.amount += lhs

    def __sub__(self, lhs):
        if self.amount >= 0:
            if lhs > self.amount:
                raise ArithmeticError
            self.amount -= lhs

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