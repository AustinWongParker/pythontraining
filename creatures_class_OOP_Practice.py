'''
Animal Class
OOP Practice in Python

Austin Wong-Parker

6 - 11 - 19

** All code is written by me for PRACTICE only **
'''

class Creatures:

    # Class Attributes
    location = 'Minnesota' # All of the following creatures can be found in Minnesota (just an example of class attributes)

    # Initializer
    def __init__ (self, name, color, num_of_legs):
        self.name = name
        self.color = color
        self.legs = num_of_legs

    def leap(self):
        print('The ' + self.name + ' leaped')

    def dance(self):
        print('The ' + self.name +' is now dancing!')

    def species(self):
        species = input(print('What kind of species are you?\nMammal, Vertebrate, Insect, Reptile, or other?\n'))
        species.capitalize()
        if (species.index('M') == 0):
            species = 'Mammal'
            print("Ok. I have you listed as a mammal.")
        elif (species.index('V') == 0):
            species = "Vertebrate"
            print("Ok. I have you listed as a Vertebrate.")
        elif (species.index('I') == 0):
            species = "Insect"
            print("Ok. I have you listed as an Insect.")
        elif (species.index('R') == 0):
            species = "Reptile"
            print("Ok. I have you listed as a Reptile.")
        elif (species.index('O') == 0):
            species = "Other"
            print("Ok. I have you listed as other.")
        else:
            print("Sorry, I don't know what to categorize you as.")

class Mammal(Creatures):
    pass
class Vertebrate(Creatures):
    pass
class Insect(Creatures):
    pass
class Reptile(Creatures):
    pass



'''
Testing
'''

Austin = Mammal("Austin", "tan", 2)
Lizard = Reptile("Lizard", "green", 4)
jeffTheBug = Insect("Jeff", "red", 6)

Austin.species()



#print("The {} is {} and has {} legs".format(Lizard.name, Lizard.color, Lizard.legs))
#print("{} is {} and has {} legs".format(Austin.name, Austin.color, Austin.legs))
#Lizard.leap()
#Austin.dance()
