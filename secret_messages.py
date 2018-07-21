alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3
newmessage = ''

message = input('Please enter a message: ')

for character in message:
	if character in alphabet:
		position = alphabet.find(character) # Find the position of the character.
		newposition = (position + key) % 26  # Go back to position 0 once it gets to position 26
		newcharacter = alphabet[newposition]
		newmessage += newcharacter
	else:
		newmessage += character
print(newmessage)


friend_score = input('Please enter you two name to score the love: ')

total = 0
for character in friend_score:
	if character in alphabet:
		if character not in 'friend':
			score = alphabet.find(character)
			total += score
		elif character in 'friend':
			total += 20
	else:
		total += 0
if total > 90:
	print(total, 'Best friend!')
else:
	print(total, 'You are still a good friend for each other.')			