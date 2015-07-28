#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
FREECADPATH = '/usr/lib/freecad/lib/'
sys.path.append(FREECADPATH)
import FreeCAD
import Mesh
import os


def machinebuilder(text, size, height, file_path):
    '''
[doc]
-title-
Text Generator
-description-
Create text in 3D
-images_url-
http://images.freeimages.com/images/previews/17b/words-of-wisdom-1514865.jpg
[inputs]
str(text)
int(size=50)
int(height=5)
    '''

    #-- Open project
    doc = FreeCAD.openDocument(os.path.abspath("text-generator.fcstd"))

    #-- Edit parameters
    doc.ShapeString.FontFile = os.path.abspath("DroidSans.ttf")
    doc.ShapeString.String = text
    doc.ShapeString.Size = size
    doc.Extrude.Dir = (0, 0, height)
    doc.recompute()

    #-- Export the file
    Mesh.export([doc.Extrude], file_path)

    """
    # Alternative FreeCAD pure code

    doc = FreeCAD.newDocument("text-generator")

    import Draft
    ss = Draft.makeShapeString(
        String=text, FontFile=os.path.abspath("DroidSans.ttf"), Size=size, Tracking=0)
    obj = doc.addObject("Part::Extrusion", "text-generator")
    obj.Base = ss
    obj.Dir = (0, 0, height)
    doc.recompute()
    """
