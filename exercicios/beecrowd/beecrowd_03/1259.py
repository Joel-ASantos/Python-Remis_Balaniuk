par = []
impar = []

var=int(input())
for i in range(var):
    num = int(input())
    
    if num % 2 == 0:
        par.append(num)
    elif num % 2 == 1:
        impar.append(num)

par.sort()
impar.sort(reverse=True)

print("\n")
for num in par:
    print(num)

for num in impar:
    print(num)