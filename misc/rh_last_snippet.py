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
import Rhino.Geometry as rg

sc.doc = rh.RhinoDoc.ActiveDoc

# remove all blocks
for block in rs.BlockNames():
    rs.DeleteBlock(block)

# set current layer
relevant_layers_dict = {"buildings": "2200", "plots" : "chelkot lines"}
rs.CurrentLayer(relevant_layers_dict["buildings"])

# remove all redundant layers
for layer_name in rs.LayerNames():
    if layer_name not in relevant_layers_dict.values:
        rs.PurgeLayer(layer_name)

# get all objects in building layer        
building_objs = rs.ObjectsByLayer(relevant_layers_dict["buildings"])

#obj_crv = rs.coercecurve(all_objs[0])
#print(obj_crv)

#pnt = rs.CreatePoint(float(-22), float(-1), float(0))
pnt = rs.CreatePoint(float(0), float(0), float(0))

counter = 0
for obj in building_objs:
    crv = rs.coercecurve(obj)        
    in_curve = rs.PointInPlanarClosedCurve(pnt, crv)
    
    counter += 1
    
    if(in_curve):
        print(counter, "Tada")

    rs.SetUserText(obj, "PartNo12", "3" )

    
    
    print (rs.GetUserText(obj, "PartNo14"))
    print(counter, crv)
    
srf = rs.ExtrudeCurveStraight(crv,(0,0,0),(0,0,20))
rs.CapPlanarHoles(srf)


rs.ViewDisplayMode(rs.CurrentView(),"Shaded")