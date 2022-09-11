class Cat:
    breed = ""
    gender = None
    fur_color = ""
    age = ""
    weight = None
    height = None
    is_tamed = None

    def eat(self, food='catfood'):            #  self --> it makes 'eat' automatically a function of the class 'Cat' ... and no calling is needed
        print(f'🐈 is eating {food}')
    
    def play(self):
        print('🐈 is playing')
    
    def sleep(self):
        print('🐈 is sleeping')


billu = Cat()  # constructor calling
tom = Cat()
bagadbilla = Cat()

billu.breed = 'Persian'
billu.weight = 2
billu.age = 2
billu.fur_color = 'white'
billu.height = 1
billu.is_tamed = True
billu.gender = 'M'

tom.breed = 'Street cat'
tom.weight = 1.5
tom.age = 100
tom.fur_color = 'grey'
tom.height = 1.1
tom.is_tamed = True
tom.gender = 'M'

bagadbilla.breed = 'Wild cat'
bagadbilla.weight = 2
bagadbilla.age = 40
bagadbilla.fur_color = 'black'
bagadbilla.height = 4
bagadbilla.is_tamed = False
bagadbilla.gender = 'M'

print('Tom Details')
print('breed:', tom.breed)
print('gender:', tom.gender)
print('age:', tom.age)
print('weight:', tom.weight)
print('height:', tom.height)
print('color:', tom.fur_color)
print('pet:', 'yes' if tom.is_tamed else 'no')
tom.eat()
tom.sleep()
tom.play()


print('Billu Details')
print('breed:', billu.breed)
print('gender:', billu.gender)
print('age:', billu.age)
print('weight:', billu.weight)
print('height:', billu.height)
print('color:', billu.fur_color)
print('pet:', 'yes' if billu.is_tamed else 'no')
billu.eat()
billu.sleep()
billu.play()


print('Bagadbilla Details')
print('breed:', bagadbilla.breed)
print('gender:', bagadbilla.gender)
print('age:', bagadbilla.age)
print('weight:', bagadbilla.weight)
print('height:', bagadbilla.height)
print('color:', bagadbilla.fur_color)
print('pet:', 'yes' if bagadbilla.is_tamed else 'no')
bagadbilla.eat('mouse')
bagadbilla.eat('bird')
bagadbilla.sleep()
bagadbilla.play('bird')