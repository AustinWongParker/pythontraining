'''
Animal Class
OOP Practice in Python

Austin Wong-Parker

6 - 11 - 19

** All code is written by me for PRACTICE only **
'''

class Creatures:

    # Class Attributes / Class Variable
    location = 'Minnesota' # All of the following creatures can be found in Minnesota (just an example of class attributes)

    # Initializer - init method is run as soon as an object is instantiated/created. Known as constructor? Cannot confirm.
    def __init__ (self, name, color, num_of_legs):
        self.name = name # This is an instance variable
        self.color = color
        self.legs = num_of_legs

    def leap(self):
        print(self.name + ' leaped')

    def dance(self):
        print(self.name +' is now dancing!')

'''
** Note about self **

Self represents the instance of the class. We can now access the attributes and methods of the class.

'''

Racoon = Creatures('Sneakers', 'black', 'four') # Racoon object is now instantiated (created) and is now an instance of class Creatures
Racoon.leap()
Racoon.dance()

Turtle = Creatures('Blastoise', 'Blue', 'four')
