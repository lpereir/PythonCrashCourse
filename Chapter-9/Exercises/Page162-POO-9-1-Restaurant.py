class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        '''Initializing name and ty atributes'''
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print(f'The restaurant name is {self.restaurant_name}')
        print(f'The cuisine type is {self.cuisine_type}')
    def open_restaurant(self):
        print('The restaurant is OPEN!')

outback=Restaurant('Outback','Texas Food')
outback.describe_restaurant()
outback.open_restaurant()
print()
Cocobambu=Restaurant('Coco Bambu','Sea Food')
Cocobambu.describe_restaurant()
Cocobambu.open_restaurant()
print()
Brutus=Restaurant('Brutus','Hamburger')
Brutus.describe_restaurant()
Brutus.open_restaurant()