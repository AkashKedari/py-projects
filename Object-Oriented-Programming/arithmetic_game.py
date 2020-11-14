# Akash Kedari
# Object Oriented Programming - section 01 - Project


"""
Put everything together and write a program that lets the user practice a series of random addition and subtraction problems. 

Begin by asking the user for a number of problems (only accept positive values) and a size for their numbers (only acceptnumbers between 5 and 10). 

Also prompt them for a single character to be used to generate their patterns
- only accept single character strings (i.e.  ’a’ is OK,but  ’apple’  is  not). 

Then, generate  a  series  of  random  addition  and  subtractionproblems 
- display the numbers to the user with your digital display functions.

Then prompt the user for an answer and check the answer using your check_answer function.  

Your program should also keep track of how many correct questions theuser answered during their game.  
"""

import random
from my_functions import *

while True:
    num_of_problems = int(input("How many problems would you like to attempt?: "))

    if num_of_problems > 0:
        break
    else:
        print("Invalid number, try again...")
        continue

print()
while True:
    user_width = int(input("How wide would you like your numbers to be? (5 - 10): "))

    if (user_width >= 5) and (user_width <=10):
        break
    else:
        print("Invalid, please enter number between 5 and 10")
        continue

print()
while True:
    user_char = input("What character would you like to use for your numbers? ")

    if len(user_char) == 1:
        break
    else:
        print("String too long, try again!")
        continue

print()

user_drill = input("Do you want to activate drill mode?  (yes or no): ")

print()
print("Here we go.....s")


# Variables 
num_problems_left = num_of_problems
ans_correct = 0
ans_wrong = 0

###############################################################################################
# Non drill mode code below 

while num_problems_left > 0 and user_drill == "no":

    # Choose random number1 and number2
    rand_number1 = random.randint(0,9)
    rand_number2 = random.randint(0,9)
    whole_num = 0

    # Choose an operator and set operator variable
    rand_sign = random.randint(1, 4)
    if rand_sign == 1:
        operator = "+"
    elif rand_sign == 2:
        operator = "-"
    elif rand_sign == 3:
        operator = "x"
    else:
        operator = "/"
        # Check cases. 
        # If randnum2 is 0, youll get a divide by zero error. You have to pick a new randnum2.
        # If randnum2 is not zero but the output is not a whole number, you need to change randnum1 and randnum2
        # I am changing both because it will always be 1 if I matched randnum2 to whatever randnum1 is.
        if rand_number2 == 0:
            rand_number2 = random.randint(1,9)

        if (rand_number2 != 0) and (rand_number1%rand_number2 != 0):

            while True:
                rand_number1 = random.randint(0, 9)
                rand_number2 = random.randint(0, 9)

                if (rand_number1%rand_number2 == whole_num):
                    break
                else: 
                    continue


    # print outputs ...Get numbers to show on user interface.
    # Print the first number
    print("What is...")
    print()

    print_number(rand_number1,user_width,user_char)
    print()
    print()

    # Print the operator
    if rand_sign == 1:
        print(plus(user_width, user_char))
    elif rand_sign == 2:
        print(minus(user_width, user_char))
    elif rand_sign == 3:
        print(multiply(user_width, user_char))
    else:
        print(divide(user_width,user_char))
        
    # Print the second number
    print()
    print()
    print_number(rand_number2,user_width,user_char)
    print()
    # Store users answer to check later
    user_answer = int(input("The answer is = "))

    # Check if the answer was correct or not. Keep track of correct/wrong answers.
    if check_answer(rand_number1,rand_number2,user_answer,operator) == True:
        print("Correct!")
        ans_correct += 1
    else:
        print("Incorrect")
        ans_wrong += 1

    num_problems_left -= 1

#################################################################################################################
# Drill mode code below 

# Variables for drill mode
# Extra attempts for type of problem
extra_add= 0
extra_minus =0
extra_multiply = 0
extra_divide = 0

# total number of each respective problem
tot_add = 0
tot_minus = 0
tot_multiply = 0
tot_divide = 0

# total correct problems of each respctive type
add_problem = 0
minus_problem = 0
multiply_problem = 0
divide_problem = 0


