import math

point1 = (float(input()),float(input()))
point2 = (float(input()),float(input()))

distancia = math.dist(point1,point2)
print("{:.4f}".format(distancia))