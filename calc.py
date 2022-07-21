# This program consists of three important functions:
#     1. askUser(): runs first to ask user which operation he/she wants to do, and which numbers
#     to calculate.
#     2. askAmounts(pushOperation): asks user which numbers to calculate.
# 
# Two secondary tier functions:
#     1. exitProgram(): used to exit the program when you type "exit" as operation.
#     2. errorMessages(errorType): prompts to inform about possible error solutions.

# Used for exitProgram() function
import sys

print("\n--- Welcome to Calculator! ---\n") 

# VALID_OPERATIONS constant consists of the operations that the program is capable of calculating
# with. Includes addition +, subtraction -, multiplication *, division /.
VALID_OPERATIONS = [
    "+", "-",
    "*", "/"
    ]

# operation_library variable consits of keywords for the signs in the VALID_OPERATIONS constant.
# If the user input for the operation isn't found in VALID_OPERATIONS, it searches in this
# dictionary instead.
operation_library = {
    "addition": "+",
    "subtraction": "-",
    "multiplication": "*",
    "division": "/"
    }

error_library = [
    "noNumbers", "operationInvalid",
    "divideZero", "missingInput"
    ]

# errorMessages() is a function that points out several possible error reasons, to be more precise. 
def errorMessages(errorType):
    
    if errorType == "noNumbers":       
        print("You didn't type a number. You can't use words as number input.")
        
    elif errorType == "operationInvalid":
        print("The operation you wanted to do is invalid, the program isn't capable of accomplishing it.")
    
    elif errorType == "divideZero":
        print("You tried dividing by 0. This isn't possible and results an error.")
    
    elif errorType == "missingInput":
        print("Missing input. You either didn't put an operation type or numbers, or both.")
        print("You can't put only one number as input, you need at least two.")
        print("You can't put more than one input in the operation space. Only one type.")
    
# exitProgram() function is used for exiting the program.
def exitProgram():
    sys.exit("Program Exited")

# calculatorSession(operation, numbers) function is used to do the actual calculating. This is 
# run at the end of the program after the inputs are done by the user.
def calculatorSession(operation, numbers):
    
    # This is the total result of the calculation. It is printed when everything is done.
    numbersTotal = 0 
    
    # For each number in the numbers paremeter that was pushed from askAmounts function...
    for number in numbers:
        if numbersTotal == 0: # If the numbersTotal is 0...
            numbersTotal = number # Replace it with the first number in the numbers list.
            
        elif operation == "+": # If the operation chosen is addition...
            numbersTotal = numbersTotal + number # Add the numbers with the numbersTotal.
            
        elif operation == "-": # If the operation chosen is subtraction...
            numbersTotal = numbersTotal - number # Subtract the numbers with the numbersTotal.
            
        elif operation == "*": # If the operation chosen is multiplication...
            numbersTotal = numbersTotal * number # Multiply the numbers with the numbersTotal.
            
        elif operation == "/": # If the operation chosen is division...
            if number != 0: # If any of the numbers are DIFFERENT than 0...
                numbersTotal = numbersTotal / number # Divide the numbers with the numbersTotal.
            else: # If it is 0...
                errorMessages(error_library[2]) # Prompt error and quit the program.   
                numbersTotal = 0 # This assigns meaning that the program shouldn't function anymore.
       
    # If the numbersTotal isn't 0, it posts the total number.
    if numbersTotal != 0:
        print("\n>> Total:", numbersTotal, "<<\n")

# askUser() is used to ask the user which operation they want to perform with, and what 
# numbers it is that they want to calculate. 
def askUser():
    print("Enter the numbers | Enter the operation type")
    print("Example: 40 50 10 | +")
    userInput = input("> ")
    
    # Splits the input by / to separate the operations and the numbers
    userInputSpl = userInput.split("|")
    
    # Removes whitespace from both inputs.
    userInputNumbers = userInputSpl[0].strip()
    userInputOperation = userInputSpl[1].strip()
    
    # Splits the numbers to a separate variable to work on.
    userInputNumbersSplit = userInputNumbers.split()
    
    # If the length of the numbers is greater than 1 (you can't just enter one number), and
    # the operation input is only equal to one (you can't put more than one input), it...
    if len(userInputNumbersSplit) > 1 and len(userInputOperation) == 1:
        try: # tries to transform the number to an integer.
            userNumbers = [int(numbers) for numbers in userInputNumbersSplit]
            
            # If the operation is in the VALID_OPERATIONS constant, it pushes it to the
            # calculatorSession() function.
            if userInputOperation in VALID_OPERATIONS:
                calculatorSession(userInputOperation, userNumbers)
                
            # If it isn't...
            else: 
                # It checks in the operation_library dictionary, if it's found there
                # it pushes it again to the calculatorSession() function.
                if userInputOperation in operation_library:
                    # Assigns the sign of the formula instead of the typed word.
                    # For example if the user typed "addition", it pushes "+"
                    userInputOperation = operation_library[userInputOperation]
                    calculatorSession(userInputOperation, userNumbers)
                
                # If it isn't in the dictionary, then it's an invalid operation type.
                else:
                    errorMessages(error_library[1])
        except: # If an error showed up, most probably the user entered a letter instead of a number.
            errorMessages(error_library[0])
    # If the user didn't type more than 2 numbers or/and only one operation, this error pops up.
    else:
        errorMessages(error_library[3])
        
# The beginning of the program. 
askUser()  




