import settings

def do():
    cmd = input('> ')

    if 'help'.startswith(cmd.lower()):
        help_msg = '''
Commands:
 help       show this list
 inventory  look at your inventory
 tools      look at your tools
 machines   look at your machines
 recipes    search recipes by input or output
 use        use a tool to craft something
 auto       set up a machine for automatic crafting
 exit       exit the program

You can also just type the first letter of a command.
'''
        print(help_msg)

    elif 'inventory'.startswith(cmd.lower()):
        print('Inventory:')
        for i in settings.GAME.items:
            print(str(i))

    elif 'tools'.startswith(cmd.lower()):
        print('Tools:')
        for t in settings.GAME.tools:
            print(str(t))

    elif 'machines'.startswith(cmd.lower()):
        print('Machines:')
        for m in settings.GAME.machines:
            print(str(m))

    elif ('quit'.startswith(cmd.lower())
            or 'exit'.startswith(cmd.lower())):
        settings.IS_RUNNING = False

    else:
        print(f"Unknown command '{cmd}'")
