'''
Chapter 3: Expressions Notes


Three Data Types: strings, ints, floats

(\ Backslash): print('I can\'t stand it')

Expression: cominbation of one or two more values (such as strings, ints, or floats)
using operators, which will give us a new value. Think of it like calculations.
+ , - , * , / , // (integer division) , ** (power) , % (mod)

Typecasting: change the data type of a value to a different value
int(15/4), float(15/4), str(15)

#Examples
print( 15+4 ) # 19
print( 15-4 ) # 11
print( 15*4 ) # 60
print( 15/4 ) # 3.75
print( 15//4 ) # 3
print( 15**4 ) # 50625
print( 15%4 ) # 3

'''
# --------------------------------------------------------------------------------------------------
# Exercise 3.1:
# The cover price of a book is $24.95, but bookstores get a 40 percent discount.
# Shipping costs $3 for the first copy and 75 cents for each additional copy. Calculate the total
# wholesale costs for 60 copies

def e_0301():
    cover_price = 24.95
    discount = cover_price * 0.4

    discount_cost = cover_price - discount
    first_shipping_cost = 3
    additional_shipping_cost = .75
    books = 60

    total = (first_shipping_cost + (discount_cost*books) + ((books - 1) * additional_shipping_cost))

    print(total)

# --------------------------------------------------------------------------------------------------
# Exercise 3.2:
# Can you identify and explain the errors in the following lines of code?
# Correct them:              print( "A message" ).
#                            print( "A message ' )
#                            print( ' A messagef" ' )

def e_0302():
    print("A message")
    print('A message')
    print('A messagef')

# --------------------------------------------------------------------------------------------------
# Exercise 3.3:
# When something is wrong with your code, Python will raise errors. Often
# these will be “syntax errors” that signal that something is wrong with the form of your
# code (e.g., the code in the previous exercise raised a SyntaxError). There are also “runtime
# errors,” which signal that your code was in itself formally correct, but that something went
# wrong during the code’s execution. A good example is the ZeroDivisionError, which indicates that you tried to divide a number by zero (which, as you may know, is not allowed).
# Try to make Python raise such a ZeroDivisionError.

def e_0303():
    print(5/0)

# --------------------------------------------------------------------------------------------------
# Exercise 3.4:
# Here is another illustrative example of a runtime error. Run the follow code
# and study the error that it generates. Can you locate the problem?
#               print( ((2*3) /4 + (5 -6/7) *8 )
#               print( ((12*13) /14 + (15 -16) /17) *18 )

'''
First one: missing parenthesis
Second one: this one is okay
'''

# --------------------------------------------------------------------------------------------------
# Exercise 3.5:
# You look at the clock and see that it is currently 14.00h. You set an alarm to
# go off 535 hours later. At what time will the alarm go off? Write a program that prints the
# answer. Hint: for the best solution, you will need the modulo operator.


def e_0305():
    clock = 1400
    alarm = 535
    print(clock + alarm)

    # author's solution: print( str( (14 + 535) % 24 ) + ".00" )
    # Side note: not sure how this is 21.00, that means it's 9pm. If 1400 is 2pm and you set and alarm for 535hours later, wouldn't it be 735pm??
    # Unclear and will leave my current function above as is.
