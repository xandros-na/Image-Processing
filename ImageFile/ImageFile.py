from PIL import Image
from PIL import ImageFilter
import time
from datetime import datetime

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
		fp.close()
		return
	
	def save_img(self, output, filename, thinning=False):
		if thinning:
			for r in range(1,self.height-1):
				for c in range(1,self.width-1):
					self.img.putpixel((c-1,r-1), output[r][c])
		else:
			for r in range(self.height):
				for c in range(self.width):
					self.img.putpixel((c,r), output[r][c])	

		new_file = ImageFile.time_stamp() + filename[20:]
		self.img.save(new_file)
		return new_file

	@staticmethod
	def time_stamp():
		ts = time.time() 
		ts = datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S-')
		return ts