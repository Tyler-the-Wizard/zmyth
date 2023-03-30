def get_int(int_range=None):
    is_valid = False

    while not is_valid:
        user_input = input('> ')

        try:
            int_input = int(user_input)
        except ValueError:
            if int_range is None:
                print('Please enter a number.')
            else:
                print(f'Please enter a number from {int_range[0]} to {int_range[1]}.')
        else:
            if int_range is not None and not (
                    int_range[0] <= int_input <= int_range[1]):
                print(f'Please enter a number from {int_range[0]} to {int_range[1]}.')
            else:
                is_valid = True

    return int_input