"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

def calculator2():
    while True:
        user_input = input("Enter your equation: ")
        tokens = user_input.split(' ')
        
        # lines 12-16: attempted to produce a message if a word was inputted instead of a number
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        for x in range(25):
            if tokens[1].index(alphabet(x)) == True:
                print("Use integers please!! >:(")

        
        if tokens[0] != ("+" or "-" or "*" or "/" or "square" or "cube" or "pow" or "mod"):
            print("Use one of the allowed operators!")


        if tokens[0] == "+":
            num1 = int(tokens[1])
            num2 = int(tokens[2])
            print(add(num1, num2))

        if tokens[0] == "-":
            num1 = int(tokens[1])
            num2 = int(tokens[2])
            print(subtract(num1, num2))

        if tokens[0] == "*":
            num1 = int(tokens[1])
            num2 = int(tokens[2])
            print(multiply(num1, num2))

        if tokens[0] == "/":
            num1 = int(tokens[1])
            num2 = int(tokens[2])
            print(divide(num1, num2))

        if tokens[0] == "square":
            num1 = int(tokens[1])
            print(square(num1))

        if tokens[0] == "cube":
            num1 = int(tokens[1])   
            print(cube(num1))
        
        if tokens[0] == "pow":
            num1 = int(tokens[1])
            num2 = int(tokens[2])   
            print(power(num1, num2))
        
        if tokens[0] == "mod":
            num1 = int(tokens[1])
            num2 = int(tokens[2])   
            print(mod(num1, num2))
        
        if tokens[0] == "q":
            break
            

calculator2()
