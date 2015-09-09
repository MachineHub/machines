import sys
FREECADPATH = '/usr/lib/freecad/lib/'
sys.path.append(FREECADPATH)
import FreeCAD
import Mesh
import os


def machinebuilder(length, width, height, file_path):

    document = os.path.abspath("hello.fcstd")
    #-- Open document
    doc = FreeCAD.openDocument(document)

    #-- Edit parameters
    cube = None
    for figure in doc.Objects:
        if figure.Label == 'hello_cube':
            cube = figure
    if cube:
        cube.Length = length
        cube.Height = height
        cube.Width = width
    	doc.recompute()

   	 #-- Export the file
    	Mesh.export([cube], file_path)
