import settings

def do():
    cmd = input('> ')

    match cmd.lower():
        case 'h':
            # Print help
            print('Help urself lol')

        case 'quit' | 'exit':
            settings.IS_RUNNING = False

        case _:
            print(f"Unknown command '{cmd}'")
