from random import randint

player = input('Choose either rock(r) or paper(p) or scissors(s):')

print(player, 'vs',end=' ') # end with a space instead of a new line
chosen = randint(1,3)
if chosen == 1:
	computer = 'r'
elif chosen == 2:
	computer = 'p'
elif chosen == 3:
	computer = 's'

print(computer)

if player == computer :
	print('Draw')
elif player == 'r' and computer == 's':
	print('player wins!')
elif player == 'r' and computer == 'p':
	print('Computer wins!')
elif player == 'p' and computer == 's':
	print('Computer wins!')
elif player == 'p' and computer == 'r':
	print('player wins!')
elif player == 's' and computer == 'r':
	print('Computer wins!')
elif player == 's' and computer == 'p':
	print('player wins!')