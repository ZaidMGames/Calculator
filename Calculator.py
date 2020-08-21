import math
import sys

score: int = 0  # used to keep score for quiz start from 0.

name = ''
Username = ''
Password = ''
PasswordCheck = ''

"""Account creation and program restart"""


# Creating an Account For The First Time
def Account():
    global Password
    global choice
    global name
    global Username
    name = input("Welcome, My name is Noob, What's yours :D?")
    print('')
    print("Hi " + str(name) + ". So because you just started the program, I need you to create an account")
    print('')
    print("Press Enter to create a username and Password")
    Username = ''  # So they press Enter
    Username = input("Please Enter Your Username ")
    print('')
    Password = input("Now Create a password that is at least 6 characters long")


# Once program has been restarted
def Restart():
    global PasswordCheck
    print('So now that you have decided to restart the program, if you are ' + name + ' Then write your Username')
    print('')
    print('Else, if you are a new user, Please enter \'New\'')
    UsernameCheck = input()
    PasswordCheck = ''
    while UsernameCheck != 'New' or Username:
        if UsernameCheck == Username:
            print('')
            PasswordCheck = input('Please Enter Your Password so we can make sure it\'s you')
            break
        if UsernameCheck == 'New':
            print('')
            Account()
            break
        elif UsernameCheck != Username:
            print('That  is not one of the options, please try again.')
            print('')
            UsernameCheck = input()
    while PasswordCheck != Password:
        if PasswordCheck == Password:
            continue
        else:
            print('That was not the correct Password')
            sys.exit()


"""ANYTHING TO DO WITH THE CALCULATOR IS BELOW"""


# If the user chose maths, they have a few selections as to what exactly they will be doing
def Maths():
    print('')
    mathchoice = input("""You chose Calculator :D
    
Enter 'Calculator' to add, subtract, multiply, divide and more between two numbers
    Enter 'pi' to multiply or divide a number by pi
        Enter ' SQRT' to find the square root of a number 
        
             """)  # Asks whether the user wants to calculate, use pi or square root
    while mathchoice.lower()!= 'calculator' or 'pi' or 'sqrt':
        if mathchoice.lower() == 'calculator':
            print(Calculator())
            break
        if mathchoice.lower() == 'pi':
            print(pi())
            break
        if mathchoice.lower() == 'sqrt':
            print(SquareRoot())
            break
        else:
            print('That  is not one of the options, please try again')
            mathchoice = input()


# The Calculator coded below:
def Calculator():
    # The variables for the input that will be asked to the user
    num1 = float(input('Enter your first Number: '))
    operator = str(input("""Enter your operator of choice:
    
                                +  (For addition)
                                -  (For subtraction)
                                x  (Multiplication)
                                / (For Division)
        //  (Floor division or Quotient or in simple words -Gives the integer division without decimal or remainder)
                                %  (well, for the remainder of a division)
                                **  (Will multiply your first number to the power of your second number)

                                Please NOTE THAT THIS IS CAP SENSITIVE!!!!

                                Enter Your Operator of Choice Here: 
                                """))

    # Functions that contribute to whichever operator is chosen by the user
    def add():
        result = num1 + num2
        return ' Your answer is ' + str(result)

    def sub():
        result = num1 - num2
        return 'Your Answer is ' + str(result)

    def divide():
        result = num1 / num2
        return ' Your answer is ' + str(result)

    def multiply():
        result = num1 * num2
        return ' Your answer is ' + str(result)

    def floor():
        result = num1 // num2
        return ' Your answer is ' + str(result)

    def remainder():
        result = num1 % num2
        return ' Your answer is ' + str(result)

    def power():
        result = num1 ** num2
        return ' Your answer is ' + str(result)

    # The Calculation process
    while operator != '+' or '-' or '/' or 'x' or '//' or '%' or '**':
        if operator == '+':
            num2 = float(input('Enter your second number: '))
            return add()  # prints out the result of doing num1 + num2
        elif operator == '-':
            num2 = float(input('Enter your second number: '))
            return sub()  # prints out the result of doing num1 - num2
        elif operator == '/':
            num2 = float(input('Enter your second number: '))
            return divide()  # prints out the result of doing num1 / num2
        elif operator == 'x':
            num2 = float(input('Enter your second number: '))
            return multiply()  # prints out the result of doing num1 * num2
        elif operator == '//':
            num2 = float(input('Enter your second number: '))
            return floor()  # prints out the result of doing num1 // num2
        elif operator == '%':
            num2 = float(input('Enter your second number: '))
            return remainder()  # prints out the result of doing num 1 % num 2
        elif operator == '**':
            num2 = float(input('Enter your second number: '))
            return power()  # Prints out the result of doing num 1 to the power of num 2
        else:
            print('That  is not one of the options, please try again.')
            operator = input()


