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
            
def checkTimeFormat(question: str, errorMsg: str, priorMsg: str, clearPrior: int, customOption: int):
    # set clearPrior to 0 if clearing output is not necessary, or 1 if it is.
    # set customOption to 1 if it is required, otherwise 0.
    validTimes = ['year', 'quarter', 'month', 'week', 'day']
    if customOption == 1:
        validTimes.append('custom')
    timeFormat = input(question).lower()
    if timeFormat in validTimes:
        return timeFormat
    else:
        if clearPrior == 1:
            cls()
        print(f'{errorMsg}\n')
        return checkTimeFormat(question, errorMsg, priorMsg, clearPrior, customOption)

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
    cls()
    print('Module 1: Compare Simple and Compound Interest Accounts \n' \
        '\nSimple interest account:\n')
    siPrincipleAmount = checkInt('x', 'x', '>> Please enter a valid number', 'Enter the principle amount (in $): ', 'x', 1)
    siInterestRate = checkInt('x', 'x', '>> Please enter a valid number', f'Enter the interest rate (Enter 7% as 7): ', 'x', 0)
    siInterestRateTimeUnit = checkTimeFormat('Enter the interest rate time unit (year, quarter, month, week, day): ', 
                                           '\n>> Please enter a valid time unit',
                                           'x', 0, 0)
    
    print('\nCompound interest account: \n')
    ciPrincipleAmount = checkInt('x', 'x', '>> Please enter a valid number', 'Enter the principle amount (in $): ', 'x', 0)
    ciInterestRate = checkInt('x', 'x', '>> Please enter a valid number', f'Enter the interest rate (Enter 7% as 7): ', 'x', 0)
    ciInterestRateTimeUnit = checkTimeFormat('Enter the interest rate time unit (year, quarter, month, week, day): ', 
                                           '\n>> Please enter a valid time unit',
                                           'x', 0, 0)
    ciCompoundingTimeUnit = checkTimeFormat('Enter the compunding period time unit (year, quarter, month, week, day, custom): ', 
                                           '\n>> Please enter a valid time unit',
                                           'x', 0, 1)
    if ciCompoundingTimeUnit.lower() == 'custom':
        ciCompoundingTimeUnit = checkInt('x', 'x', '>> Please enter a valid number', 'Enter the number of compounding periods per interest rate time unit: ', 'x', 0)
    
    print('\nFuture projecting timeframe\n')
    timeIntoFuture = checkInt('x', 'x', '>> Please enter a valid number', 'Enter the amount of time to project into the future: ', 'x', 0)
    projectionUnit = checkTimeFormat('Enter the projection time unit (year, quarter, month, week, day): ', '>> Please enter a valid time unit', 'x', 0, 0)

    
    cls()
    print(

f'Summary:\n \
- Simple Interest:\n \
  > Principle Amount: {siPrincipleAmount}\n \
  > Interest Rate: {siInterestRate}% per {siInterestRateTimeUnit}\n \
- Compound Interest:\n \
  > Principle Amount: {ciPrincipleAmount}\n \
  > Interest Rate: {ciInterestRate}% per {ciInterestRateTimeUnit}\n \
  > Compounding Frequency: {ciCompoundingTimeUnit}'
            
         )




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
