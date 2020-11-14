# Akash Kedari
# Object Oriented Programming - section 01 - Project 

def horizontal_line (width , string):
    return(width * string)


def vertical_line(shift,height,string):
    vert_line = str()

    for a in range(height):
        vert_line += " " * shift + string + '\n'

    return vert_line

def two_vertical_lines(width, height, string):
    two_vert = str()

    for a in range(height):
        two_vert += string + " "*width + string + '\n'
        
    return two_vert

# Make numbers using the three above functions. 
# Call abouve function to make shape 
# can assume numbers printed with height = 5
# Each number function takes in width and character
# Width controls the spacing from the left side of the output screen
# Character is just the chosen character
def number_0(width, character):
    pattern = str()
    pattern += horizontal_line(width, character)
    pattern += "\n"
    pattern += two_vertical_lines(width-2,3,character)
    pattern += horizontal_line(width, character)
    return pattern

def number_1(width, character): 
    pattern = vertical_line(width-1, 5, character)
    return pattern

def number_2(width, character):
    # Had to add a new line in-between because the function didnt add a line in for horizontal line
    # I don't wanna add the new line in the horizontal line function so im just gonna hardcode it in. 
    # Subtract 1 from width for vertical line because star takes one space
    # Subtract 2 from two_vertical_lines cause two stars take two spaces
    pattern = str()
    pattern += horizontal_line(width, character)
    pattern += "\n"
    pattern += vertical_line(width-1, 1, character)
    pattern += horizontal_line(width, character)
    pattern += "\n"
    pattern += vertical_line(0, 1, character)
    pattern += horizontal_line(width, character)
    return pattern

def number_3(width, character):
    pattern = str()
    pattern += horizontal_line(width, character)
    pattern += "\n"
    pattern += vertical_line(width-1, 1, character)
    pattern += horizontal_line(width, character)
    pattern += "\n"
    pattern += vertical_line(width-1, 1, character)
    pattern += horizontal_line(width, character)
    return pattern

def number_4(width, character):
    pattern = str()
    pattern += two_vertical_lines(width-2 ,2,character)
    pattern += horizontal_line(width, character)
    pattern += '\n'
    pattern += vertical_line(width-1,1, character)
    pattern += vertical_line(width-1, 1, character)
    return pattern

def number_5(width, character):
    # Opposite of number 2 for the single stars printed Hence, switch the statements for vertical lines. 
    pattern = str()
    pattern += horizontal_line(width, character)
    pattern += "\n"
    pattern += vertical_line(0, 1, character)
    pattern += horizontal_line(width, character)
    pattern += "\n"
    pattern += vertical_line(width-1, 1, character)
    pattern += horizontal_line(width, character)
    return pattern

def number_6(width, character):
    pattern = str()
    pattern += horizontal_line(width, character)
    pattern += "\n"
    pattern += vertical_line(0, 1, character)
    pattern += horizontal_line(width, character)
    pattern += "\n"
    pattern += two_vertical_lines(width-2,1,character)
    pattern += horizontal_line(width, character)
    return pattern

def number_7(width, character):
    pattern = str()
    pattern += horizontal_line(width, character)
    pattern += "\n"
    # goes down 4 times
    pattern += vertical_line(width-1, 4, character)
    return pattern

def number_8(width, character):
    pattern = str()
    pattern += horizontal_line(width, character)
    pattern += "\n"
    pattern += two_vertical_lines(width-2,1,character)
    pattern += horizontal_line(width, character)
    pattern += "\n"
    pattern += two_vertical_lines(width-2, 1, character)
    pattern += horizontal_line(width, character)
    return pattern

def number_9(width,character):
    pattern = str()
    pattern += horizontal_line(width, character)
    pattern += "\n"
    pattern += two_vertical_lines(width-2, 1, character)
    pattern += horizontal_line(width, character)
    pattern += "\n"
    pattern += vertical_line(width-1,2,character)
    return pattern


# Write a function to print a give number. Input should be
# number , width and string value

def print_number(number, width, character):
    
    if number == 0:
        print(number_0(width, character))
    elif number == 1:
        print(number_1(width, character))
    elif number == 2:
        print(number_2(width, character))
    elif number == 3:
        print(number_3(width, character))
    elif number == 4:
        print(number_4(width, character))
    elif number == 5:
        print(number_5(width, character))
    elif number == 6:
        print(number_6(width, character))
    elif number == 7:
        print(number_7(width, character))
    elif number == 8:
        print(number_8(width, character))
    elif number == 9:
        print(number_9(width, character))

# Write a function to simulate plus and minus signs 
# Input is width value, and string character 
# assume the height is 5 

def plus (width, string):
    plus_sign = str()

    # check condition for the doubling up of the sign
    if width%2 == 1:
        space = int(width/2)
        plus_sign += vertical_line(space,2,string)
        plus_sign += horizontal_line(width,string)
        plus_sign += '\n'
        plus_sign += vertical_line(space,2,string)
    else:
        space = int(width/2)-1
        plus_sign += " " * space + two_vertical_lines(0,1,string)
        plus_sign += " " * space + two_vertical_lines(0, 1, string)
        plus_sign += horizontal_line(width, string)
        plus_sign += '\n'
        plus_sign += " " * space + two_vertical_lines(0, 1, string)
        plus_sign += " " * space + two_vertical_lines(0, 1, string)

    return plus_sign

def minus(width, string):
    minus_sign = horizontal_line(width, string)
    return minus_sign


def multiply(width, string):
    space = " "
    multiply_sign = str()
    multiply_sign += 1*space + two_vertical_lines(3,1,string)
    multiply_sign += 2*space + two_vertical_lines(1, 1, string)
    multiply_sign += vertical_line(3,1,string)
    multiply_sign += 2*space + two_vertical_lines(1, 1, string)
    multiply_sign += 1*space + two_vertical_lines(3, 1, string)
    return multiply_sign

def divide (width, string):
    division_sign = str()
    division_sign += vertical_line(2,1,string)
    division_sign += horizontal_line(width,string)
    division_sign += '\n'
    division_sign += vertical_line(2, 1, string)
    return division_sign



# Check answer function takes in number1, number2, user answer, and operator
# return true or false if user answer is correct/not correct
def check_answer(number1, number2, answer, operator):

    if operator == "-":
        correct_answer = number1 - number2
    elif operator == "+":
        correct_answer = number1 + number2
    elif operator == "x":
        correct_answer = number1 * number2
    elif operator == "/":
        correct_answer = number1/number2
    
    if answer == correct_answer:
        return True
    else:
        return False


