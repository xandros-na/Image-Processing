from PIL import Image
from PIL import ImageFilter
import copy
import time
from datetime import datetime

KERNEL_SIZE = 3
def open_file(filename):
	fp = open(filename, "rb")
	im = Image.open(fp)
	pixels = list(im.getdata())
	width, height = im.size
	pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
	return im, fp, width, height, pixels


def get_matrix(r, c, width, height, pixels):
	m = [[0,0,0], [0,0,0], [0,0,0]]
	for i in range(-1, 2):
		for j in range(-1,2):
			if (r+i>=0 and c+j>=0) and (r+i<=height-1 and c+j<= width-1):
				m[i+1][j+1]=pixels[r+i][c+j]
	return m


def apply_kernel(kernel, matrix):
	s = 0
	for ker, mat in zip(kernel, matrix):
		for k, m in zip(ker, mat):
			s += k * m
	return s


def produce_output(kernel, pixels, width, height):
	output = copy.deepcopy(pixels)
	for r in range(height):
		for c in range(width):
			matrix = get_matrix(r, c, width, height, pixels)
			s = apply_kernel(kernel, matrix)
			output[r][c] = round(s)
	return output


def save_img(width, height, im, output, filename):
	for r in range(height):
		for c in range(width):
			im.putpixel((c,r),output[r][c])
	ts = time.time() 
	ts = datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
	new_file = ts + filename
	im.save(new_file)
	return new_file
