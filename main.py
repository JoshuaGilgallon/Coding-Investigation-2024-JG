import os



def menuBar():
    print('1 - Select one of the 5 modules below:')
    print('2 - Compare simple and compound interest savings acccounts')
    print('3 - Calculate the time for a CI savings account to reach a target amount')
    print('4 - Compare two Compound Interest savings accounts')
    print('5 - Model a CI savings account with regular deposits')
    print('6 - Model increases in compounding frequency')
    print('7 - Exit')
    selection = input('Select an option: ')
    try: int(selection)
    except: 
        print('Please select a valid option.')
        menuBar()
    else:
        return selection
    
module = menuBar()
