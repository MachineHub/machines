#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
FREECADPATH = '/usr/lib/freecad/lib/'
sys.path.append(FREECADPATH)
from pyooml import *

def machinebuilder(edge, file_path):
    '''
[doc]
-title-
Cube Generator
-description-
Create a parametric cube
-images_url-
http://images.freeimages.com/images/previews/92c/toy-1419795.jpg
http://images.freeimages.com/images/previews/ea8/wooden-cubes-1189233.jpg
http://images.freeimages.com/images/previews/b9c/cubes-1-1178873.jpg
[inputs]
int(edge=50,(0:1:100))
    '''

    #-- Generate the cube
    doc = newdoc()
    c = cube(edge,edge,edge)
    
    #-- Export the file
    c.export_STL(file_path)
