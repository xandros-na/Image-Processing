import copy
# from filters import get_matrix
import time
BLACK = 0
WHITE = 255

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
    
    def save_img(self, output, filename):
        for r in range(1,self.height-1):
            for c in range(1,self.width-1):
                self.img.putpixel((c-1,r-1), output[r][c])

        new_file = ImageFile.time_stamp() + filename[20:]
        self.img.save(new_file)
        return new_file

    @staticmethod
    def time_stamp():
        ts = time.time() 
        ts = datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S-')
        return ts


def zs_thin(img):
    img=zero_padding(img)
    flag = 1
    processing = True
    # c = 0
    while processing:

        changed=False
        # t1=time.time()
        remove=[]
        for r in range(1,img.height-1):
            # t1=time.time()
            for c in range(1,img.width-1):
                if img.pixels[r][c] == BLACK:
                    if _zs_thin_conditions(r,c,img, flag):
                        remove.append([r,c])
                        changed=True
            # print(time.time()-t1)
        # print(time.time()-t1)
        for i in remove:
            img.pixels[i[0]][i[1]]=WHITE
        if changed is False:
            processing= False
        flag*=-1
        # c+=1
    # print(c)

    return img.pixels

def zero_padding(img):

    for i in range(img.height):
        img.pixels[i]=[255]+img.pixels[i]
        img.pixels[i].append(255)
    img.height+=2
    img.width+=2
    img.pixels=[[255 for i in range(img.width)]]+img.pixels
    img.pixels.append([255 for i in range(img.width)])

    return img

def neighbor_check(points):
    counter = 0
    # for i in points:
    #     if i==0:
    #         counter+=1
    b = filter(lambda x:x==0, points)
    for i in b:
        counter += 1
    return 2 <= counter-1 <=6

def _zs_thin_conditions(r,c,img, flag):
    p2 = img.pixels[r-1][c]
    p3 = img.pixels[r-1][c+1]
    p4 = img.pixels[r][c+1]
    p5 = img.pixels[r+1][c+1]
    p6 = img.pixels[r+1][c]
    p7 = img.pixels[r+1][c-1]
    p8 = img.pixels[r][c-1]
    p9 = img.pixels[r-1][c-1]
    points = [p2, p3, p4, p5, p6, p7, p8, p9]

    if flag == 1:
        return p2p4p6(p2, p4, p6) and  p4p6p8(p4, p6, p8) and zero_one_check(points) and neighbor_check(points)
    return  p2p6p8(p2, p6, p8) and  p2p4p8(p2, p4, p8) and  zero_one_check(points) and neighbor_check(points)
    #     return neighbor_check(points) and zero_one_check(points) and p2p4p6(points) and p4p6p8(points)
    # return neighbor_check(points) and zero_one_check(points) and p2p4p8(points) and p2p6p8(points)

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

    return counter == 1

def p2p4p6(p2, p4, p6):
    return p2 == WHITE or p4 == WHITE or p6 == WHITE

def p4p6p8(p4, p6, p8):
    return p4 == WHITE or p6 == WHITE or p8 == WHITE

'''
second iteration
'''
def p2p4p8(p2, p6, p8):
    return p2 == WHITE or p6 == WHITE or p8 ==WHITE

def p2p6p8(p2, p4, p8):
    return p2 == WHITE or p4 == WHITE or p8 == WHITE
'''
end second iteration
'''

def main():
    img = ImageFile('2015-11-20-19-05-36-1.bmp')
    output = zs_thin(img)
    new_file = img.save_img(output, '2015-11-20-19-05-36-1.bmp')

if __name__ == '__main__':
    main()