import os
import sys

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()

def checkInt(lowVal, highVal, errorMsg: str, question: str, priorMsg: str, clearPrior: int):
    # set lowVal and highVal, or priorMsg to 'x' if they arent needed
    # set clearPrior to 0 if clearing output is not necessary, or 1 if it is.
    if priorMsg != 'x':
        print(priorMsg)
    answer = input(question)
    try:
        answer = int(answer)
    except:
        cls()
        print(f'{errorMsg}\n')
        return checkInt(lowVal, highVal, errorMsg, question, priorMsg, clearPrior)
    else:
        if lowVal == 'x':
            return answer
        else:
            if lowVal < answer < highVal:
                return answer
            else:
                cls()
                print(f'{errorMsg}\n')
                return checkInt(lowVal, highVal, errorMsg, question, priorMsg, clearPrior)

def menuBar():
    module = checkInt(0, 8, '>> Please select a valid option.', 'Select an option: ',
            '1 - Select one of the 5 modules below:\n'
            '2 - Compare simple and compound interest savings acccounts\n'
            '3 - Calculate the time for a CI savings account to re`ach a target amount\n'
            '4 - Compare two Compound Interest savings accounts\n'
            '5 - Model a CI savings account with regular deposits\n'
            '6 - Model increases in compounding frequency\n'
            '7 - Exit', 1
            )
    
    module_functions[module]()

def moduleOne():
    cls()
    print('Module 1: Compare Simple and Compound Interest Accounts \n')
    print('Simple interest account:')
    principleAmount = input('Enter the principle amount: ')
    checkInt('x', 'x', '>> Please enter a valid number', 'Enter the principle amount: ', 'x')

def moduleTwo():
    pass

def moduleThree():
    pass

def moduleFour():
    pass

def moduleFive():
    pass

def moduleSix():
    pass

def exitProgram():
    print('Thanks for playing!')
    sys.exit()
    
module_functions = {
    1: moduleOne,
    2: moduleTwo,
    3: moduleThree,
    4: moduleFour,
    5: moduleFive,
    6: moduleSix,
    7: exitProgram
}
    
menuBar()

