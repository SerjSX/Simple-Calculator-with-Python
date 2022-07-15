# This program consists of three important functions:
#     1. askOperation(): runs first to ask user which operation he/she wants to do.
#     2. askAmounts(pushOperation): asks user which numbers to calculate.
#     3. calculatorSession(operation, numbers): this is where the calculation is being done.
# 
# Two secondary tier functions:
#     1. exitProgram(): used to exit the program when you type "exit" as operation.
#     2. errorMessages(): prompts to inform about possible error solutions.

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

# errorMessages() is a function that points out several possible error reasons, to be more precise. 
def errorMessages():
    print("Possible Error 1: You didn't type a number. You can't use words as number input.")
    print("Possible Error 2: The operation you wanted to do is invalid, the program isn't capable of accomplishing it.")
    print("Possible Error 3: You tried dividing by 0. This isn't possible and results an error.\n")

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
                errorMessages() # Prompt error and quit the program.
        
    # Prints the result!
    print("\n>>", numbersTotal, "<<\n")
    

# askAmounts(pushOperation) function is used to ask the user for the amounts that will be 
# calculated. This is the second function that is run, after askOperation().
def askAmounts(pushOperation):
    print("Insert the amounts you will calculate, separate with ','.")
    userNumbers = input("Numbers: ")
    
    # This splits the numbers by ',', so it would be a list having the numbers in it.
    userNumbersSplit = userNumbers.split(",")
    
    try: # The program tries to transform the number to an integer.
        userNumbersSplit = [int(numbers) for numbers in userNumbersSplit]
        
        # If succeeded, it pushes it to the calculation function.
        calculatorSession(pushOperation, userNumbersSplit)
    except: # If an error showed up, the errorMessages() is run. Most probably the user entered a letter instead of a number.
        errorMessages()
        
# askOperation() is used to ask the user which operation they want to perform with.
# It is the first function that is run in this program.
def askOperation():
    print("What operation will you perform?")
    print("Your choices: + (addition), - (subtraction), * (multiplication), / (division).")
    print("Type 'exit' if you would like to quit the application.")
    chosenOperation = input("Operation: ")
    
    # Removes any whitespace from the input. Sometimes users put a space after/before writing 
    # which operation they want to perform. It takes care of that issue.
    chosenOperationStrip = chosenOperation.strip()
    print("")
    
    # For making it more precise, another variable is used throughout the program.
    userOperation = chosenOperationStrip
    
    # If the chosen operation is in the VALID_OPERATIONS constant...
    if (chosenOperation in VALID_OPERATIONS): 
        askAmounts(userOperation) # Push it to the askAmounts function.
    
    # If the user typed 'exit'...
    elif (userOperation == 'exit'): 
        exitProgram() # Exit the program.
        
    # If it isn't in the VALID_OPERATIONS constant...
    else:
        # If it is in the operation_library dictionary...
        if userOperation in operation_library:
            # Replace the userOperation variable value with the sign of the 
            # operation the user typed as the keyword instead of sign.
            userOperation = operation_library[userOperation]
            askAmounts(userOperation) # Push it to the askAmounts function.
        # If it isn't in the operation_library dictionary...
        else: 
            errorMessages() # Prompt the errors. 

# The beginning of the program. askOperation() asks the user which operation he/she
# wants to perform with.
askOperation()  