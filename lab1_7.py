import math

input("Enter a, b, c form y = ax2 + bx + c:")
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

d = b**2-4*a*c

if d<0:
    print ("No roots")
elif d == 0:
    x = (-b + math.sqrt(b**2-4*a*c))/2*a
    print (x)
else:
    x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    print (x1, '\n',x2)

