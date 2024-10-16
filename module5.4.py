#class Example:
    #def __new__(cls, *args, **kwargs):
        #print(args)
        #print(kwargs)
        #return object.__new__(cls)
   # def __init__(self, first, second, third):
        #self.first = first
        #self.second = second
        #self.third = third

class House:

    houses_history = []
    def __new__(cls, name, *args, **kwargs,):
        cls.houses_history.append(name)
        return object.__new__(cls)







    def __init__(self, name, number_of_floors,):

        self.name = name
        self.number_of_floors = number_of_floors
    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')


       
#first = ('data')
#second = 25
#third = 3,14
#ex = Example(first, second, third)

h1 = House('ЖК Эльбрус', 10)

print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
del h2
#h_h = [h1, h2, h3]


