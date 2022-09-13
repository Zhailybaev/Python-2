print("Input lengths of the triangle sides:")
x=int(input("x: "))
y=int(input("y: "))
z=int(input("z: "))
if x==y and y==z:
    print("Equilateral triangle")
if x!=y and y!=z and x!=z:
    print("Scalene triangle")
if x==y and x!=z or x==z and x!=y or y==z and y!=x:
    print("Isosceles triangle")


