number1I = 'null'
number2I = 'null'

print("Welcome to Calculator!")
print("")

def calculatorSession():
    print("Please insert the first number you will calculate. If you want to exit just type exit instead.")
    number1 = input("First number: ")

    if number1 != 'exit':
        try:
            number1I = int(number1)
        except:
            print("You didn't enter a number! Exiting...")
            exit()
    else:
        print("Exiting...")
        exit()

    print("")
    print("Now insert the number you want to calculate it with. If you want to exit just type exit instead.")
    number2 = input("Second number: ")

    if number2 != 'exit':
        try:
            number2I = int(number2)
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
    print("The first number you chose is " + number1 + ", the second number you chose is " + number2 + ".")
    print("")
    calculation = input("What calculation method would you like to calculate it with? Type the sign (+/-/*/'/'): ")

    def calculationMethod(calculation, number1, number2):
        if (calculation == '+' and number1I != 'null' and number2I != 'null'):
            additionCalc = number1 + number2
            print("")
            print("--")
            print(additionCalc)
            print("--")
            print("")
        elif (calculation == '-' and number1I != 'null' and number2I != 'null'):
            subtractionCalc = number1 - number2
            print("")
            print("--")
            print(subtractionCalc)
            print("--")
            print("")
        elif (calculation == '*' and number1I != 'null' and number2I != 'null'):
            multiplyCalc = number1 * number2
            print("")
            print("--")
            print(multiplyCalc)
            print("--")
            print("")
        elif (calculation == '/' and number2 != 0 and number1I != 'null' and number2I != 'null'):
            divideCalc = number1 / number2
            print("")
            print("--")
            print(divideCalc)
            print("--")
            print("")
        else:
            print("")
            print("--")
            print("This calculation is invalid.")
            print("Possible reason 1: you tried dividing with 0. That's not possible and it results math error.")
            print("Possible reason 2: you typed the word for the calculation method instead of the sign. Please use the sign as it's shorter and simpler.")
            print("--")
            print("")


    calculationMethod(calculation, number1I, number2I)

    print("New session...")
    calculatorSession()

calculatorSession()
