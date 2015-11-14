from PIL import Image
from PIL import ImageFilter
import time
from datetime import datetime

KERNEL_SIZE = 3

class ImageFile:
	def __init__(self, filename):
		self.filename = filename
		self._open_file()
		return 
	
	def _open_file(self):
		fp = open(self.filename, "rb")
		self.img = Image.open(fp)
		pixels = list(self.img.getdata())
		self.width, self.height = self.img.size
		self.pixels = [pixels[i * self.width:(i + 1) * self.width] for i in range(self.height)]
		return
	
	def save_img(self, output, filename):
		for r in range(self.height):
			for c in range(self.width):
				self.img.putpixel((c,r), output[r][c])

		ts = time.time() 
		ts = datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
		new_file = ts + filename
		self.img.save(new_file)
		return new_file