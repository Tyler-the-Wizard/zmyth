import settings

def do():
    cmd = input('> ')

    match cmd.lower():
        case 'h' | 'help':
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

        case 'i' | 'inv':
            print('Inventory:')
            # TODO

        case 'q':
            print("Type 'quit' to quit.")

        case 'e':
            print("Type 'exit' to exit.")

        case 'quit' | 'exit':
            settings.IS_RUNNING = False

        case _:
            print(f"Unknown command '{cmd}'")
