moves = "UD"
x = 0
y = 0
for move in moves:
	if move == 'L':
		x -= 1
	elif move == 'R':
		x += 1
	elif move == 'U':
		y += 1
	elif move == 'D':
		y -= 1

if x == 0 and y == 0:
	print('True')
else:
	print('False')
