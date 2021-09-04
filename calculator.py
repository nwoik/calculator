import re
import time


def main():
    print("***Welcome to David's calculator***\n\nYou can add(+), subtract(-), multiply(* or x) and divide(/)\n\nPress 'E' to exit\n\nDISCLAIMER: THIS CALCULATOR WORKS FROM LEFT TO RIGHT ON A FCFS BASIS\n")
    c = " "
    while c != "e":
        print(c)
        c = calc()
        

def calc():
    operators = ["+", "-", "*", "x", "/"]

    user_input = input("Enter your sum: ") # Get's user input

    if user_input == "": # If the user enters nothing
        print("Error: [NULL ENTRY]\n")
        return calc()

    elif user_input.lower() == "e": # If they press E to exit
        print("Thank you for using my calculator")
        time.sleep(2)
        return "e"

    else:
        user_input = re.sub("\s", "", user_input) # Removes any whitespaces the user might've typed
        

        numbers = re.split("\D", user_input) # Get's all the digits from the string from the string
        operators = re.findall("[+*xX/-]", user_input) # Get's all the non digits
        # print(numbers)
        # print(operators)
        if len(operators) == 0:
            return "Error: [THERE ARE NO OPERATORS]"

        if len(numbers) == 1:
            return "Error: [NOT ENOUGH VARIABLES]"


        numbers = [convert(num) for num in numbers] # Converts all the string number types to int 

        answer = numbers[0] 
        index = 1

        while index < len(numbers):
            if operators[index-1] == "+": # If the operator is + then add
                answer = add(answer, numbers[index])
            elif operators[index-1] == "-": # If it's - then take
                answer = sub(answer, numbers[index])
            elif operators[index-1] == "*" or operators[index-1] == "x": # If it's multiply
                answer = multiply(answer, numbers[index])
            else:
                answer = divide(answer, numbers[index])
            index += 1

       
        return answer

def add(x, y):
    return x+y

def sub(x, y):
    return x-y

def multiply(x, y):
    return x*y

def divide(x, y):
    return x/y

def convert(num):
    num = int(num)
    return num
    
main()