#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
FREECADPATH = '/usr/lib/freecad/lib/'
sys.path.append(FREECADPATH)
import FreeCAD
import Draft
import Mesh

def machinebuilder(text, size, height):
    '''
[doc]
-title-
Text Generator
-description-
Create text in 3D
[inputs]
str(text)
int(size)
int(height)
    '''

    #-- Generate text
    doc = FreeCAD.newDocument("TextGenerator")

    ss=Draft.makeShapeString(String=text,FontFile="/usr/share/fonts/truetype/droid/DroidSans.ttf",Size=size,Tracking=0)
    #ss=Draft.extrude(ss,FreeCAD.Base.Vector(0,0,10))

    obj = doc.addObject("Part::Extrusion","TextGenerator")
    obj.Base = ss
    obj.Dir = (0,0,height)

    doc.recompute()

    #-- Export the file
    name = text+"-"+str(size)+".stl"
    Mesh.export([obj], './%s' % name)

    return name