def trim(matrix):
	largest_y = 0
	largest_x = 0
	lowest_y = len(matrix[0])
	lowest_x = len(matrix)

	for x in range(len(matrix)):
		for y in range(len(matrix[0])):
			if matrix[x][y] == 0:
				if x < lowest_x:
					lowest_x = x
				if y < lowest_y:
					lowest_y = y
				if x > largest_x:
					largest_x = x
				if y > largest_y:
					largest_y = y
	trimmed = [[0 for j in range(largest_y-lowest_y+1)] for i in range(largest_x - lowest_x+1)]
	print(len(trimmed), len(trimmed[0]))
	for x in range(len(matrix)):
		for y in range(len(matrix[0])):
			if lowest_x <= x <= largest_x and lowest_y <= y <= largest_y:
				trimmed[x-lowest_x][y-lowest_y] = matrix[x][y]
	return trimmed

def feature_histogram(matrix):
	vertical = [0 for i in range(16)]
	horizontal = [0 for i in range(16)]

	sub_y = len(matrix[0]) // 16
	sub_x = len(matrix) // 16

	for x in range(len(matrix)):
		for y in range(len(matrix[0])):
			if matrix[x][y] == 0:
				if x>15*sub_x:
					vertical[15]+=1
				else:
					vertical[x//sub_x] += 1
				if y> 15* sub_y:
					horizontal[15]+=1
				else:
					horizontal[y//sub_y] += 1

	feature_vector = []
	for i, j in zip(vertical, horizontal):
		feature_vector.append(round((i-j)/(i+j), 2))
	return feature_vector

