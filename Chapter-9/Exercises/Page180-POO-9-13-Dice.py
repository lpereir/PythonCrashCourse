from random import randint
class Die:
    def __init__(self,sides=6):
        self.sides=sides
    
    def roll_die(self):
        print(f'{randint(1,self.sides)}')


test6 = Die()
test10 = Die(10)
test20 = Die(20)

print('-'*15)
print('6-sided die')
print('-'*15)
for i in range(1,11):
    print(f'{i}º - ',end='')
    test6.roll_die()

print()
print('-'*15)
print('10-sided die')
print('-'*15)
for i in range(1,11):
    print(f'{i}º - ',end='')
    test10.roll_die()

print()
print('-'*15)
print('20-sided die')
print('-'*15)
for i in range(1,11):
    print(f'{i}º - ',end='')
    test20.roll_die()
