import copy

def get_matrix(r, c, img):
	m = [[0,0,0], [0,0,0], [0,0,0]]
	for i in range(-1, 2):
		for j in range(-1,2):
			if (r+i>=0 and c+j>=0) and (r+i<=img.height-1 and c+j<= img.width-1):
				m[i+1][j+1]=img.pixels[r+i][c+j]
	return m


def apply_kernel(kernel, matrix):
	s = 0
	for ker, mat in zip(kernel, matrix):
		for k, m in zip(ker, mat):
			s += k * m
	return s


def produce_output(kernel, img):
	output = copy.deepcopy(img.pixels)
	for r in range(img.height):
		for c in range(img.width):
			matrix = get_matrix(r, c, img)
			s = apply_kernel(kernel, matrix)
			output[r][c] = round(s)
	return output
