import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()

def checkInt(lowVal: float, highVal: float, errorMsg: str, question: str, priorMsg: str):
    print(priorMsg)
    answer = input(question)
    try:
        answer = int(answer)
    except ValueError:
        cls()
        print(f'{errorMsg}\n')
        return checkInt(lowVal, highVal, errorMsg, question, priorMsg)
    else:
        if lowVal < answer < highVal:
            return answer
        else:
            cls()
            print(f'{errorMsg}\n')
            return checkInt(lowVal, highVal, errorMsg, question, priorMsg)

def menuBar():
    # print('1 - Select one of the 5 modules below:')
    # print('2 - Compare simple and compound interest savings acccounts')
    # print('3 - Calculate the time for a CI savings account to reach a target amount')
    # print('4 - Compare two Compound Interest savings accounts')
    # print('5 - Model a CI savings account with regular deposits')
    # print('6 - Model increases in compounding frequency')
    # print('7 - Exit')
    # selection = input('Select an option: ')
    # try: selection = int(selection)
    # except: 
    #     cls()
    #     print('>> Please select a valid option.\n')
    #     menuBar()
    # else:
    #     if selection > 0 and selection < 8:
    #         return selection
    #     else:
    #         cls()
    #         print('>> Please select a valid option.\n')
    #         menuBar()
    checkInt(0, 8, '>> Please select a valid option.', 'Select an option: ',
            '1 - Select one of the 5 modules below:\n'
            '2 - Compare simple and compound interest savings acccounts\n'
            '3 - Calculate the time for a CI savings account to reach a target amount\n'
            '4 - Compare two Compound Interest savings accounts\n'
            '5 - Model a CI savings account with regular deposits\n'
            '6 - Model increases in compounding frequency\n'
            '7 - Exit'
            )

def moduleOne():
    cls()
    print('Module 1: Compare Simple and Compound Interest Accounts \n')
    print('Simple interest account:')
    principleAmount = input('Enter the principle amount: ')


    
module = menuBar()


