import os
from pynput import keyboard



def menuBar():
    print('- Select one of the 5 modules below:')
    print('- Compare simple and compound interest savings acccounts')
    print('- Calculate the time for a CI savings account to reach a target amount')
    print('- Compare two Compound Interest savings accounts')
    print('- Model a CI savings account with regular deposits')
    print('- Model increases in compounding frequency')
    print('- Exit')
    with keyboard.Events() as events:
        event = events.get(16)
        if event.key == keyboard.KeyCode.from_char('down'):
            print("YES")
    
menuBar()
