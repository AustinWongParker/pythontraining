'''
Practice with Python using 'praticepython.org'
Solutions either my own, combination, or taken from site.

For learning purposes only.

Austin Wong-Parker
7/24/19

---------------------
Exercise 1: Character Input
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
(Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines.
(Hint: the string "\n is the same as pressing the ENTER button)

'''


name = input("Please enter your name.\n")
age = int(input("Please enter your age.\n"))
oneHundred = 100 - age
current_year = 2019

oneHundred = print("You will be 100 years old in {} .\n", oneHundred, current_year)

#+ str(oneHundred + current_year) + ".\n")

# Extras:
repeat = int(input('How many times would you like the message to repeat?\n'))
print(oneHundred * repeat)
