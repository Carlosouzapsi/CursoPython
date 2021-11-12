
'''
Exercise 12: Distance Between Two Points on Earth
(27 Lines)
The surface of the Earth is curved, and the distance between degrees of longitude
varies with latitude. As a result, finding the distance between two points on the surface
of the Earth is more complicated than simply using the Pythagorean theorem.
Let (t1, g1) and (t2, g2) be the latitude and longitude of two points on the Earth’s
surface. The distance between these points, following the surface of the Earth, in
kilometers is:
distance = 6371.01 × arccos(sin(t1) × sin(t2) + cos(t1) × cos(t2) × cos(g1 − g2))

Create a program that allows the user to enter the latitude and longitude of two
points on the Earth in degrees. Your program should display the distance between
the points, following the surface of the earth, in kilometers.
'''
import math

t1 = int(input('Informe a latitude do ponto 1 em graus: '))
g1 = int(input('Informe a longitude do ponto 1 em graus: '))
t2 = int(input('Informe a latitude do ponto 2 em graus: '))
g2 = int(input('Informe a longitude do ponto 2 em graus:'))

t1_rad = math.radians(t1)
g1_rad = math.radians(g1)
t2_rad = math.radians(t2)
g2_rad = math.radians(g2)

def calcDist():
    d = 6371.01 * (math.acos(math.sin(t1_rad) * math.sin(t2_rad) + (math.cos(t1_rad) * math.cos(t2_rad) * math.cos(g1_rad - g2_rad))))
    return d
print(calcDist())











