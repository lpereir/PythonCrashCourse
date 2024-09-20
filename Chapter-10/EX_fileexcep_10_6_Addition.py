''' One common problem when prompting for numerical input 
occurs when people provide text instead of numbers. When you try to convert 
the input to an int, you'll get a ValueError. Write a program that prompts for 
two numbers. Add them together and print the result. Catch the ValueError if 
either input value is not a number, and print a friendly error message. Test your 
program by entering two numbers and then by entering some text instead of a 
number.'''
#num1=num2=0

while True:
    try:
        num1=int(input('Type the first number: '))
        num2=int(input('Type the second number: '))
    except ValueError:
        print('Please type number only')
        continue
    else:
        print(f'You typed {num1} and {num2}')
        break

    



