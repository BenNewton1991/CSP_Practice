#Calculator

#Complete the program below. 
#Should be able to add, subtract, divide, multiply numbers. 


def interface():
    exit = input('would you like to exit the program? [y/n]')

    while exit != 'y':
        answer = input('would you like to add, multiply, subtract, or divide numbers? [a/m/s/d]')

        if answer == 'a':  
            first = int(input('first number?'))
            second = int(input('second number?'))
            print(add(first, second))
        elif True:
            multiply()
        else:
            divide()
    
def add(a,b):
    return

def multiply():
    return

def divide():
    return

#need to add a subtract function

interface()