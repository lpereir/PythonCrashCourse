from random import choice

lucky_numbers=[1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e']
winner_ticket=list()
for i in range(0,4):
    var=choice(lucky_numbers)
    winner_ticket.append(var)
    lucky_numbers.remove(var)
print(f'Any Ticket matching {winner_ticket} wins a prize')


