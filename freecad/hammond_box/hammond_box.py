#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
FREECADPATH = '/usr/lib/freecad/lib/'
sys.path.append(FREECADPATH)
sys.path.append(os.path.realpath(os.path.dirname(__file__)))
import FreeCAD
import Mesh
import tempfile
import doctools
import shutil

def machinebuilder(model, file_path):
    """
[doc]
-title-
Hammond 1550 box generator
-images_url-
http://static3.tme.eu/products_pics/a/b/8/ab8d69582f285942fdd5ccd29a678476/25560.jpg
-description-
Create Hammond 1550 box
[inputs]
str(model, ['1550B','1550A'])
    """
    
    # Here go the basic machine definition (main dimensions)
    source_files= os.path.join(os.path.realpath(os.path.dirname(__file__)), 'files')
    main_object= 'Fillet'
    object_data= {'1550B': {'length': '114.5',
                            'width': '64.00',
                            'height': '26.00',
                            'internal_length': '110.66',
                            'internal_width': '60.16',
                            'internal_height': '24.50',
                            'hole_x_interval': '104.5',
                            'hole_y_interval':'54.00',
                            'hole_depth':'6.00',
                            'hole_clearance_x':'98.50',
                            'hole_clearance_y':'48.00'},
                  '1550A': {'length': '89.00',
                            'width': '35.00',
                            'height': '26.00',
                            'internal_length': '85.16',
                            'internal_width': '31.16',
                            'internal_height': '24.50',
                            'hole_x_interval': '79.00',
                            'hole_y_interval':'25.00',
                            'hole_depth':'6.00',
                            'hole_clearance_x':'73.00',
                            'hole_clearance_y':'19.00'}}

    # Here go the computations for the secondary dimensions:
    hole_center_x = str(float(object_data[model]['length']) - float(object_data[model]['hole_x_interval']) / 2.0)
    hole_center_y = str(float(object_data[model]['width']) -  float(object_data[model]['hole_y_interval']) / 2.0)

    # Load the Document.xml file and replace the key values:
    with open(os.path.join(source_files, 'Document.xml'), 'r') as f:
        contents = ''.join(f.readlines())

    contents.format(length=object_data[model]['length'],
                    width=object_data[model]['width'],
                    height=object_data[model]['height'],
                    internal_length=object_data[model]['internal_length'],
                    internal_width=object_data[model]['internal_width'],
                    internal_height=object_data[model]['internal_height'],
                    hole_x_interval=object_data[model]['hole_x_interval'],
                    hole_y_interval=object_data[model]['hole_y_interval'],
                    hole_depth=object_data[model]['hole_depth'],
                    hole_clearance_x=object_data[model]['hole_clearance_x'],
                    hole_clearance_y=object_data[model]['hole_clearance_y'],
                    hole_center_x=hole_center_x,
                    hole_center_y=hole_center_y)

    # Create temporal dir and move all required files to it
    tmpdir = tempfile.mkdtemp()
    for src_dir, dirs, files in os.walk(source_files):
        for needed_file in files:
            if needed_file != 'Document.xml':
                shutil.copy2(os.path.join(source_files, needed_file), tmpdir)

    # Save the resulting xml file in a temporal file
    with tempfile.NamedTemporaryFile('w', dir=tmpdir, suffix='.xml') as f:
        f.write(contents)
        f.seek(0)

        # Generate a FreeCAD project from temp file
        out_file = file_path.replace(".stl", "") + ".fcstd"
        doctools.createDocument(f.name, out_file)

    # Open the FreeCAD doc and generate stl
    doc = FreeCAD.open(out_file)
    doc.recompute()

    obj = doc.getObject(main_object)
    Mesh.export([obj], file_path)