'''
Chapter 4: Variables Notes

Variable is a labeled place in the computer memory that you can use to store a value in.
You must assign it a value using =
Constants are values assigned to a variable that doesnt change after the first assignment. Usually written in all capital letters.

'''

# Example of *more readable* code
def total():
    SERVICE_CHARGE = 1.15
    CENTS = 100
    total = 24.95
    final_total = int( CENTS * total * SERVICE_CHARGE ) / CENTS
    print( final_total )


# --------------------------------------------------------------------------------------------------
# Exercise 4.1:
# Define three variables var1, var2 and var3. Calculate the average of these
# variables and assign it to average. Print the average. Add three comments

def e_0401():
    var1 = 1
    var2 = 2
    var3 = 3
    avg = (var1+var2+var3)
    print(avg)

# --------------------------------------------------------------------------------------------------
# Exercise 4.2:
# Write code that can compute the surface of circle, using the variables radius
# and pi = 3.14159. The formula, in case you do not know, is radius times radius times pi.
# Print the outcome of your program as follows: “The surface area of a circle with radius ...
# is ...”

def e_0402():
    radius = 3
    pi = 3.14159
    surface_of_circle = (radius**radius) * pi
    print('The surface area of a cricle with radius is ' + str(surface_of_circle))

e_0402()
# --------------------------------------------------------------------------------------------------
# Exercise 4.3:
def e_0403():
    pass
# --------------------------------------------------------------------------------------------------
# Exercise 4.4:
def e_0404():
    pass
# --------------------------------------------------------------------------------------------------
# Exercise 4.5:
def e_0405():
    pass
