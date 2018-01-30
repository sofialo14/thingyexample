'''
SI 206 W18 Homework03: Classes and Inheritance

Your discussion section: 005
People you worked with: Orly Abrams

######### DO NOT CHANGE PROVIDED CODE ############
'''

#######################################################################
#---------- Part 1: Class
#######################################################################

'''
Task A
'''
import random
from random import randrange
class Explore_pet:
    boredom_decrement = -4
    hunger_decrement = -4
    boredom_threshold = 6
    hunger_threshold = 10

    def __init__(self, name="Coco"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "I'm " + self.name + '. '
        state += 'I feel ' + self.mood() + '. '
        if self.mood() == 'hungry':
            state += 'Feed me.'
        if self.mood() == 'bored':
            state += 'You can teach me new words.'
        return state


#your code begins here . . .

coco = Explore_pet()
coco.boredom = 8
print(coco)

brian = Explore_pet(name='Brian')
brian.hunger = 11
print(brian)

'''
Task B
'''
#For task B, add your code inside the Pet class
class Pet:
    boredom_decrement = -4
    hunger_decrement = -4
    boredom_threshold = 6
    hunger_threshold = 10

    def __init__(self, name="Coco"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.words = ["hello"]

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "I'm " + self.name + '. '
        state += 'I feel ' + self.mood() + '. '
        if self.mood() == 'hungry':
            state += 'Feed me.'
        if self.mood() == 'bored':
            state += 'You can teach me new words.'
        return state

    def clock_tick(self):
        self.hunger += 2
        self.boredom += 2

    def say(self):
        print("I know how to say:")
        for x in self.words:
            print(x)

    def teach(self, word):
        self.words.append(word)
        if self.boredom < self.boredom_decrement:
            self.boredom = 0
        else:
            self.boredom += self.boredom_decrement

    def feed(self):
        if self.hunger < self.hunger_decrement:
            self.hunger = 0
        else:
            self.hunger += self.hunger_decrement

    def hi(self):
        return random.choice(self.words)


'''
Task C
'''

def teaching_session(my_pet, new_words):
    for word in new_words:
        my_pet.teach(word)
        my_pet.hi()
        print(my_pet)
        if my_pet.hunger > my_pet.hunger_threshold:
            my_pet.feed()
        my_pet.clock_tick()

fluffy = Pet(name='fluffy')
teaching_session(fluffy, new_words= ['I am sleepy', 'You are the best', 'I love you, too'])


#######################################################################
#---------- Part 2: Inheritance - subclasses
#######################################################################
'''
Task A: Dog and Cat
'''
#your code begins here . . .

class Dog(Pet):
    def __str__(self):
        return super().__str__().replace('.', ', arrrf!')

#d1 = Dog()
#print(d1)

class Cat(Pet):
    def __init__(self, name, meow_count):
        super().__init__(name)
        self.meows = meow_count

    def hi(self):
        w = (random.choice(self.words))
        return w * self.meows


'''
Task B: Poodle
'''
#your code begins here . . .

class Poodle(Dog):
    def dance(self):
        return "Dancing in circles like poodles do!"

    def say(self):
        print(self.dance())
        super().say()


p1 = Poodle('Polly')
p1.say()

c1 = Cat(name='Kitty', meow_count= 3)
print(c1.hi())
