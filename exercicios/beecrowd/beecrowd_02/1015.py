import math

<<<<<<< HEAD
point1= (float(input()),float(input()))
point2= (float(input()),float(input()))
distancia = math.dist(point1,point2)

print("{:.4f}".format(distancia))
=======
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print('{:.4f}'.format(distancia))
>>>>>>> 1df64d17226899509f84ecedca209f807d2d2fe4
