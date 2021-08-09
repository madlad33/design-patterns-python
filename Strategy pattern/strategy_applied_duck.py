from abc import ABC, abstractmethod


class DuckQuackBehaviour(ABC):
    @abstractmethod
    def quack(self):
        print('quack quack')


class SimpleQuack(DuckQuackBehaviour):
    def quack(self):
        print('quack')


class NoQuack(DuckQuackBehaviour):
    def quack(self):
        print('q....')


class DisplayBehaviour(ABC):
    @abstractmethod
    def display(self):
        pass


class SimpleDisplay(DisplayBehaviour):
    def display(self):
        print('Simple looking duck')


class HandsomeDuck(DisplayBehaviour):
    def display(self):
        print('Handsome duck!')


class FlyBehaviour(ABC):
    @abstractmethod
    def fly(self):
        print('I believe you can fly!')


class HighFly(FlyBehaviour):
    def fly(self):
        print('I believe I can fly higher!')


class ArtificialFly(FlyBehaviour):
    def fly(self):
        print('I believe I can lift myself above ground for a sec...')


class Duck:
    def __init__(self, quack_behaviour: DuckQuackBehaviour, fly_behaviour: FlyBehaviour,
                 display_behaviour: DisplayBehaviour):
        """ Injecting dependencies and creating different strategy for different functions which can be reused"""
        self.quack_behaviour = quack_behaviour
        self.fly_behaviour = fly_behaviour
        self.display_behaviour = display_behaviour

    def quack(self):
        self.quack_behaviour.quack()

    def display(self):
        self.display_behaviour.display()

    def fly(self):
        self.fly_behaviour.fly()


wild_duck = Duck(SimpleQuack(), HighFly(), HandsomeDuck())
wild_duck.quack(), wild_duck.fly(), wild_duck.display()

plastic_duck = Duck(NoQuack(), ArtificialFly(), SimpleDisplay())
plastic_duck.quack(), plastic_duck.fly(), plastic_duck.display()
