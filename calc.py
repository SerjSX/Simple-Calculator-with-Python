def calculatorSession(chosenOperation, numbersSet):
    numbersTotal = None

    if chosenOperation == '+' or chosenOperation == 'addition':
        try:
            for numbers in numbersSet:
                if numbersTotal == None:
                    numberintone = int(numbers)
                    numbersTotal = numberintone
                else:
                    numberinttwo = int(numbers)
                    numbersTotal = numbersTotal + numberinttwo

        except:
            print("Possible error: you didn't insert numbers! Letters aren't allowed.")
            exit()

    elif chosenOperation == '-' or chosenOperation == 'subtraction':
        try:
            for numbers in numbersSet:
                if numbersTotal == None:
                    numberintone = int(numbers)
                    numbersTotal = numberintone
                else:
                    numberinttwo = int(numbers)
                    numbersTotal = numbersTotal - numberinttwo    
        except:
            print("Possible error: you didn't insert numbers! Letters aren't allowed.")
            exit()

    elif chosenOperation == '*' or chosenOperation == 'multiplication':
        try:
            for numbers in numbersSet:
                if numbersTotal == None:
                    numberintone = int(numbers)
                    numbersTotal = numberintone
                else:
                    numberinttwo = int(numbers)
                    numbersTotal = numbersTotal * numberinttwo                            
        except:
            print("Possible error: you didn't insert numbers! Letters aren't allowed.")
            exit()

    elif chosenOperation == '/' or chosenOperation == 'division':
        try:
            for numbers in numbersSet:
                if numbersTotal == None:
                    numberintone = int(numbers)
                    numbersTotal = numberintone
                else:
                    numberinttwo = int(numbers)
                    numbersTotal = numbersTotal / numberinttwo
        
        except:
            print("Possible error 1: you tried dividing by 0, which isn't possible. If that's not the case, report in Github issues with explaining everything in detail.")
            print("Possible error 2: you didn't insert numbers! Letters aren't allowed.")
            exit()

    print("---")
    print("Result:", numbersTotal)
    print("---")

print("Welcome to Calculator!")
print("")

def askUser():
    print("What operation will you perform? Your choices: + (addition), - (subtraction), * (multiplication), / (division). Type 'exit' if you would like to quit the application.")
    chosenOperation = input("Operation: ")
    print("")

    if (chosenOperation == 'exit'):
        print("Exiting...")
        exit()

    if (chosenOperation == '+' or chosenOperation == '-' or chosenOperation == '*' or chosenOperation == '/' or chosenOperation == 'addition' or chosenOperation == 'subtraction' or chosenOperation == 'multiplication' or chosenOperation == 'division'):
        print("Insert the amounts you will calculate, separate with ','.")
        userNumbers = input("Numbers: ")
        userNumbersSplit = userNumbers.split(",")

        calculatorSession(chosenOperation, userNumbersSplit)
    else:
        print("You didn't insert an operation that the program is capable of calculating as!")
        exit()

askUser()
