import re
print("Calculator - Home Screen")
print("Type 'Quit' to Exit\n")
previous = 0 #Previous variable holds the value of previously calculated results.
run = True

def performMath():
    global run
    global previous
    equation = ""

    if previous == 0:
        equation = input("Enter Equation:")
    else:
        equation = input(str(previous))

    if equation == 'Quit':
        print("Goodbye")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()""]', '', equation)

        if previous == 0:
            previous = eval(equation) #eval built-in function is used to perform complex mathematical operations
        else:
            previous = eval(str(previous)+equation)

while run:
    performMath()

