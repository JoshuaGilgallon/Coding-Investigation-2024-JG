import os
import sys
import math

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()

def checkInt(lowVal, highVal, errorMsg: str, question: str, priorMsg: str, clearPrior: bool, isFloat: bool):
    # set lowVal and highVal, or priorMsg to 'x' if they arent needed
    if priorMsg != 'x':
        print(priorMsg)
    answer = input(question)
    try:
        if isFloat:
            answer = float(answer)
        else:
            answer = int(answer)
    except:
        if clearPrior:
            cls()
        print(f'{errorMsg}\n')
        return checkInt(lowVal, highVal, errorMsg, question, priorMsg, clearPrior, isFloat)
    else:
        if lowVal == 'x':
            return answer
        else:
            if lowVal < answer < highVal:
                return answer
            else:
                if clearPrior:
                    cls()
                print(f'{errorMsg}\n')
                return checkInt(lowVal, highVal, errorMsg, question, priorMsg, clearPrior, isFloat)
            
def checkTimeFormat(question: str, errorMsg: str, priorMsg: str, clearPrior: bool, customOption: bool):
    validTimes = ['year', 'quarter', 'month', 'week', 'day']
    if customOption:
        validTimes.append('custom')
    timeFormat = input(question).lower()
    if timeFormat in validTimes:
        return timeFormat
    else:
        if clearPrior:
            cls()
        print(f'{errorMsg}\n')
        return checkTimeFormat(question, errorMsg, priorMsg, clearPrior, customOption)

