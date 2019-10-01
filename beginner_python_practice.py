'''
Austin Wong-Parker

6 - 11 - 19

** All code is written by me for PRACTICE only **

*** Code in some areas are NOT correct - written by others ***
'''

'''
a = 5
b = 10
c = "150"

Execute: (a+b) + C
Expected output: 165

print((a+b) + int(c))

--------------------------------

# Rain will fall if it's 0; Rain will not fall if it's anything but 0. Check if it's raining or not. You get a user input

# Variables
user_input = int(input("Will it rain? [Please enter 0 or any number]\n"))


x = 0

def hello_world(x):
    if (user_input == x):
        return "It will rain."
    else:
        return "It will not rain"
        # code for the if statement in here

x = int(input("What number do you choose\n"))
while(x != 10):
    print("X is not 10, you lose. You guess " + str(x))
    break

if (x == 10):
    print("Yes, x is 10")
'''


# Coding Challenge 1: Create a function that takes in a user input and checks if it's equal to the word Apple.

'''
def apple():
    user_input = str(input("Please type in Apple\n"))
    example_apple = "Apple"
    if (user_input == "Apple".lower()):
        print("true")
    else:
        print("false")
apple()
'''

# Coding Challenge 2: Have the same function, but if the user enters anything except the word Apple,
#                     they must get another prompt asking them to enter it again.
'''
def apple():
    user_input = str(input("Please type in Apple\n"))
    example_apple = "Apple"
    while (user_input != "Apple"):
        print("Please try again.")
        apple()
    if (user_input == "Apple"):
        print("true")
apple()
'''

'''
def apple():
    user_input = str(input("Please type in Apple\n"))
    example_apple = "Apple"
    if (user_input == "Apple"):
        print("true")
    else:
        print("Please try again.")
apple()

'''





# Coding Challenge 3: Create a function that compares two different user inputs and prints out (on the command line) the greater
#                     of the two.
'''
def sum():
    user_input1 = int(input("Please type a number.\n"))
    user_input2 = int(input("Please type another number.\n"))
    if (user_input1 > user_input2):
        print("The greater number is " + str(user_input1))
    else:
        print("The greater number is " + str(user_input2))
sum()
'''


# Coding Challenge 4: Create a simple calculator function that will take three arguments from the user and do that operation.
#                     For example: ... user will enter their first input: 5
#                                                            second input: ADD
#                                                            third input: 8
#                                                            The output will be 5 + 8 = 13 (I want to see the command prompt say 5 + 8 = 13)
#                     Another example: ... 7 * 4, the output will be '7 * 4 = 28'
#


'''
def calculator():

    user_input5 = int(input("first input:\n"))
    user_input6 = str(input("second input (add, subtract, multiply, or divide):\n"))
    user_input7 = int(input("third input:\n"))
    user_input6.lower()
    if (user_input6 == "add"):
        add_var = (user_input5 + user_input7)
        print(str(add_var) + " = " + str(user_input5) + ' + ' + str(user_input7))
    elif(user_input6 == "subtract"):
        sub_bar = (user_input5 - user_input7)
        print(str(sub_bar) + " = " + str(user_input5) + ' - ' + str(user_input7))
    elif(user_input6 == "multiply"):
        mult_bar = (user_input5 * user_input7)
        print(str(mult_bar) + " = " + str(user_input5) + ' * ' + str(user_input7))
    elif(user_input6 == "divide"):
        div_bar = (user_input5 / user_input7)
        print(str(div_bar) + " = " + str(user_input5) + ' / ' + str(user_input7))
    else:
        print("Sorry, something went wrong!")

calculator()

    def add():
        user_input1 = str(input("second input:\n"))
        if (user_input1 == "add"):
            print(+)

        def subtract():
            user_input2 = str(input("second input:\n"))
            if (user_input2 == "subtract"):
                print(-)

        def multiply():
            user_input3 = str(input("second input:\n"))
            if (user_input3 == "multiply"):
                print(*)

        def divide():
            user_input4 = str(input("second input:\n"))
            if (user_input4 == "divide"):
                print(/)
'''




# Coding Challnge 5: Create a list that contains three variables (that have been passed into the list); A,B,C.
#                    A is 5, B is 8, C is 2. Then, create a function that will take the highest value out of all the Variables
#                    and multiple that value by 10.
'''
def highest_value(a,b,c):
    if (a > b) and (a > c):
        print(a * 10)
    elif (b > a) and (b > c):
        print(b * 10)
    elif (c > a) and (c > b):
        print(c * 10)
highest_value()
'''



# Coding Challenge 6: Create a function that will take in three students' test scores, and you need to convert them into a string. After you Create
                     #the function, print out the highest student scores in order; highest to lowest.
'''
test_scores1 = str(input("Enter in your test score \n"))
test_scores2 = str(input("Enter in your test score \n"))
test_scores3 = str(input("Enter in your test score \n"))

def student_scores():
    if (test_scores1 > test_scores2) and (test_scores1 > test_scores3) and (test_scores2 > test_scores3):
        print(test_scores1, test_scores2, test_scores3)
    elif ()
student_scores()
'''


# Coding Challenge 7: Create a function that takes in one argument. This argument will be the one student's test score.
#                     check if the test score is lower than 70. if it is, print FAILED. If not, ASK the student if they could have done
#                     better. If they can do better, print 'maybe next time'. If they're good, print 'good job'.
'''
student_scores = int(input("Enter your score \n"))


def scores(student_scores):
    if(student_scores < 50):
        print("You've been kicked out of the program.")
    elif(student_scores > 100):
        print("Yeah, no you didn't")
    else:
        while(student_scores < 70):
            print("You failed")
            break

        if(student_scores > 70):
            a = str(input("Do you think you could've done better? yes or no\n"))
            if(a == "yes".lower()):
                print("maybe next time")
            elif(a == "no".lower()):
                print("good job")

scores(student_scores)
'''



# Coding Challenge 8: Create a weather function that will tell the user whether it will be raining, sunny, cloudy, or snowing.
#                     12AM - 8AM will be snowing
#                     8:01 AM - 11:59 AM will be raining
#                     12 PM - 6PM will be sunny
#                     6:01 PM - 11:59 PM will be cloudy
#                     If the user DOES NOT enter in the format __ : __, he will have to try again (hint: you can use while loop).
'''
user_input = int(input("I will tell you the weather. What time is it? Use 24 hour time without the colon"))

def weather():
    if (user_input >= 0)
        print("It is snowing.")
    elif (user_input > 0800) and (user_input <= 1159):
        print ("It is raining.")
    elif (user_input >= 1200) and (user_input <=1800):
        print ("It is sunny.")
    elif (user_input > 1800) and (user_input <= 2359):
        print ("It is cloudy.")
    else:
        print ("Please try again.")

weather():
'''
