print("\n--- Welcome to Calculator! ---\n")

# This program consists of two functions: 
#     1. PRIMARY function which is at the bottom of the page
#     2. SECONDARY - calculatorSession(chosenOperation, numbersSet) 
# The former operates first in order to ask for the inputs from the user, which later on passes
# to the calculatorSession function with filling in the paremeters. The latter is used for 
# the actual calculating processes which prints out the results at the end.

# The below constant variable inputs are the calculation methods that the user can do 
# calculations with.
# There's addition, subtractions, multiplication, and division. Both by name and sign can be used.
VALID_OPERATIONS = [ 
    "+", "addition", "-", "subtraction", 
    "*", "multiplication", "/", "division"
    ]

# SECONDARY FUNCTION
def calculatorSession(chosenOperation, numbersSet): 

# The variable below is used as the result of the calculations, at the end of the calculation it is 
# printed. It starts with None indicating that it is empty and will be filled later on.
    numbersTotal = None 

# First chosen operation is if the chosen operation (+|-|*|/) is either 0 or 1 from the 
# VALID_OPERATOR constant, which is addition.
    if chosenOperation in VALID_OPERATIONS[0:2]:
        for numbers in numbersSet: # for each number in numbersSet which we pushed from askUser...
            if numbersTotal == None: # if the numbersTotal is None (always is at first)...
                numbersTotal = numbers # set the first number as default
            else: # if it isn't None...
                numbersTotal = numbersTotal + numbers # do the calculation and asign it to the 
                # numbersTotal variable, which already has the first number.

# Second chosen operation is if the chosen operation is either 2 or 3 from the VALID_OPERATOR
# constant, which is subtraction.
    elif chosenOperation in VALID_OPERATIONS[2:4]:
        for numbers in numbersSet:
            if numbersTotal == None:
                numbersTotal = numbers
            else:
                numbersTotal = numbersTotal - numbers    

# Third chosen operation is if the chosen operation is either 4 or 5 from the VALID_OPERATOR 
# constant, which is multiplication.
    elif chosenOperation in VALID_OPERATIONS[4:6]:
        for numbers in numbersSet:
            if numbersTotal == None:
                numbersTotal = numbers
            else:
                numbersTotal = numbersTotal * numbers                            

# Fourth chosen operation is if the chosen operation is either 6 or 7 from the VALID_OPERATOR
# constant, which is division.
    elif chosenOperation in VALID_OPERATIONS[6:8]:
        for numbers in numbersSet:
            try: # Try this function, because if the user inserts 0 as second number it'll show error.
                if numbersTotal == None:
                    numbersTotal = numbers
                else:
                    numbersTotal = numbersTotal / numbers

            except: # Hence if error is shown, it points out that you can't divide by 0!
                print("\n --- Error: You can't divide by 0! --- \n")
                exit()

    print("\n>>", numbersTotal, "<<\n")


# PRIMARY FUNCTION

# 1. Asks which operation the user wants to perform: +|-|*|/
print("What operation will you perform?")
print("Your choices: + (addition), - (subtraction), * (multiplication), / (division).")
print("Type 'exit' if you would like to quit the application.")
chosenOperation = input("Operation: ")
chosenOperationStrip = chosenOperation.strip() # Removes whitespace, maybe the user accidentally put
# a space after/before inserting the operation type.
print("") # For better appearance without everything being on top of each other, a space is put.

if (chosenOperationStrip == 'exit'): # If the user typed exit, it quits the application.
    exit()

# 2. Asks which numbers the user wants to calculate
if (chosenOperationStrip in VALID_OPERATIONS): 
    # if the chosen operation is valid in the VALID_OPERATIONS constant, asks to insert numbers.
    print("Insert the amounts you will calculate, separate with ','.")
    userNumbers = input("Numbers: ")
    userNumbersSplit = userNumbers.split(",") # Splits the numbers by comma
        
    try: # Tries to convert the string numbers to integers, if the user put letters it'll be obvious...
        userNumbersSplit = [int(numbers) for numbers in userNumbersSplit]
    except: # and it'll print out an error that points out that you didn't enter a number.
        print("\n --- Error: you didn't enter a number! --- \n")
        exit()

    # Push the inputs to the calculatorSession function to start the calculations.
    calculatorSession(chosenOperationStrip, userNumbersSplit)
else: # If the chosen operation isn't in the VALID_OPERATIONS constant, it quits the application.
    print("You didn't insert an operation that the program is capable of calculating as!")
    exit()
