# Implement a function that will flatten and sort an array of integers in ascending order, 
# and which adheres to a functional programming paradigm

def flatten_and_sort(num_list):
    flat_list = []
    for num in num_list:
        for i in num:
            flat_list.append(i)
    return sorted(flat_list)

# print(flatten_and_sort([[3, 2, 1], [4, 5, 6]]))

# how does this solution ensure data immutability?
# it adds the flattened and sorted list to a new list, which doesn't change the original list

# is this solution a pure function? Yes. why? because it does not produce side effects or
# change the original list

# is this solution a higher-order function? I think so, because it is returning a function sorted()

# would it have been easier to solve this problem using a different programming style?
# no, because this is the simplest way to solve this problem

# Why in particular is functional programming a helpful paradigm when solving this problem?
# because it is pure and simple and straightforward.

class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired"

class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def boost(self):
        self.max_speed *=2

class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def flame_jet(self, other):
        other.condition = "trashed"

pod = Podracer(200, "poor", 20000)
pod.repair()
print(pod.condition)

new_pod = AnakinsPod(2, "good", 30000)
new_pod.boost()
print(new_pod.max_speed)

third_pod = SebulbasPod(100, "fair", 10000)
third_pod.flame_jet(third_pod)
print(third_pod.condition)

# Once an Object Oriented solution has been implemented, answer the following questions:
# How does this solution demonstrate the four pillars of OOP? 
# (It may not demonstrate all of them, describe only those that apply)
# Encapsulation
# Abstraction
# Inheritance
# Polymorphism

# This solution demonstrates Encapsulation with the attributes from Podracer being hidden from other classes,
# but accessible through methods in each class. It also demonstrates Inheritance by allowing 
# AnakinsPod and SebulbasPod to reuse attributes of the Podracer class. It demonstrated Polymorphism
# by adding the boost and flame_jet functions to each of the other classes so that they had unique functionality
# in addition to things they shared with the Podracer class.

# Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
# I don't think it would have been easier. This seems like the most organized way to break down
# the code into reusable pieces.

# How in particular did Object Oriented Programming assist in the solving of this problem?
# OOP provided a way to group the data into classes which allowed inheritance and polymorphism
# by creating the Podracer class with common attributes and extending them to the other classes,
# which each had their own additional functions.