# lambda arguments: expression
add10 = lambda  x: x + 10
# print(add10(2))

mult = lambda x,y: x*y
# print(mult(2,10))

points2d = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2d_sorted = sorted(points2d, key=lambda x: x[1])

print(points2d_sorted)
print(points2d)


 