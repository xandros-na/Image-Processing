def trim(img):
	largest_y = 0
	largest_x = 0
	lowest_y = img.width
	lowest_x = img.height

	for x in range(img.height):
		for y in range(img.width):
			if img.pixels[x][y] == 0:
				if x < lowest_x:
					lowest_x = x
				if y < lowest_y:
					lowest_y = y
				if x > largest_x:
					largest_x = x
				if y > largest_y:
					largest_y = y
	trimmed = [[0 for j in range(largest_y-lowest_y+1)] for i in range(largest_x - lowest_x+1)]
	
	for x in range(img.height):
		for y in range(img.width):
			if lowest_x <= x <= largest_x and lowest_y <= y <= largest_y:
				trimmed[x-lowest_x][y-lowest_y] = img.pixels[x][y]
	return trimmed

def feature_histogram(trimmed):
	vertical = [0 for i in range(16)]
	horizontal = [0 for i in range(16)]
	width = len(trimmed[0])
	height = len(trimmed)
	# width, height, trimmed = _append_zero(trimmed, 16)
	# for i in trimmed:
	# 	print(i)
	sub_y = width / 16
	sub_x = height / 16

	for x in range(height):
		for y in range(width):
			if trimmed[x][y] == 0:
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
		feature_vector.append(round((i-j*1.0)/(i+j*1.0), 2))
	return feature_vector

# def _append_zero(trimmed, n):
# 	rem_w = 0
# 	rem_h = 0
# 	width = len(trimmed[0])
# 	height = len(trimmed)
# 	if width%n != 0 or width < n:
# 		rem_w = n-(width % n)
# 		for row in trimmed:
# 			for r in range(rem_w):
# 				row.append(255)

# 	width += rem_w
# 	if height%n != 0 or height < n:
# 		rem_h = n-(height % n)
# 		for h in range(rem_h):
# 			trimmed.append([255 for i in range(width)])
# 	height += rem_h	
# 	return width, height, trimmed

def zoning_method(trimmed):
	feature_vector = []
	width = len(trimmed[0])
	height = len(trimmed)
	#width, height, trimmed = _append_zero(trimmed, 4)

	sub_y = width / 4
	sub_x = height / 4
	black = [0 for i in range(16)]
	for x in range(height):
		for y in range(width):
			if trimmed[x][y] == 0:
				if x >= 3*sub_x:
					if y>=3*sub_y:
						black[15] += 1
					else:
						black[12+(y//sub_y)] += 1
				elif y >= 3*sub_y:	
					if x>=3*sub_x:
						black[15] += 1
					else:
						black[(x//sub_x)*4+3] += 1
				else:		
					black[(x//sub_x)*4+(y//sub_y)] += 1
	black[15]=black[15]/2

	for b in range(len(black)):
		black[b] = round((black[b]*1.0) / (1.0*sub_x*sub_y), 2) 
	return black

