'''
Python Practice for:
    1. While Loops
    2. For Loops
    3. Nested For Loops
    4. If Statements
    5. etc.
    ------------

    Austin Wong-Parker
    6/5/19

    ** All code is written by me for PRACTICE only **

'''

'''
# This is a list; it acts like an Array in other programming languages
fruit_bowl = ["apple", "banana", "kiwi", "pears", "peaches", 8]


# User guess which position the apple is in
def fruit_bowl_practice():
    user_input = int(input("Is the apple in postion 0, 1, 2, 3? Take a guess. \n"))
    if (user_input == 0):
        print("Yes, the apple is in position " + str(fruit_bowl.index("apple")))
    else:
        print("The apples are not in that position, sorry. Would you like to guess again? [Y/N] \n")
        try_again = str(input()).lower()
        if (try_again[0] == 'y'):
            fruit_bowl_practice()
        else:
            print("Better luck next time!")
fruit_bowl_practice()
'''


'''
This is how other programming languages do FOR loops
for(int i=0; i < 5; i++){
    print(i) # output: 0, 1, 2, 3, 4
}

'''

# This is how Python does it

example_list = ["Austin", "Will", "Bob", "Rob"]
for x in example_list:
    if x == 3:
        print("We found the boy, {}".format("Rob"))
        break
else:
    print("We didn't find the boy")
