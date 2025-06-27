# inherritence concept
"""
class animal:
        def sound(self):
            print ("The sound of the animal is 'ahhhhhhhhhhhhhwooooooooooooooo'")
class dog(animal):
    def eat(self):
        print("All animals eat!")
    #def sound(self):
        #print("The sound of the dog is 'bowbowbowbowbowbowbowbowbowbowbow'")
res = animal()
print()
res = dog()
res.sound()
"""

# polymorphism
'''
class Animal:
    def sound(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def sound(self):
        print("Dog says Woof!")

class Cat(Animal):
    def sound(self):
        print("Cat says Meow!")


a = Animal()
d = Dog()
c = Cat()

a.sound()
d.sound()
c.sound()
'''

'''
# abstraction
from abc import ABC, abstractmethod

class payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class creditcard(payment):
    def pay(self):
        print("payment done using Credit Card")
class upi(payment):
    def pay(self):
        print("pyment done using Upi")
class paypal(payment):
    def pay(self):
        print("payment done using Paypal")
p1 = creditcard()
p2 = upi()
p3 = paypal()

p1.pay()
p2.pay()
p3.pay()


'''





