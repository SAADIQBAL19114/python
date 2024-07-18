import math

def circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area , circumference

area, circumference = circle_stats(4)

print("Area: " , area, "Circumference: ", circumference)
