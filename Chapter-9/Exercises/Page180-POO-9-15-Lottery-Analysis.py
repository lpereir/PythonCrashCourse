from random import choice

lucky_numbers=[1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e']
winner_ticket=list()
for i in range(0,4):
    var=choice(lucky_numbers)
    winner_ticket.append(var)
    lucky_numbers.remove(var)
print('-'*30)
print(f'Any Ticket matching {winner_ticket} wins a prize')
print('-'*30)
count=0
try_ticket=list()
#try_numbers=[1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e']
while True:
    try_numbers=[1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e']
    for i in range(0,4):
        temp=choice(try_numbers)
        try_ticket.append(temp)
        try_numbers.remove(temp)
    if try_ticket == winner_ticket:
        print('-'*30)
        print('!!CONGRATULATIONS!!')
        print(f'After {count} tries, you wins a prize')
        print('-'*30)
        break
    try_ticket.clear()
    count +=1


