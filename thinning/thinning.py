import copy
from filters import get_matrix
BLACK = 0
WHITE = 255

def zs_thin(img):
    flag = 1
    processing = True
    while processing:
        temp_pixel = copy.deepcopy(img.pixels)
        changed=False
        for r in range(img.height):
            for c in range(img.width):
                if img.pixels[r][c] == BLACK:
                    matrix = get_matrix(r, c, img)
                    if _zs_thin_conditions(matrix, flag):
                        temp_pixel[r][c] = WHITE
                        changed=True
        img.pixels = temp_pixel
        if changed is False:
            processing= False
        flag*=-1

    return img.pixels


def neighbor_check(matrix):
    counter = 0
    for i in matrix:
        for j in i:
            if j == BLACK:
                counter += 1

    return 2 <= counter-1 <=6

def _zs_thin_conditions(matrix, flag):
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
    return neighbor_check(matrix) and zero_one_check(points) and p2p4p8(points) and p2p6p8(points)

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
