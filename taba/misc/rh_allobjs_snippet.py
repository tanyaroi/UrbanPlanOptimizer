"""Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""

__author__ = "tanya"
__version__ = "2021.03.17"

import rhinoscriptsyntax as rs
import Rhino as rh
import scriptcontext as sc
        
sc.doc = rh.RhinoDoc.ActiveDoc


all_objs = rs.AllObjects()

#obj_crv = rs.coercecurve(all_objs[0])
#print(obj_crv)

#pnt = rs.CreatePoint(float(-22), float(-1), float(0))
pnt = rs.CreatePoint(float(42), float(-3), float(0))

counter = 0
for obj in all_objs:
    crv = rs.coercecurve(obj)        
    in_curve = rs.PointInPlanarClosedCurve(pnt, crv)
    
    counter += 1
    
    if(in_curve):
        print(counter, "Tada")

    
    points = rs.PolylineVertices(curve)
    pnt = rs.CreatePoint(float(235), float(240), float(0))
    rs.SetUserText(curve, "PartNo", "KM40-4960" )

    print(counter, crv)