# The Square Rooter coded below:
def SquareRoot():
    num = input("Enter the number you would like to be square rooted")
    return math.sqrt(float(num))


# Pi coded below:
def pi():
    number = input("Enter the number that will be multiplied or divided by the constant pi (3.14....) ")
    PI = math.pi

    while number == '0':
        if number == '0':
            print('')
            print('You can\'t choose the number 0, so try again')
            print('')
            number = input("Enter the number that will be multiplied or divided by the constant pi (3.14....) ")
            print('')
        if number != '0':
            print('')
            break
    operator = input("""Enter '/' (to divide by pi)
    Enter 'x'  (to Multiply by pi)""")
    if operator == '/':
        print(PI / float(number))
    if operator == 'x':
        print(PI * float(number))


""" All Other Functions needed for full program"""


# If the user chose quiz, the  quiz begins
def Quiz():
    global score
    ans = 'The Answer for This Question was '
    # These are the Answers
    a1 = "sam"
    a2 = "age"
    a3 = "queue"
    a4 = "piano"
    a5 = "light"
    a6 = "TV"

    def checker(guess, answer):
        global score
        if guess.lower() == answer.lower():
            score = score + 1
            print("Correct Answer! Well done.:D" + "\n")
            print("Your score is now " + str(score))
        else:
            print("Incorrect Answer! :(")
            print("")

    # The title of the program
    print("")
    print("Mini Quiz")
    print("=========")
    print("All the questions are answered in one word so answer with one word otherwise it won't be correct :D")
    print("")

    # Question 1
    q1 = input("1.Sam’s mother has five children. March, April, May, June – what is the name of the fifth daughter?  ")
    print("")
    checker(q1, a1)

    # Question 2
    q2 = input("2.What goes up but never comes down?      ")
    print("")
    checker(q2, a2)

    # Question 3
    q3 = input("3.What word is pronounced the same if you take away four of its five letters?      ")
    print("")
    checker(q3, a3)

    # Question 4
    q4 = input("4. What has many keys but can’t open a single lock?     ")
    print("")
    checker(q4, a4)

    # Question 5
    q5 = input("5. What can fill a room but takes up no space?      ")
    print("")
    checker(q5, a5)

    # Question 6
    q6 = input("6. You stare at me but I don’t blush, you switch me off when you’re in a rush. ")
    print("")
    checker(q6, a6)

    # End of mini quiz
    if score == 6:
        print("")
        print("You scored " + str(score) + " out of 6")
        print("Full marks amazing")
    else:
        print("You scored " + str(score))
        print("Nice try!")
        print("The correct answers are:")
        print('For Question 1, ' + ans + a1)
        print('For Question 2, ' + ans + a2)
        print('For Question 3, ' + ans + a3)
        print('For Question 4, ' + ans + a4)
        print('For Question 5, ' + ans + a5)
        print('For Question 6, ' + ans + a6)


"""CALLING ALL FUNCTION HERE TO ACTUALLY EXECUTE THE CODE"""
# Account creation
Account()

while len(Password) < 6:
    print("That Password is smaller than 6 characters, please Retry: ")
    print('')
    Password = input()

# The beginning of the program, asks what the user wants to use the program to do
print('')
choice = input("""What would you like to use the program to do?

                Enter 'Maths' for a calculator
                Enter ' Quiz' for a  quiz
""")
while choice.lower() != 'maths' or 'quiz':
    if choice.lower() == 'maths':
        print(Maths())
        break
    if choice.lower() == 'quiz':
        print(Quiz())
        break
    else:
        print('That  is not one of the options, please try again. You can choose between \'Maths\' or \'Quiz\'')
        choice = input()

# Asking the user whether to restart the program or to end it
print('You have Reached The End Of The Program')
print('')
Choice2 = input("""If you would like to Restart the program, enter 'Restart'
if not, Enter 'Bye' to end the program with a goodbye message :D""")

while Choice2.lower() != 'restart' or 'bye':
    if Choice2 == 'restart':
        print('')
        print('The Program is Restarting............')
        Restart()
        choice = input("""What would you like to use the program to do?
        
                            Enter 'Maths' for a calculator
                            Enter ' Quiz' for a  quiz
                            
                            (PLEASE ENTER WHAT IS INSIDE THE SPEECH MARKS WITHOUT INCLUDING THE SPEECH MARKS)""")
        while choice.lower() != 'maths' or 'quiz':
            if choice.lower() == 'maths':
                print(Maths())
                break
            if choice.lower() == 'quiz':
                print(Quiz())
                break
            else:
                print('That  is not one of the options, please try again. You can choose between \'Maths\' or \'Quiz\'')
                choice = input()
        break
    if Choice2.lower() == 'bye':
        print('')
        print('Thank you for using this program and I hope you have a lovely day :D')
        break
    else:
        sys.exit()