while num_problems_left > 0 and user_drill == "yes":
    # Choose random number1 and number2
    rand_number1 = random.randint(0, 9)
    rand_number2 = random.randint(0, 9)
    whole_num = 0

    # Choose an operator and set operator variable
    # Also keep track of which type of problem it is and its frequency
    rand_sign = random.randint(1, 4)
    if rand_sign == 1:
        operator = "+"
        tot_add +=1 
    elif rand_sign == 2:
        operator = "-"
        tot_minus+=1
    elif rand_sign == 3:
        operator = "x"
        tot_multiply+=1
    else:
        operator = "/"
        tot_divide +=1
        # Check cases.
        # If randnum2 is 0, youll get a divide by zero error. You have to pick a new randnum2.
        # If randnum2 is not zero but the output is not a whole number, you need to change randnum1 and randnum2
        # I am changing both because it will always be 1 if I matched randnum2 to whatever randnum1 is.
        if rand_number2 == 0:
            rand_number2 = random.randint(1, 9)

        if (rand_number2 != 0) and (rand_number1 % rand_number2 != 0):

            while True:
                rand_number1 = random.randint(0, 9)
                rand_number2 = random.randint(1, 9)

                if (rand_number1 % rand_number2 == whole_num):
                    break
                else:
                    continue

    # print outputs ...Get numbers to show on user interface.
    # Print the first number
    print("What is...")
    print()

    print_number(rand_number1, user_width, user_char)
    print()
    print()

    # Print the operator
    if rand_sign == 1:
        print(plus(user_width, user_char))
    elif rand_sign == 2:
        print(minus(user_width, user_char))
    elif rand_sign == 3:
        print(multiply(user_width, user_char))
    else:
        print(divide(user_width, user_char))

    # Print the second number
    print()
    print()
    print_number(rand_number2, user_width, user_char)
    print()
    # Store users answer to check later but also 
    # keep inputting answer until user gets it correct. 
    # Keep track of those extra attempts for each type.
    while True:
        user_answer = int(input("The answer is = "))

        if check_answer(rand_number1,rand_number2,user_answer,operator) == True:
            print("Correct!")

            # Keep track of which type of problem was correct. 
            # Only increment if it was correct on the first attempt. 
            if operator =="+" and extra_add == 0:
                add_problem +=1
            elif operator =="-" and extra_minus == 0:
                minus_problem +=1 
            elif operator =="x" and extra_multiply == 0:
                multiply_problem+=1
            elif operator=="/" and extra_divide == 0:
                divide_problem +=1

            break
        else:
            # keep track of wrong answers attempts for each type. 
            print("Incorrect, try again!")
            if operator == "+":
                extra_add +=1
            elif operator == "-":
                extra_minus +=1
            elif operator == "x":
                extra_multiply += 1
            elif operator == "/":
                extra_divide += 1

            continue

    # Decrement the remaining problems left
    num_problems_left -=1



# Output final stats/results 

if user_drill == "no":
    print()
    print("You got "+ str(ans_correct)+ " out of "+str(num_of_problems) +" correct!")


if user_drill =="yes":
    print()
    if tot_add == 0:
        print("No addition problems presented")
    if tot_minus == 0:
        print("No subtraction problems presented")
    if tot_multiply == 0:
        print("No multiplication problems presented")
    if tot_divide == 0:
        print("No division problems presented")


    if tot_add > 0:

        percent_add = (add_problem/tot_add)*100
        print()
        print("Total addition problems:", tot_add)
        print("Correct addition problems:", add_problem, percent_add)

        if extra_add == 0:
            print("Number of extra attempts:",extra_add, " (Perfect!)")
        else:
            print("Number of extra attempts:", extra_add)

    if tot_minus > 0:

        percent_minus = (minus_problem/tot_minus)*100
        print()

        print("Total subtraction problems:", tot_minus)
        print("Correct subtraction problems:", minus_problem)

        if extra_minus == 0:
            print("Number of extra attempts:", extra_minus, " (Perfect!)")
        else:
            print("Number of extra attempts:", extra_minus)

    if tot_multiply > 0:

        percent_multiply = (multiply_problem/tot_multiply)*100
        print()

        print("Total multiplication problems:", tot_multiply)
        print("Correct addition problems:", multiply_problem)

        if extra_multiply == 0:
            print("Number of extra attempts:", extra_multiply, " (Perfect!)")
        else:
            print("Number of extra attempts:", extra_multiply)

    if tot_divide > 0:

        percent_divide = (divide_problem/tot_divide)*100
        print()

        print("Total division problems:", tot_divide)
        print("Correct division problems:", divide_problem, percent_divide)

        if extra_add == 0:
            print("Number of extra attempts:", extra_divide, " (Perfect!)")
        else:
            print("Number of extra attempts:", extra_divide)

