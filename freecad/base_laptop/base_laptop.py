import sys

FREECADPATH = '/usr/lib/freecad/lib/'
sys.path.append(FREECADPATH)

from math import cos, radians, sin, sqrt, asin, degrees
from pyooml import newdoc, cube, cylinder
import FreeCAD


def union(g, ang):
    c = cube(3*g, 3*g, g)
    p = cylinder(r=3*g, h=g).translate(3*g, 3*g, 0)
    c -= p
    c.rotate(v=FreeCAD.Vector(0, 0, 1), ang=ang)
    return c


def square(x=2, y=2, z=2, g=1, direc='z'):
    gx, gy, gz, ix, iy, iz = 0, 0, 0, 0, 0, 0
    if direc == 'x':
        gx, gy, gz, ix, iy, iz = 0, g, g, x, y-2*g, z-2*g
    elif direc == 'y':
        gx, gy, gz, ix, iy, iz = g, 0, g, x-2*g, y, z-2*g
    elif direc == 'z':
        gx, gy, gz, ix, iy, iz = g, g, 0, x-2*g, y-2*g, z
    else:
        raise Exception()

    c = cube(x, y, z) - cube(ix, iy, iz).translate(gx, gy, gz)

    if direc == 'z':
        p = union(g, 0).translate(g, g, 0)
        p += union(g, 90).translate(x-g, g, 0)
        p += union(g, 270).translate(g, y-g, 0)
        p += union(g, 180).translate(x-g, y-g, 0)
        c +=p

    if direc == 'y':
        p = union(g, 0).translate(g, g, 0)
        p += union(g, 90).translate(x-g, g, 0)
        p += union(g, 270).translate(g, z-g, 0)
        p += union(g, 180).translate(x-g, z-g, 0)
        p.rotate(v=FreeCAD.Vector(1, 0, 0), ang=90).translate(0, g, 0)
        c += p

    return c


def machinebuilder(X, Y, angle, G, file_path):
    '''
[doc]
-title-
Base Laptop
-description-
Create a base to your laptop.
Version 1.0
-images_url-
http://images.freeimages.com/images/previews/e49/isolated-macbook-pro-1615424.jpg
[inputs]
int(X=150,(100:5:250))
float(Y=200)
int(angle=30,[30,35,40,45])
int(G=10)
    '''
    print X, Y, angle, G
    doc = newdoc()
    c = square(X, Y, G, G, 'z')

    p = square(X, G/2, 2*G, G/2, 'y')
    p.translate(0, Y-G/2, 0)
    c += p

    p = cube(sqrt((X*X + Y*Y))-2*G, G, G/2)
    ang = degrees(asin(Y/sqrt((X*X + Y*Y))))
    p.rotate(v=FreeCAD.Vector(0, 0, 1), ang=ang)
    p.translate(G, 0, G/2)
    c += p

    p = cube(sqrt((X*X + Y*Y))-2*G, G, G/2)
    ang = degrees(asin(Y/sqrt((X*X + Y*Y))))
    p.rotate(v=FreeCAD.Vector(0, 0, 1), ang=ang)
    p.rotate(v=FreeCAD.Vector(0, 1, 0), ang=180)
    p.translate(X-G, 0, G)
    c += p

    c.rotate(v=FreeCAD.Vector(1, 0, 0), ang=-angle)
    c.translate(0, 0, sin(radians(angle)) * Y)
    p = square(X, G, sin(radians(angle)) * Y, G, 'y')
    c += p
    p = square(X, cos(radians(angle)) * Y, G, G, 'z')
    c += p
    c.export_STL(file_path)
    return 'laptop.stl'

if __name__ == "__main__":
    machinebuilder(200, 200, 30, 10)
