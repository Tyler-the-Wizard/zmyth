import os

if os.name == 'nt':
    os.system('color')

def colorize(text, color_code):
    return f'\33[{color_code}m{text}\33[0m'

def GRAY(text):
    return colorize(text, 30)
def RED(text):
    return colorize(text, 31)
def GREEN(text):
    return colorize(text, 32)
def YELLOW(text):
    return colorize(text, 33)
def BLUE(text):
    return colorize(text, 34)
def PURPLE(text):
    return colorize(text, 35)
def CYAN(text):
    return colorize(text, 36)
