class Animal:
  legs = 4

  def __init__(self, nm):
    self.name = nm

  def get_num_legs(self):
    return self.legs

class Cow(Animal):
  pass

class Bird(Animal):
  legs = 2

class Spider(Animal):
  legs = 8

c1 = Cow('Bessie')
b1 = Bird('Polly')
s1 = Spider('Charlotte')

animals = [c1, b1, s1]
for a in animals:
  print (a.name, 'has', a.get_num_legs(), 'legs')
