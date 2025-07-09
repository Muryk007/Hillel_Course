while True:
    user_text = input('Enter any text with \'h\' or \'H\' letter: ')
    for char in user_text:
        if char == 'h' or char == 'H':
            print("Thank you!")
            exit()
