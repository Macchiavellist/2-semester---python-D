import math


def degree_to_radian(degree):
    radian = degree * (math.pi / 180)
    print(f"Degree: {degree} => Radian: {radian:.6f}")

def area_of_trapezoid(height, base1, base2):
    area = (height * (base1 + base2)) / 2
    print(f"Area of trapezoid: {area:.1f}")


def area_of_polygon(sides, length):
    area = (sides * length**2) / (4 * math.tan(math.pi / sides))
    print(f"The area of the polygon is: {area:.1f}")


def area_of_parallelogram(base, height):
    area = base * height
    print(f"Area of parallelogram: {area:.1f}")


def main():

    degree = float(input("Enter degree to convert to radian: "))
    degree_to_radian(degree)


    height = float(input("\nEnter height of trapezoid: "))
    base1 = float(input("Enter the first base of trapezoid: "))
    base2 = float(input("Enter the second base of trapezoid: "))
    area_of_trapezoid(height, base1, base2)


    sides = int(input("\nEnter number of sides of polygon: "))
    length = float(input("Enter the length of a side of polygon: "))
    area_of_polygon(sides, length)


    base = float(input("\nEnter the base of parallelogram: "))
    parallelogram_height = float(input("Enter the height of parallelogram: "))
    area_of_parallelogram(base, parallelogram_height)


main()
