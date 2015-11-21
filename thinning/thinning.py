import copy
from filters import get_matrix
import time
BLACK = 0
WHITE = 255

def zs_thin(img):
    img=zero_padding(img)
    flag = 1
    processing = True
    while processing:

        changed=False
        # t1=time.time()
        remove=[]
        for r in range(1,img.height-1):
            t1=time.time()
            for c in range(1,img.width-1):
                if img.pixels[r][c] == BLACK:
                    if _zs_thin_conditions(r,c,img, flag):
                        remove.append([r,c])
                        changed=True
            print(time.time()-t1)
        # print(time.time()-t1)
        for i in remove:
            img.pixels[i[0]][i[1]]=WHITE
        if changed is False:
            processing= False
        flag*=-1


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
    for i in points:
        if i==0:
            counter+=1

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
        return neighbor_check(points) and zero_one_check(points) and p2p4p6(points) and p4p6p8(points)
    return neighbor_check(points) and zero_one_check(points) and p2p4p8(points) and p2p6p8(points)

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

def p2p4p6(points):
    return WHITE in [points[0], points[2], points[4]]

def p4p6p8(points):
    return WHITE in [points[2], points[4], points[6]]

'''
second iteration
'''
def p2p4p8(points):
    return WHITE in [points[0], points[2], points[6]]

def p2p6p8(points):
    return WHITE in [points[0], points[4], points[6]]
'''
end second iteration
'''
