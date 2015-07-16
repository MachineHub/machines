#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
FREECADPATH = '/usr/lib/freecad/lib/'
sys.path.append(FREECADPATH)
from pyooml import *

def machinebuilder(edge):
    '''
[doc]
-title-
Cube Generator
-description-
Create a parametric cube
[inputs]
int(edge=50,(0:1:100))
    '''

    #-- Generate the cube
    doc = newdoc()
    c = cube(edge,edge,edge)
    
    #-- Export the file
    name = "cube{}-{}-{}.stl".format(edge,edge,edge)
    c.export_STL('./%s' % name)
    
    return name
