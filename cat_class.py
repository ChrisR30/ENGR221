"""
File: cat_class.py
Description: Implementation of a cat
"""

class Cat:
    def __init__(self, name, color, age, fur_length):
        self.name = name #name of the cat
        self.color = color #color of the cat
        self.age = age #age of the cat
        self.fur_length = fur_length #fur length of the cat

        ####
        # Data Methods
        ####

    def attack(self):
     # Attack
        print("Attack!")
        
    def defend(self):
            # Defend
        print("Defending!")

    def meow(self):
            # Meow
        print("Meow")

    def excrete(self):
            # Excrete
        print("Excreting")

    def purr(self):
        #purr
        print("Purr")

if __name__ == '__main__':
    tom = Cat("Tom", "gray", 84, "Short")
    print(tom.age) # Print Tom's age
    #tom.attack("Scratch")

    hello_kitty = Cat("Hello Kitty", "white", 40, "Short")
    print(hello_kitty.age)
    hello_kitty.age = 58
    print(hello_kitty.age)
    print(tom.age)
                  