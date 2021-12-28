


class bootleg():
    def __init__(self):
        self.sw = 0

counter = 0
objstore = []

o1 = bootleg()
o2 = bootleg()
o3 = bootleg()
objstore.append(o1)
objstore.append(o2)
objstore.append(o3)


while(True):
    counter = counter + 1

    for x in objstore:
        print(x.sw)
    if(counter == 4):
        counter = 0
        o2.sw = o2.sw+1
