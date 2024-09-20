class Restaurant:
    def __init__(self,restaurant_name,cuisine_type, number_served=0):
        '''Initializing name and the atributes'''
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=number_served
    def describe_restaurant(self):
        print(f'The restaurant name is {self.restaurant_name}')
        print(f'The cuisine type is {self.cuisine_type}')
        print(f'The number of customer served is {self.number_served}')
    def open_restaurant(self):
        print('The restaurant is OPEN!')
    def set_number_served(self,n):
        self.number_served=n
    def increment_number_served(self,num):
        self.number_served+=num

class IceCreamStand(Restaurant):
    '''Initializing name and the atributes'''
    def __init__(self,restaurant_name,cuisine_type, number_served,flavors):
        super().__init__(restaurant_name,cuisine_type, number_served)
        self.flavors=flavors

    def display_flavors(self):
        print('-'*20)
        print('Available Flavors:')
        print('-'*20)
        for flavor in self.flavors:
            print(f'{flavor}', end='\n')
        print('-'*20)


gelaguela=IceCreamStand('Gela Guela','Ice Cream', 10, ['Morango','Chocolate','Coco','Abacaxi','Pistache'])
gelaguela.describe_restaurant()
gelaguela.display_flavors()
