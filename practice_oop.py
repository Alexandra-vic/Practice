class Berd:
    wings = 'i have wings'
   
    def can_fly(self):
        print('I can fly')

    def can_swim(self):
        print('I can swim')

    def cannot_fly(self):
        print('I cannot fly')
        
    def cannot_swim(self):
        print('I cannot swim')    

        
class Fish:
    gills = 'I breathe through gills'

    def can_swim(self):
        print('I can swim')    

        
class Mammals:
    wool = 'I have wool'
    baby_eats_milk = 'I feed my baby milk'

    def can_swim(self):
        print('I can swim')        
    


class Predator:
    def eat(self):
        print('I eat Fish')

    def also_eat(self):
        print('I eat meat')    

class Herbivorous:
    def eat(self):
        print('I cannot eat meat ')        

        

class Penguin(Berd, Predator):
    def __init__(self, type, age):
        self.type = type
        self.age = age
        print(f'Type - {self.type}\nAge - {self.age}')
    

class Falcon(Berd, Predator):
    def __init__(self, type, age):
        self.type = type
        self.age = age
        print(f'\nType - {self.type},\nAge - {self.age}')
    
        
class Trout(Fish, Predator):
    def __init__(self, type, age):
        self.type = type
        self.age = age
        print(f'\nType - {self.type},\nAge - {self.age}')    

        
class Whale(Mammals, Predator):
    def __init__(self, type, age):
        self.type = type
        self.age = age
        print(f'\nType - {self.type}\nAge - {self.age}')
        

c = Penguin('Royal', '1')
print(c.wings)
c.can_swim()
c.cannot_fly()
c.eat()

a = Falcon('Peregrine falcon', '7')
print(a.wings)
a.can_fly()
a.cannot_swim()
a.also_eat()

f = Trout('Salmo trutta marmoratus', '3')
print(f.gills)
f.can_swim()
f.eat()

k = Whale('Blue whale', '60')
print(k.wool,'and', k.baby_eats_milk)
k.can_swim()
k.eat()