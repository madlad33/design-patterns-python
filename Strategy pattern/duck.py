class Duck:
    def quack(self):
        print('quack')

    def display(self):
        print('Normal looking duck!')

    def fly(self):
        print('Duck go WEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')


class WildDuck(Duck):
    def quack(self):
        print('quack quack')

    def display(self):
        print('Kinda handsome duck')

    def fly(self):
        print('I can fly higheeeeeeeeeeerrrrrrr')


class CityDuck(Duck):
    def quack(self):
        print('quack quack quack')

    def display(self):
        print('Well behaved duck')

    def fly(self):
        print('I can fly, but not as high as wild :(')


class RubberDuck(Duck):
    def quack(self):
        print('Recorded sound goes quack quack')

    def display(self):
        print('I am artificial duck')

    def fly(self):
        print("I'm not a natural flyer but I can fly a bit")


class PlasticDuck(Duck):
    """
    Here as we have duplicated code for rubber and plastic ducks. We need to reuse this code
    w/o using multiple inheritance as it can lead to messy code.
    Inheritance is good for hierarchical but not for horizontal sharing b/w classes.
    """

    def quack(self):
        print('Recorded sound go brrrrrrrrrrr"')

    def display(self):
        print("I'm an artificial duck")

    def fly(self):
        print("I'm not a natural flyer but I can fly a bit")
