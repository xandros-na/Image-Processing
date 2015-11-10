BLACK = 0
WHITE = 255

def neighbor_check(matrix):
	counter = 0
	for i in matrix:
		for j in i:
			if j == BLACK:
				counter += 1
	
	if 2 <= counter-1 <=6:
		return True  
	return False

def zs_thin(matrix, flag):
	p2 = matrix[0][1]
	p3 = matrix[0][2]
	p4 = matrix[1][2]
	p5 = matrix[2][2]
	p6 = matrix[2][1]
	p7 = matrix[2][0]
	p8 = matrix[1][0]
	p9 = matrix[0][0]
	points = [p2, p3, p4, p5, p6, p7, p8, p9]
	if flag == 1:
		return neighbor_check(matrix) and zero_one_check(points) and p2p4p6(points) and p4p6p8(points)
	return neighbor_check(matrix) and zero_one_check(points) and p2p6p8(points) and p2p6p8(points)

def zero_one_check(points):
	tempo = None
	counter = 0
	for p in points:
		if tempo is not None:
			if tempo == WHITE and p == BLACK:
				counter += 1
		tempo = p

	if tempo == WHITE and points[0] == BLACK:
		counter += 1

	if counter == 1:
		return True
	return False

def p2p4p6(points):
	if WHITE in [points[1], points[3], points[5]]:
		return True
	return False
	
def p4p6p8(points):
	if WHITE in [points[3], points[5], points[7]]:
		return True
	return False

'''
second iteration
'''
def p2p4p8(points):
	if WHITE in [points[1], points[3], points[7]]:
		return True
	return False

def p2p6p8(points):
	if WHITE in [points[1], points[5], points[7]]:
		return True
	return False
'''
end second iteration
'''