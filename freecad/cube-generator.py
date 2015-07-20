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
[inputs]
int(edge=50,(0:1:100))
    '''

    #-- Generate the cube
    doc = newdoc()
    c = cube(edge,edge,edge)
    
    #-- Export the file
    c.export_STL(file_path)
