'''
Practice using Inheritance in Python

Austin Wong-Parker

6 - 26 - 19

** All code is written by me for PRACTICE only **
'''

class businessMember: "This represents any person in the person"
    def __init__(self, name, age, salary, title):
        self.name = name
        self.age = age
        self.salary = salary
        self.title = title

    def describe(self):
        print("My name is {}, I'm {}, and I make {}".format(self.name, self.age, self.salary), end=" ")

class CEO(businessMember): "This represents the CEO of the business; he inherited businessMember traits"
    def __init__(self, name, age, salary, skills):
        businessMember.__init__(self, name, age, salary)
        self.skills = skills

    def what_skill(self):
        businessMember.describe(self)
        print("I am a Master at {}".format(self.skills))

# Creating Objects
Bob = CEO('Bob', '56' '$500,000', 'Cutting Hair')

# Print blank line
print()
businessMember.describe()
CEO.what_skill()
