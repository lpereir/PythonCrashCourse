class Restaurant:
    def __init__(self,restaurant_name,cuisine_type, number_served=0):
        '''Initializing name and ty atributes'''
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

outback=Restaurant('Outback','Texas Food')
outback.describe_restaurant()
outback.open_restaurant()
print()
outback.set_number_served(15)
outback.describe_restaurant()
print()
outback.increment_number_served(10)
outback.describe_restaurant()





