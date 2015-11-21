BLACK = 0
WHITE = 255

def zs_thin(img):
    img=zero_padding(img)
    flag = 1
    processing = True

    while processing:
        changed=False
        remove=[]
        for r in range(1,img.height-1):
            for c in range(1,img.width-1):
                if img.pixels[r][c] == BLACK:
                    if _zs_thin_conditions(r,c,img, flag):
                        remove.append([r,c])
                        changed=True

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

def _zs_thin_conditions(r,c,img, flag):
    p2 = img.pixels[r-1][c]
    p3 = img.pixels[r-1][c+1]
    p4 = img.pixels[r][c+1]
    p5 = img.pixels[r+1][c+1]
    p6 = img.pixels[r+1][c]
    p7 = img.pixels[r+1][c-1]
    p8 = img.pixels[r][c-1]
    p9 = img.pixels[r-1][c-1]

    if flag == 1:
        if (p2 == WHITE or p4 == WHITE or p6 == WHITE) and (p4 == WHITE or p6 == WHITE or p8 == WHITE):
            tempo = None
            counter = 0
            for p in (p2,p3,p4,p5,p6,p7,p8,p9):
                if tempo is not None:
                    if tempo == WHITE and p == BLACK:
                        counter += 1
                tempo = p

            if tempo == WHITE and p2 == BLACK:
                counter += 1

            if counter == 1:
                counter = 0
                b = filter(lambda x:x==0, (p2,p3,p4,p5,p6,p7,p8,p9))
                for i in b:
                    counter += 1
                return 2 <= counter-1 <=6
            else:
                return False            
        else:
            return False
    else:
        if (p2 == WHITE or p6 == WHITE or p8 == WHITE) and (p2 == WHITE or p4 == WHITE or p8 == WHITE):
            tempo = None
            counter = 0
            for p in (p2,p3,p4,p5,p6,p7,p8,p9):
                if tempo is not None:
                    if tempo == WHITE and p == BLACK:
                        counter += 1
                tempo = p

            if tempo == WHITE and p2 == BLACK:
                counter += 1

            if counter == 1:
                counter = 0
                b = filter(lambda x:x==0, (p2,p3,p4,p5,p6,p7,p8,p9))
                for i in b:
                    counter += 1
                return 2 <= counter-1 <=6
            else:
                return False            
        else:
            return False           

# used for profiling:
def main():
    img = ImageFile('2015-11-20-19-05-36-1.bmp')
    output = zs_thin(img)
    new_file = img.save_img(output, '2015-11-20-19-05-36-1.bmp')

if __name__ == '__main__':
    main()