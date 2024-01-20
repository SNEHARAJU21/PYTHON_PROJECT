import sys
def collatz_seq(number):
    if number % 2 == 0: # Remainder = 0, Checks for even number
        value = number // 2
    elif number % 2 != 0: # Remainder = 1, Checks for odd number
        value = (number*3)+1
    while value == 1: # If value is 1
        print(value,end=" ") 
        sys.exit() # Program exits
    while value != 1: # The loop runs until the value is not 1.
        print(value,end=" ") 
        number = value # Value of value is copied to number
        return collatz_seq(number) 
print('Enter a number: ') # Input statement
try: 
    numb = int(input())# Typecast as Integer Input
    if numb == 0: 
        print('Number must be an integer not equal to zero.') 
    elif numb < 0: 
        numb = abs(numb) 
        print("A negative number entered") 
        collatz_seq(numb) 
    else: 
        collatz_seq(numb) 
except ValueError: 
    print('You must enter an integer type.')