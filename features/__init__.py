from features import feature_histogram, trim
from PIL import Image
from PIL import ImageFilter

fp = open("B.bmp", "rb")
im = Image.open(fp)
pixels = list(im.getdata())
width, height = im.size
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

v = feature_histogram(trim(pixels))
print(v)
