from ImageFile import ImageFile
from features import feature_histogram, trim, zoning_method

suffix = ['-00a.bmp', '-00b.bmp', '-00c.bmp', '-00d.bmp', '-00e.bmp', '-00f.bmp', '-00g.bmp', '-00h.bmp', '-00i.bmp',
          '-00j.bmp', '-00k.bmp', '-00l.bmp', '-00m.bmp', '-00n.bmp', '-00o.bmp', '-00p.bmp', '-00q.bmp', '-00r.bmp',
          '-00s.bmp', '-00t.bmp', '-00u.bmp', '-00v.bmp', '-00w.bmp', '-00x.bmp', '-00y.bmp']

zeros = dict(path="./images/zero/", v=["0" + j for i, j in enumerate(suffix)])
ones = dict(path="./images/one/", v=["1" + j for i, j in enumerate(suffix)])
twos = dict(path="./images/two/", v=["2" + j for i, j in enumerate(suffix)])
threes = dict(path="./images/three/", v=["3" + j for i, j in enumerate(suffix)])
fours = dict(path="./images/four/", v=["4" + j for i, j in enumerate(suffix)])
fives = dict(path="./images/five/", v=["5" + j for i, j in enumerate(suffix)])
sixs = dict(path="./images/six/", v=["6" + j for i, j in enumerate(suffix)])
sevens = dict(path="./images/seven/", v=["7" + j for i, j in enumerate(suffix)])
eights = dict(path="./images/eight/", v=["8" + j for i, j in enumerate(suffix)])
nines = dict(path="./images/nine/", v=["9" + j for i, j in enumerate(suffix)])
lists = [zeros, ones, twos, threes, fours, fives, sixs, sevens, eights, nines]

f = open('histogram.txt', 'w')
for l in lists:
    files = l.get('v')
    path = l.get('path')
    for fil in files:
        img = ImageFile(path + fil)
        trimmed = trim(img)
        img_vector = feature_histogram(trimmed)
        f.write(",".join([str(s) for s in img_vector]))
        f.write('\n')
f.close()