def menuBar():
    cls()
    module = checkInt(0, 7, '>> Please select a valid option.', 'Select an option: ',
            '1 - Compare simple and compound interest savings acccounts\n'
            '2 - Calculate the time for a CI savings account to re`ach a target amount\n'
            '3 - Compare two Compound Interest savings accounts\n'
            '4 - Model a CI savings account with regular deposits\n'
            '5 - Model increases in compounding frequency\n'
            '6 - Exit', True, False
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

def createCompoundAccount():
    ciPrincipleAmount = checkInt('x', 'x', '>> Please enter a valid number', 'Enter the principle amount (in $): ', 'x', False, True)
    ciInterestRate = checkInt('x', 'x', '>> Please enter a valid number', f'Enter the interest rate (Enter 7% as 7): ', 'x', False, True)
    ciInterestRateTimeUnit = checkTimeFormat('Enter the interest rate time unit (year, quarter, month, week, day): ', 
                                           '\n>> Please enter a valid time unit',
                                           'x', False, False)
    ciCompoundingTimeUnit = checkTimeFormat('Enter the compounding period time unit (year, quarter, month, week, day, custom): ', 
                                           '\n>> Please enter a valid time unit',
                                           'x', False, True)
    
    if ciCompoundingTimeUnit.lower() == 'custom':
        ciCompoundingTimeUnit = checkInt('x', 'x', '>> Please enter a valid number', 'Enter the number of compounding periods per interest rate time unit: ', 'x', False, False)
    else:
        ciCompoundingMap = {
                      'day': 1,
                      'year': 1,
                      'quarter': 4,
                      'month': 12,
                      'week': 52}

        ciCompoundingTimeUnit = ciCompoundingMap.get(ciCompoundingTimeUnit.lower(), 0)

    return ciPrincipleAmount, ciInterestRate, ciInterestRateTimeUnit, ciCompoundingTimeUnit

def moduleOne():
    cls()
    print('Module 1: Compare Simple and Compound Interest Accounts \n' \
        '\nSimple interest account:\n')
    siPrincipleAmount = checkInt('x', 'x', '>> Please enter a valid number', 'Enter the principle amount (in $): ', 'x', True, True)
    siInterestRate = checkInt('x', 'x', '>> Please enter a valid number', f'Enter the interest rate (Enter 7% as 7): ', 'x', False, True)
    siInterestRateTimeUnit = checkTimeFormat('Enter the interest rate time unit (year, quarter, month, week, day): ', 
                                           '\n>> Please enter a valid time unit',
                                           'x', False, False)
    
    print('\nCompound interest account: \n')

    ciPrincipleAmount, ciInterestRate, ciInterestRateTimeUnit, ciCompoundingTimeUnit = createCompoundAccount()
    
    print('\nFuture projecting timeframe\n')
    timeIntoFuture = checkInt('x', 'x', '>> Please enter a valid number', 'Enter the amount of time to project into the future: ', 'x', False, False)
    projectionUnit = checkTimeFormat('Enter the projection time unit (year, quarter, month, week, day): ', '>> Please enter a valid time unit', 'x', False, False)

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

    input('Press enter to return to menu')
    menuBar()

def moduleTwo():
    cls()
    print('Module 2: Time for a Compound Interest account to reach a target amount. \n')

    ciPrincipleAmount, ciInterestRate, ciInterestRateTimeUnit, ciCompoundingTimeUnit = createCompoundAccount()
    
    targetAmount = checkInt('x', 'x', '>> Please enter a valid amount', 'Enter the target amount: ', 'x', False, True)

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

    print(
        'Summary:\n'
        '- Compound Interest:\n'
        f'  > Principle Amount: {ciPrincipleAmount}\n'
        f'  > Interest Rate: {ciInterestRate}% per {ciInterestRateTimeUnit}\n'
        f'  > Compounding Frequency: {ciCompoundingTimeUnit}\n'
        f'  > Target Amount: {targetAmount}\n'
    )

    print('Individual values over time:')
    print('-'*30)

    cycle = 0
    for i in timeProjections:
        cycle += 1
        print(f'{ciInterestRateTimeUnit.capitalize()} {cycle}: {i:.2f}')

    input('Press enter to return to menu')
    menuBar()

def moduleThree():
    cls()
    print('Module 3: Compare Two Compound Interest Accounts \n' \
        '\nCompound interest account 1:\n')

    ciPrincipleAmount1, ciInterestRate1, ciInterestRateTimeUnit1, ciCompoundingTimeUnit1 = createCompoundAccount()

    print('\nCompound interest account 2:\n')

    ciPrincipleAmount2, ciInterestRate2, ciInterestRateTimeUnit2, ciCompoundingTimeUnit2 = createCompoundAccount()

    

    print('\nCompare Options: \n')
    compareType = checkInt(0, 3, '>> Please enter a valid option', 'Would you like to compare the accounts:\n  - Up to a certain $ value (1)\n  - For a specified amount of time (2)\n\nSelect option: ', 'x', False, False)

    ciCompoundingMap = {
                      'day': 1,
                      'year': 1,
                      'quarter': 4,
                      'month': 12,
                      'week': 52}

    if compareType == 1:
        compareFinalValue = checkInt('x', 'x', '>> Please enter a valid number', 'Enter the value to compare the two accounts up to ($): ', 'x', True, True)
        compareTimeUnit = checkTimeFormat('What time unit should the projections increment in (year, quarter, month, week, day): ', '>> Please enter a valid time unit', 'x', False, False)

        compareTimeUnit = ciCompoundingMap.get(compareTimeUnit.lower(), 0)

        time1 = 0
        time2 = 0
        

        while True:
            amountAcc1 = ciPrincipleAmount1 * (1 + ciInterestRate1 / 100 / compareTimeUnit) ** (compareTimeUnit * time1)

            timeProjectionsAcc1 = []
            timeProjectionsAcc2 = []

            timeProjectionsAcc1.append(amountAcc1)

            if amountAcc1 >= compareFinalValue:
                break

            time1 += 1

        while True:
            amountAcc2 = ciPrincipleAmount2 * (1 + ciInterestRate2 / 100 / compareTimeUnit) ** (compareTimeUnit * time2)

            timeProjectionsAcc2.append(amountAcc2)

            if amountAcc2 >= compareFinalValue:
                break

            time2 += 1

        index = 0
        cycle = 0
        p2Print = ''
        print('\nComparison over time:')
        print('A1 = Account 1 and A2 = Account 2')
        print('-' * 30)
        for i in timeProjectionsAcc1:
            cycle += 1

            if i > compareFinalValue:
                p1Print = 'Target Reached'
            else:
                p1Print = round(i, 2)
            
            if p2Print != 'Target Reached':
                if timeProjectionsAcc2[index] > compareFinalValue:
                    p2Print = 'Target Reached'
                else:
                    p2Print = round(timeProjectionsAcc2[index], 2)

            print(f'{ciInterestRateTimeUnit1.capitalize()} {cycle}: A1: {p1Print}, A2: {p2Print}')

            index += 1

    elif compareType == 2:
        cls()
        compareTimeAmount = checkInt('x', 'x', '>> Please enter a valid number', 'How much time to predict for (unit will be asked next): ', 'x', False, False)
        compareTimeAmountUnit = checkTimeFormat('What time unit (year, quarter, month, week, day): ', '>> Please enter a valid time unit', 'x', 0, 0)
        compareTimeAmountUnitStr = compareTimeAmountUnit

        compareTimeAmountUnit = ciCompoundingMap.get(compareTimeAmountUnit.lower(), 0)

        timeProjectionsAcc1 = []
        timeProjectionsAcc2 = []

        for time in range(1, compareTimeAmount + 1):
            amountAcc1 = ciPrincipleAmount1 * (1 + ciInterestRate1 / 100 / compareTimeAmountUnit) ** (compareTimeAmountUnit * time)
            amountAcc2 = ciPrincipleAmount2 * (1 + ciInterestRate2 / 100 / compareTimeAmountUnit) ** (compareTimeAmountUnit * time)

            timeProjectionsAcc1.append(amountAcc1)
            timeProjectionsAcc2.append(amountAcc2)

        print('\nComparison over time:')
        print('A1 = Account 1 and A2 = Account 2')
        print('-' * 30)

        for i in range(compareTimeAmount):
            print(f'{compareTimeAmountUnitStr} {i + 1}: A1|{timeProjectionsAcc1[i]:.2f}, A2|{timeProjectionsAcc2[i]:.2f}')

    else:
        raise Exception("Value isn't between specified numbers")
        # raise an error if the compareType chekInt function fails and assigns a number that is not 1 or 2.
    
    input('Press enter to return to menu')
    menuBar()

def moduleFour():
    cls()
    print('Module 4: Model a CI savings account with regular deposits\n')

    ciPrincipleAmount, ciInterestRate, ciInterestRateTimeUnit, ciCompoundingTimeUnit = createCompoundAccount()

    initialGift = checkInt('x', 'x', '>> Please enter a valid number', 'Enter the initial gift amount (in $): ', 'x', True, True)
    monthlyDeposit = checkInt('x', 'x', '>> Please enter a valid number', 'Enter the monthly deposit amount (in $): ', 'x', False, True)
    savingsDuration = checkInt('x', 'x', '>> Please enter a valid number', 'Enter the savings duration (in years): ', 'x', False, False)

    totalInitialGift = initialGift * (1 + ciInterestRate / 100) ** (ciCompoundingTimeUnit * savingsDuration)
    totalContributions = monthlyDeposit * 12 * savingsDuration
    totalAmount = totalInitialGift + totalContributions

    cls()

    print(f'With an initial gift of ${initialGift}, and a monthly deposit of ${monthlyDeposit},')
    print(f'compounded at an interest rate of {ciInterestRate}% per {ciInterestRateTimeUnit},')
    print(f'you will have a total of ${totalAmount:.2f} after {savingsDuration} years.')

    targetAmount = checkInt('x', 'x', '>> Please enter a valid number', 'Enter the target amount for buying the car (in $): ', 'x', False, True)

    if totalAmount >= targetAmount:
        print(f'\nCongratulations! You will have enough money (${totalAmount:.2f}) to buy your car!')
    else:
        print(f'\nUnfortunately, you will not have enough money (${totalAmount:.2f}) to buy your car.')

        remainingMonths = savingsDuration * 12
        minMonthlyDeposit = (targetAmount - totalInitialGift) / (12 * remainingMonths)

        print(f'You would need to deposit at least ${minMonthlyDeposit:.2f} per month to just manage to reach your target of ${targetAmount}.')

    input('\nPress enter to return to menu')
    menuBar()

def moduleFive():
    pass

def exitProgram():
    cls()
    print('Thanks for playing!\n')
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
