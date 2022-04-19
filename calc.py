number1I = 'null'
number2I = 'null'
number3I = 'null'
number4I = 'null'
number5I = 'null'

def calculatorSession(chosenAmount):
    def amountTwo():
        def calculationMethodTwo(calculation, number1, number2):
            number1str = str(number1)
            number2str = str(number2)

            if (calculation == '+' and number1I != 'null' and number2I != 'null'):
                calculatedAmount = number1 + number2
                calculatedAmountI = str(calculatedAmount)
                print("")
                print("--")
                print(number1str + " + " + number2str + " = " + calculatedAmountI)
                print("--")
                print("")

            elif (calculation == '-' and number1I != 'null' and number2I != 'null'):
                calculatedAmount = number1 - number2
                calculatedAmountI = str(calculatedAmount)
                print("")
                print("--")
                print(number1str + " - " + number2str + " = " + calculatedAmountI)
                print("--")
                print("")

            elif (calculation == '*' and number1I != 'null' and number2I != 'null'):
                calculatedAmount = number1 * number2
                calculatedAmountI = str(calculatedAmount)
                print("")
                print("--")
                print(number1str + " * " + number2str + " = " + calculatedAmountI)
                print("--")
                print("")

            elif (calculation == '/' and number2 != 0 and number1I != 'null' and number2I != 'null'):
                calculatedAmount = number1 / number2
                calculatedAmountI = str(calculatedAmount)
                print("")
                print("--")
                print(number1str + " / " + number2str + " = " + calculatedAmountI)
                print("--")
                print("")

            else:
                print("")
                print("--")
                print("This calculation is invalid.")
                print("Possible reason 1: you tried dividing with 0. That's not possible and it results math error, infinity!")
                print("Possible reason 2: you typed the word for the calculation method instead of the sign. Please use the sign as it's shorter and simpler.")
                print("--")
                print("")

        print("You chose amount two. Now you will insert the two numbers that you will calculate.")
        number1 = input("First number: ")

        if number1 != 'exit':
            try:
                number1cp = number1.replace(" ", "")
                number1I = int(number1cp)
            except:
                print("You didn't enter a number! Exiting...")
                exit()
        else:
            print("Exiting...")
            exit()

        print("")
        number2 = input("Second number: ")

        if number2 != 'exit':
            try:
                number2cp = number2.replace(" ", "")
                number2I = int(number2cp)
            except:
                print("You didn't enter a number! Exiting...")
                exit()
        else:
            print("Exiting...")
            exit()

        print("")
        print("Now you will type the calculation method you want to use. There are three available...")
        print("")
        print("> Addition: +")
        print("> Subtraction: -")
        print("> Multiplication: *")
        print("> Division: /")
        print("")
        calculation = input("What calculation method would you like to calculate it with? Type the sign (+/-/*/'/'): ")

        calculationMethodTwo(calculation, number1I, number2I)

        askAmount()

    def amountThree():
        def calculationMethodThree(calculation, number1, number2, number3):
            number1str = str(number1)
            number2str = str(number2)
            number3str = str(number3)
            if (calculation == '+' and number1I != 'null' and number2I != 'null' and number3I != 'null'):
                calculatedAmount = number1 + number2 + number3
                calculatedAmountI = str(calculatedAmount)
                print("")
                print("--")
                print(number1str + " + " + number2str + " + " + number3str + " = " + calculatedAmountI)
                print("--")
                print("")

            elif (calculation == '-' and number1I != 'null' and number2I != 'null' and number3I != 'null'):
                calculatedAmount = number1 - number2 - number3
                calculatedAmountI = str(calculatedAmount)
                print("")
                print("--")
                print(number1str + " - " + number2str + " - " + number3str + " = " + calculatedAmountI)
                print("--")
                print("")

            elif (calculation == '*' and number1I != 'null' and number2I != 'null' and number3I != 'null'):
                calculatedAmount = number1 * number2 * number3
                calculatedAmountI = str(calculatedAmount)
                print("")
                print("--")
                print(number1str + " * " + number2str + " * " + number3str + " = " + calculatedAmountI)
                print("--")
                print("")

            elif (calculation == '/' and number2 != 0 and number3 != 0 and number1I != 'null' and number2I != 'null' and number3I != 'null'):
                calculatedAmount = number1 / number2 / number3
                calculatedAmountI = str(calculatedAmount)
                print("")
                print("--")
                print(number1str + " / " + number2str + " / " + number3str + " = " + calculatedAmountI)
                print("--")
                print("")

            else:
                print("")
                print("--")
                print("This calculation is invalid.")
                print("Possible reason 1: you tried dividing with 0. That's not possible and it results math error, infinity!")
                print("Possible reason 2: you typed the word for the calculation method instead of the sign. Please use the sign as it's shorter and simpler.")
                print("--")
                print("")

        print("You chose amount three. Now you will insert the three numbers that you will calculate.")
        number1 = input("First number: ")

        if number1 != 'exit':
            try:
                number1cp = number1.replace(" ", "")
                number1I = int(number1cp)
            except:
                print("You didn't enter a number! Exiting...")
                exit()
        else:
            print("Exiting...")
            exit()

        print("")
        number2 = input("Second number: ")

        if number2 != 'exit':
            try:
                number2cp = number2.replace(" ", "")
                number2I = int(number2cp)
            except:
                print("You didn't enter a number! Exiting...")
                exit()
        else:
            print("Exiting...")
            exit()

        print("")
        number3 = input("Third number: ")

        if number3 != 'exit':
            try:
                number3cp = number3.replace(" ", "")
                number3I = int(number3cp)
            except:
                print("You didn't enter a number! Exiting...")
                exit()
        else:
            print("Exiting...")
            exit()

        print("")
        print("Now you will type the calculation method you want to use. There are three available...")
        print("")
        print("> Addition: +")
        print("> Subtraction: -")
        print("> Multiplication: *")
        print("> Division: /")
        print("")
        calculation = input("What calculation method would you like to calculate it with? Type the sign (+/-/*/'/'): ")

        calculationMethodThree(calculation, number1I, number2I, number3I)

        askAmount()

    def amountFour():
        def calculationMethodFour(calculation, number1, number2, number3, number4):
            number1str = str(number1)
            number2str = str(number2)
            number3str = str(number3)
            number4str = str(number4)
            if (calculation == '+' and number1I != 'null' and number2I != 'null' and number3I != 'null' and number4I != 'null'):
                calculatedAmount = number1 + number2 + number3 + number4
                calculatedAmountI = str(calculatedAmount)
                print("")
                print("--")
                print(number1str + " + " + number2str + " + " + number3str + " + " + number4str + " = " + calculatedAmountI)
                print("--")
                print("")

            elif (calculation == '-' and number1I != 'null' and number2I != 'null' and number3I != 'null' and number4I != 'null'):
                calculatedAmount = number1 - number2 - number3 - number4
                calculatedAmountI = str(calculatedAmount)
                print("")
                print("--")
                print(number1str + " - " + number2str + " - " + number3str + " - " + number4str + " = " + calculatedAmountI)
                print("--")
                print("")

            elif (calculation == '*' and number1I != 'null' and number2I != 'null' and number3I != 'null' and number4I != 'null'):
                calculatedAmount = number1 * number2 * number3 * number4
                calculatedAmountI = str(calculatedAmount)
                print("")
                print("--")
                print(number1str + " * " + number2str + " * " + number3str + " * " + number4str + " = " + calculatedAmountI)
                print("--")
                print("")

            elif (calculation == '/' and number2 != 0 and number3 != 0 and number4 != 0 and number1I != 'null' and number2I != 'null' and number3I != 'null' and number4I != 'null'):
                calculatedAmount = number1 / number2 / number3 / number4
                calculatedAmountI = str(calculatedAmount)
                print("")
                print("--")
                print(number1str + " / " + number2str + " / " + number3str + " / " + number4str + " = " + calculatedAmountI)
                print("--")
                print("")

            else:
                print("")
                print("--")
                print("This calculation is invalid.")
                print("Possible reason 1: you tried dividing with 0. That's not possible and it results math error, infinity!")
                print("Possible reason 2: you typed the word for the calculation method instead of the sign. Please use the sign as it's shorter and simpler.")
                print("--")
                print("")

        print("You chose amount four. Now you will insert the four numbers that you will calculate.")
        number1 = input("First number: ")

        if number1 != 'exit':
            try:
                number1cp = number1.replace(" ", "")
                number1I = int(number1cp)
            except:
                print("You didn't enter a number! Exiting...")
                exit()
        else:
            print("Exiting...")
            exit()

        print("")
        number2 = input("Second number: ")

        if number2 != 'exit':
            try:
                number2cp = number2.replace(" ", "")
                number2I = int(number2cp)
            except:
                print("You didn't enter a number! Exiting...")
                exit()
        else:
            print("Exiting...")
            exit()

        print("")
        number3 = input("Third number: ")

        if number3 != 'exit':
            try:
                number3cp = number3.replace(" ", "")
                number3I = int(number3cp)
            except:
                print("You didn't enter a number! Exiting...")
                exit()
        else:
            print("Exiting...")
            exit()

        print("")
        number4 = input("Fourth number: ")

        if number4 != 'exit':
            try:
                number4cp = number4.replace(" ", "")
                number4I = int(number4cp)
            except:
                print("You didn't enter a number! Exiting...")
                exit()
        else:
            print("Exiting...")
            exit()

        print("")
        print("Now you will type the calculation method you want to use. There are three available...")
        print("")
        print("> Addition: +")
        print("> Subtraction: -")
        print("> Multiplication: *")
        print("> Division: /")
        print("")
        calculation = input("What calculation method would you like to calculate it with? Type the sign (+/-/*/'/'): ")

        calculationMethodFour(calculation, number1I, number2I, number3I, number4I)

        askAmount()

    def amountFive():
        def calculationMethodFive(calculation, number1, number2, number3, number4, number5):
            number1str = str(number1)
            number2str = str(number2)
            number3str = str(number3)
            number4str = str(number4)
            number5str = str(number5)
            if (calculation == '+' and number1I != 'null' and number2I != 'null' and number3I != 'null' and number4I != 'null' and number5I != 'null'):
                calculatedAmount = number1 + number2 + number3 + number4 + number5
                calculatedAmountI = str(calculatedAmount)
                print("")
                print("--")
                print(number1str + " + " + number2str + " + " + number3str + " + " + number4str + " + " + number5str + " = " + calculatedAmountI)
                print("--")
                print("")

            elif (calculation == '-' and number1I != 'null' and number2I != 'null' and number3I != 'null' and number4I != 'null' and number5I != 'null'):
                calculatedAmount = number1 - number2 - number3 - number4 - number5
                calculatedAmountI = str(calculatedAmount)
                print("")
                print("--")
                print(number1str + " - " + number2str + " - " + number3str + " - " + number4str + " - " + number5str + " = " + calculatedAmountI)
                print("--")
                print("")

            elif (calculation == '*' and number1I != 'null' and number2I != 'null' and number3I != 'null' and number4I != 'null' and number5I != 'null'):
                calculatedAmount = number1 * number2 * number3 * number4 * number5
                calculatedAmountI = str(calculatedAmount)
                print("")
                print("--")
                print(number1str + " * " + number2str + " * " + number3str + " * " + number4str + " * " + number5str + " = " + calculatedAmountI)
                print("--")
                print("")

            elif (calculation == '/' and number2 != 0 and number3 != 0 and number4 != 0 and number5 != 0 and number1I != 'null' and number2I != 'null' and number3I != 'null' and number4I != 'null' and number5I != 'null'):
                calculatedAmount = number1 / number2 / number3 / number4 / number5
                calculatedAmountI = str(calculatedAmount)
                print("")
                print("--")
                print(number1str + " / " + number2str + " / " + number3str + " / " + number4str + " / " + number5str + " = " + calculatedAmountI)
                print("--")
                print("")

            else:
                print("")
                print("--")
                print("This calculation is invalid.")
                print("Possible reason 1: you tried dividing with 0. That's not possible and it results math error, infinity!")
                print("Possible reason 2: you typed the word for the calculation method instead of the sign. Please use the sign as it's shorter and simpler.")
                print("--")
                print("")

        print("You chose amount five (max). Now you will insert the five numbers that you will calculate.")
        number1 = input("First number: ")

        if number1 != 'exit':
            try:
                number1cp = number1.replace(" ", "")
                number1I = int(number1cp)
            except:
                print("You didn't enter a number! Exiting...")
                exit()
        else:
            print("Exiting...")
            exit()

        print("")
        number2 = input("Second number: ")

        if number2 != 'exit':
            try:
                number2cp = number2.replace(" ", "")
                number2I = int(number2cp)
            except:
                print("You didn't enter a number! Exiting...")
                exit()
        else:
            print("Exiting...")
            exit()

        print("")
        number3 = input("Third number: ")

        if number3 != 'exit':
            try:
                number3cp = number3.replace(" ", "")
                number3I = int(number3cp)
            except:
                print("You didn't enter a number! Exiting...")
                exit()
        else:
            print("Exiting...")
            exit()

        print("")
        number4 = input("Fourth number: ")

        if number4 != 'exit':
            try:
                number4cp = number4.replace(" ", "")
                number4I = int(number4cp)
            except:
                print("You didn't enter a number! Exiting...")
                exit()
        else:
            print("Exiting...")
            exit()

        print("")
        number5 = input("Fifth number: ")

        if number5 != 'exit':
            try:
                number5cp = number5.replace(" ", "")
                number5I = int(number5cp)
            except:
                print("You didn't enter a number! Exiting...")
                exit()
        else:
            print("Exiting...")
            exit()

        print("")
        print("Now you will type the calculation method you want to use. There are three available...")
        print("")
        print("> Addition: +")
        print("> Subtraction: -")
        print("> Multiplication: *")
        print("> Division: /")
        print("")
        calculation = input("What calculation method would you like to calculate it with? Type the sign (+/-/*/'/'): ")

        calculationMethodFive(calculation, number1I, number2I, number3I, number4I, number5I)

        askAmount()

    if (chosenAmount == 2):
        amountTwo()
    elif (chosenAmount == 3):
        amountThree()
    elif (chosenAmount == 4):
        amountFour()
    elif (chosenAmount == 5):
        amountFive()
    else:
        print("Uh oh... An unexpected error occured. Are you sure you entered a number that the program is capable of calculating?")

print("Welcome to Calculator!")
print("")

def askAmount():
    print("Type the amount of numbers you will calculate. You can up to 5 and minimum 2, because you can't calculate a number by itself.")
    chosenAmount = input("Amount: ")
    print("")

    if (chosenAmount != "exit"):
        try:
            chosenAmountI = int(chosenAmount)
        except:
            print("You didn't enter a number!")
    else:
        print("Exiting...")
        exit()

    if (chosenAmountI < 2 or chosenAmountI > 5):
        print("You entered an amount that the program isn't capable of calculating.")
        exit()
    else:
        calculatorSession(chosenAmountI)

askAmount()
