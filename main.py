def arithmetic_arranger(problems, solutions=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    row1 = ""           # Row for the first number
    row2 = ""           # Row for the operator and second number
    row3 = ""           # Row for the result bar
    row4 = ""           # Ror for the result

    for i, problem in enumerate(problems):
        firstNumber, operator, secondNumber = problem.split()

        # Array must have a + or - operator
        if (operator != "+" and operator != "-"):
            return "Error: Operator must be '+' or '-'."

        # Array must contain numbers
        if (firstNumber.isdigit() == False or secondNumber.isdigit() == False):
            return "Error: Numbers must only contain digits."

        # Array numbers must be a maximum of 4 digits
        if len(firstNumber) >= 5 or len(secondNumber) >= 5:
            return "Error: Numbers cannot be more than four digits."

        # Make the math
        if operator == "+":
            solution = int(firstNumber) + int(secondNumber)
        else:
            solution = int(firstNumber) - int(secondNumber)

        numberLength = len(max([firstNumber, secondNumber], key=len))

        row1 += firstNumber.rjust(numberLength+2)
        row2 += operator + secondNumber.rjust(numberLength+1)
        row3 += "-" * (numberLength + 2)
        row4 += str(solution).rjust(numberLength+2)

        # Space between problems
        if i < len(problems)-1:
            row1 += 4*" "
            row2 += 4*" "
            row3 += 4*" "
            row4 += 4*" "

    solvedProblems = row1 + "\n" + row2 + "\n" + row3
    if solutions:
        solvedProblems += "\n" + row4

    return solvedProblems


print(arithmetic_arranger(["32 - 698", "3801 - 2", "45 + 43", "123 + 49","1245 + 9875"], True))
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "5+5", "8+8"], True))
print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"], True))