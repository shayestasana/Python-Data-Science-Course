class Cat:

    def __init__(self, breed, fur_color, gender='F', age=1, w=1, h=1, is_tamed=True):
        self.breed = breed #self makes breed a variable for Cat class
        self.fur_color = fur_color
        self.gender = gender
        self.age = age
        self.weight = w
        self.height = h
        self.is_tamed = is_tamed

    def eat(self, food='catfood'):            #  self --> it makes 'eat' automatically a function of the class 'Cat' ... and no calling is needed
        print(f'🐈 is eating {food}')
    
    def play(self):
        print('🐈 is playing')
    
    def sleep(self):
        print('🐈 is sleeping')
 
    def info(self):
        print('--'*15)  #optional design
        print(f'Breed: {self.breed}')
        print(f'Age: {self.age} year')
        print(f'Weight: {self.weight} kg')
        print(f'Height: {self.height} ft')
        print(f'Gender: {self.gender}')
        print(f'Color: {self.fur_color}')
        print(f'Tamed: {self.is_tamed}')
        print('--'*15)  

tom = Cat('Street cat', 'Grey', age=10, gender='M')
soni = Cat('houese cat', 'brown', age=3)
snowbell = Cat('Persian', 'White', age=6, w=5)
spike = Cat('Jungle cat', 'Black', age=13, w=3, h=1.5, is_tamed=False)

print("TOM")
tom.info()
tom.eat('jerry')

print("SNOWBELL")
snowbell.info()
snowbell.eat('stuart')