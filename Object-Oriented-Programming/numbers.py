# Akash Kedari - OOP Seciton 01 

# All functions take in a number int
# returns a boolean value 


# Funciton is_even
def is_even(number):
    if number%2 == 0:
        return True

# Function is_odd
def is_odd(number):
    if number%2 != 0:
        return True

# function is_prime 
def is_prime(number):

    counter = 0
    for x in range (1, number+1):
        if number % x == 0:
            counter += 1

        if counter ==2:
            result = True
        else:
            result = False

    return result 

# function is_prime_range
def is_prime_range(num1 , num2):

    prime_nums = str()
    counter = 0 

    for x in range(num1, num2):
        num_factors = 0
        for pot_factor in range (1,x+1):
            if x % pot_factor == 0:
                num_factors +=1 

        if num_factors ==2:
            counter +=1 
            prime_nums += str(x) + '\n'

    return prime_nums


# function is_perfect
def is_perfect(number):
    sum_perfect = 0

    for x in range (1, number+1):
        if number % x == 0:
            sum_perfect += x

    sum_perfect = sum_perfect - number

    if number == sum_perfect:
        return True
    else: 
        return False

# function is_abundant
def is_abundant(number):
    sum_abundant = 0

    for x in range (1, number+1):
        if number % x == 0:
            sum_abundant += x

    sum_abundant = sum_abundant - number

    if number < sum_abundant:
        return True
    else: 
        return False



'''
Next,  write a program  that prompts the  allows  the user to  analyze numbers within 

a given range for numbers that fit the above criteria.  

The program should continueto execute as long as the user wishes to keep going. 
'''

while True:
    print("1 - Find all prime numbers within a given range.")

    print("2 - Find all perfect numbers within a given range.")

    print("3 - Find all abundant numbers within a given range.")

    print("4 - Chart all even, odd, prime, perfect ,and abundant numbers within a given range.")

    print("5 - Quit")

    user_choice = int(input("Please choose from the main menu: "))

    if user_choice == 1:
        while True:
            start_num = int(input("Enter starting number: "))

            if start_num <= 0:
                print("Enter valid value please")
                continue
            else: 
                break

        while True:
            ending_num = int(input("Enter ending number: "))

            if ending_num <= 0:
                print("Enter valid value please")
                continue
            else:
                break

        # Code to find all prime numbers below 
        print("All prime numbers between", start_num,"and",ending_num)
        print(is_prime_range(start_num,ending_num+1))
        
    if user_choice == 2:
        while True:
            start_num = int(input("Enter starting number: "))

            if start_num <= 0:
                print("Enter valid value please")
                continue
            else:
                break

        while True:
            ending_num = int(input("Enter ending number: "))

            if ending_num <= 0:
                print("Enter valid value please")
                continue
            else:
                break

        # Code to find all perfect numbers below
        # for this code I figured out that I can iterate from the start to the end value
        # and check each number if it is perfect, and if it is, I can output that number
        for i in range(start_num,ending_num+1):
            if is_perfect(i):
                print(i)

    if user_choice == 3:
        while True:
            start_num = int(input("Enter starting number: "))

            if start_num <= 0:
                print("Enter valid value please")
                continue
            else:
                break

        while True:
            ending_num = int(input("Enter ending number: "))

            if ending_num <= 0:
                print("Enter valid value please")
                continue
            else:
                break

        # code to find all abundant numbers in give range. 
        # I can use the same logic from above: 
        # iterate through the range and check if each number is abundant and then print
        for i in range(start_num,ending_num+1):
            if is_abundant(i):
                print(i)

    if user_choice == 4:
        while True:
            start_num = int(input("Enter starting number: "))

            if start_num <= 0:
                print("Enter valid value please")
                continue
            else:
                break

        while True:
            ending_num = int(input("Enter ending number: "))

            if ending_num <= 0:
                print("Enter valid value please")
                continue
            else:
                break

        # Code to chart all the even, odd, prime, perfect, and abundant.
        
        space = " "
        print("Number", space*5, "Even", space*5, "Odd", space*5, "Prime", space*5, "Perfect", space*5, "Abundant")

        # Check even
        for x in range(start_num,ending_num+1):

            numbers = str(x)
            even_sign = str()
            odd_sign = str()
            prime_sign = str()
            perfect_sign = str()
            abundant_sign = str()

            if is_even(x):
                #even_sign += numbers + space*10+"X"
                #print(even_sign)
                even_sign +="X"

            if is_odd(x):
                #odd_sign +=numbers + space*21+"X"
                #print(odd_sign)
                odd_sign += "X"
            if is_prime(x):
                #prime_sign += space*35+"X"
                #print(prime_sign)
                prime_sign += "X"
            if is_perfect(x):
                #perfect_sign += space*47+ "X"
                #print(perfect_sign)
                perfect_sign += "X"
            if is_abundant(x):
                #abundant_sign += space*65 + "X"
                #print(abundant_sign)
                abundant_sign += "X"

            # I googled a few formatting outputs for tables in python. 
            # The formatting is all on one line and the "X" marks corrospond for each number

            print ('%-13s %-10s %-13s %-13s %-13s %-12s' % (numbers, even_sign,odd_sign,prime_sign,perfect_sign,abundant_sign))


    if user_choice == 5:
        print("Quit")
        break



