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
        if clearPrior == 1:
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
                if clearPrior == 1:
                    cls()
                print(f'{errorMsg}\n')
                return checkInt(lowVal, highVal, errorMsg, question, priorMsg, clearPrior)

def menuBar():
    module = checkInt(0, 7, '>> Please select a valid option.', 'Select an option: ',
            '1 - Compare simple and compound interest savings acccounts\n'
            '2 - Calculate the time for a CI savings account to re`ach a target amount\n'
            '3 - Compare two Compound Interest savings accounts\n'
            '4 - Model a CI savings account with regular deposits\n'
            '5 - Model increases in compounding frequency\n'
            '6 - Exit', 1
            )
    
    module_functions[module]()

def moduleOne():
    priorMsgAsFormat = 'Module 1: Compare Simple and Compound Interest Accounts \n' \
                        '\nSimple interest account:\n'
    cls()
    principleAmount = checkInt('x', 'x', '>> Please enter a valid number', 'Enter the principle amount: ', priorMsgAsFormat, 1)
    priorMsgAsFormat = f'{priorMsgAsFormat}\n{principleAmount}'

    

def moduleTwo():
    pass

def moduleThree():
    pass

def moduleFour():
    pass

def moduleFive():
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
    6: exitProgram
}
    
menuBar()
