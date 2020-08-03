import math

def weights(l):
    d = {}
    for i in l:
        root = math.sqrt(i)
        if int(root + 0.5) ** 2 == i:
            d[i] = 5
        elif(i % 4 == 0 and i % 6 == 0):
            d[i] = 4
        elif(i % 2 == 0):
            d[i] = 3
    sort_orders = sorted(d.items(), key=lambda x: x[1], reverse=True)
    for j in sort_orders:
        print(j[0],j[1])

weights([10,36,54,89,12])
