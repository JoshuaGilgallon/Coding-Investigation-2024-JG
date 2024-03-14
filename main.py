import os
import sys
import math

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

def getTimeFactor(interestRateUnit, projectionUnit):
    timeFactors = {
        'year': 1,
        'quarter': 4,
        'month': 12,
        'week': 52,
        'day': 365
    }
    return timeFactors.get(interestRateUnit.lower(), 1) / timeFactors.get(projectionUnit.lower(), 1)

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
    ciCompoundingTimeUnit = checkTimeFormat('Enter the compounding period time unit (year, quarter, month, week, day, custom): ', 
                                           '\n>> Please enter a valid time unit',
                                           'x', 0, 1)
    
    if ciCompoundingTimeUnit.lower() == 'custom':
        ciCompoundingTimeUnit = checkInt('x', 'x', '>> Please enter a valid number', 'Enter the number of compounding periods per interest rate time unit: ', 'x', 0)
    else:
        ciCompoundingMap = {'custom': checkInt('x', 'x', '>> Please enter a valid number', 'Enter the number of compounding periods per interest rate time unit: ', 'x', 0),
                      'day': 1,
                      'year': 1,
                      'quarter': 4,
                      'month': 12,
                      'week': 52}

        ciCompoundingTimeUnit = ciCompoundingMap.get(ciCompoundingTimeUnit.lower(), 0)
    
    print('\nFuture projecting timeframe\n')
    timeIntoFuture = checkInt('x', 'x', '>> Please enter a valid number', 'Enter the amount of time to project into the future: ', 'x', 0)
    projectionUnit = checkTimeFormat('Enter the projection time unit (year, quarter, month, week, day): ', '>> Please enter a valid time unit', 'x', 0, 0)

    # Adjustments based on time units for both simple and compound interest calculations
    siTimeFactor = getTimeFactor(siInterestRateTimeUnit, projectionUnit)
    ciTimeFactor = getTimeFactor(ciInterestRateTimeUnit, projectionUnit)

    siProjectedAmount = siPrincipleAmount * (1 + siInterestRate / 100 * siTimeFactor * timeIntoFuture)
    siInterestEarned = siProjectedAmount - siPrincipleAmount

    ciProjectedAmount = ciPrincipleAmount * (1 + ciInterestRate / 100 / ciCompoundingTimeUnit) ** (ciCompoundingTimeUnit * ciTimeFactor * timeIntoFuture)
    ciInterestEarned = ciProjectedAmount - ciPrincipleAmount
    
    cls()
    
    print(
        'Summary:\n'
        '- Simple Interest\n'
        f'  > Principle Amount: {siPrincipleAmount}\n'
        f'  > Interest Rate: {siInterestRate}% per {siInterestRateTimeUnit}\n'
        '- Compound Interest:\n'
        f'  > Principle Amount: {ciPrincipleAmount}\n'
        f'  > Interest Rate: {ciInterestRate}% per {ciInterestRateTimeUnit}\n'
        f'  > Compounding Frequency: {ciCompoundingTimeUnit}\n'
        f'- Projection Timeframe: {timeIntoFuture} {projectionUnit}s'

    )
    
    print(
        f'\nSI Account projected amount: ${siProjectedAmount:.2f}, Interest earned: ${siInterestEarned:.2f}\n'
        f'CI Account projected amount: ${ciProjectedAmount:.2f}, Interest earned: ${ciInterestEarned:.2f}'
    )

def moduleTwo():
    cls()
    print('Module 2: Time for a Compound Interest account to reach a target amount. \n')
    ciPrincipleAmount = checkInt('x', 'x', '>> Please enter a valid number', 'Enter the principle amount (in $): ', 'x', 0)
    ciInterestRate = checkInt('x', 'x', '>> Please enter a valid number', f'Enter the interest rate (Enter 7% as 7): ', 'x', 0)
    ciInterestRateTimeUnit = checkTimeFormat('Enter the interest rate time unit (year, quarter, month, week, day): ', 
                                           '\n>> Please enter a valid time unit',
                                           'x', 0, 0)
    ciCompoundingTimeUnit = checkTimeFormat('Enter the compounding period time unit (year, quarter, month, week, day, custom): ', 
                                           '\n>> Please enter a valid time unit',
                                           'x', 0, 1)
    
    if ciCompoundingTimeUnit.lower() == 'custom':
        ciCompoundingTimeUnit = checkInt('x', 'x', '>> Please enter a valid number', 'Enter the number of compounding periods per interest rate time unit: ', 'x', 0)
    else:
        ciCompoundingMap = {
                      'day': 1,
                      'year': 1,
                      'quarter': 4,
                      'month': 12,
                      'week': 52}

        ciCompoundingTimeUnit = ciCompoundingMap.get(ciCompoundingTimeUnit.lower(), 0)
    
    targetAmount = checkInt('x', 'x', '>> Please enter a valid amount', 'Enter the target amount: ', 'x', 0)

    time = 0
    timeProjections = []

    # Calculate amount at each time step until target amount is reached
    while True:
        amount = ciPrincipleAmount * (1 + ciInterestRate / 100 / ciCompoundingTimeUnit) ** (ciCompoundingTimeUnit * time)

        timeProjections.append(amount)

        if amount >= targetAmount:
            break

        time += 1

    cls()

    print(f'It will take approximately {time} {ciInterestRateTimeUnit}s to reach the target amount of ${targetAmount}.\n\n')
    print('Individual values over time:')
    print('-'*30)

    cycle = 0
    for i in timeProjections:
        cycle += 1
        print(f'{ciInterestRateTimeUnit} {cycle}: {i}')

    print('\n Summary:')



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
