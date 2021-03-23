"""Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""
        
__author__ = "tanya"
__version__ = "2021.03.14"
        
import csv
import os
import rhinoscriptsyntax as rs
import Rhino as rh
import scriptcontext as sc
import Rhino.Geometry as rg
        

# constants
working_dir_path = "D:\\Google Drive\\Work\\Hired\\2020 - HQ Architects\\PyGH\\taba\\"
target_labels_path = "config\\target_labels.csv"
composite_path = "inputs\\composite.csv"
proc_composite_path = "inputs\\proc_composite.csv"
proc_polylines_path = "inputs\\proc_polylines.csv"
proc_attributes_path = "inputs\\proc_attributes.csv"

relevant_layers_dict = {"buildings": "2200", "plots" : "chelkot lines"}
MIN_BUILDING_AREA_SQM = 50
FLOOR_HEIGHT_M = 3

##########################################################################################################################################

# set scriptcontext.doc to Rhino.ActiveDoc
sc.doc = rh.RhinoDoc.ActiveDoc

# remove all blocks
for block in rs.BlockNames():
    rs.DeleteBlock(block)

# set current layer
rs.CurrentLayer(relevant_layers_dict["buildings"])

# remove redundant layers
for layer_name in rs.LayerNames():
    if layer_name not in relevant_layers_dict.values():
        rs.PurgeLayer(layer_name)

# get all objects in building layer        
building_objs = rs.ObjectsByLayer(relevant_layers_dict["buildings"])

for building_obj in building_objs:
    if rs.IsCurve(building_obj) and rs.IsCurveClosed(building_obj):        
        # flatten curve to XY plane
        matrix = rs.XformPlanarProjection(rg.Plane.WorldXY)
        rs.TransformObject(building_obj, matrix, copy=False)


##########################################################################################################################################

# set current working dir
os.chdir(working_dir_path)

# Add attributes to buildings
with open(proc_attributes_path,"r") as input_handle:
    rdr = csv.reader( input_handle )
        
    # read attribure labels (first row)
    attribute_labels_list = next(rdr)            
    
    # get x, y, z attributes indices
    x_idx, y_idx, z_idx = attribute_labels_list.index("Position X"), attribute_labels_list.index("Position Y"), attribute_labels_list.index("Position Z")
    
    # get all objects in building layer        
    building_objs = rs.ObjectsByLayer(relevant_layers_dict["buildings"])

    out_loop_counter = 0
    xy_found = 0

    for attributes_row in rdr:         
        out_loop_counter += 1
        x_val, y_val, z_val = float(attributes_row[x_idx]), float(attributes_row[y_idx]), float(attributes_row[z_idx])
        
        related_building_pnt = rs.CreatePoint(x_val, y_val, z_val)
        
        xy_found = False
        in_loop_counter = 0
        for building_obj in building_objs:
            in_loop_counter += 1
            if rs.IsCurve(building_obj) and rs.IsCurveClosed(building_obj) and (rs.CurveArea(building_obj)[0] > MIN_BUILDING_AREA_SQM):
                crv = rs.coercecurve(building_obj)
                if rs.PointInPlanarClosedCurve(related_building_pnt, crv):                
                    xy_found = True
                    for attr_label, attr_val in zip(attribute_labels_list, attributes_row):
                        rs.SetUserText(building_obj, attr_label, attr_val)
        if not xy_found:
            rs.SelectObject(building_obj)
            print(x_val, y_val, z_val)
    print(out_loop_counter)
##########################################################################################################################################

# Extrude all buildings according to NUM_FLOORS attribute multiplied by FLOOR_HEIGHT constant
# get all objects in building layer        
building_objs = rs.ObjectsByLayer(relevant_layers_dict["buildings"])
for building_obj in building_objs:
    if rs.IsCurve(building_obj) and rs.IsCurveClosed(building_obj) and rs.CurveArea(building_obj)[0] > MIN_BUILDING_AREA_SQM:
        crv = rs.coercecurve(building_obj)
        
        num_of_floors = rs.GetUserText(building_obj, "NUM_FLOORS")
        if num_of_floors == None:
            pass
#        building_height = FLOOR_HEIGHT_M * num_of_floors
        srf = rs.ExtrudeCurveStraight(crv,(0,0,0),(0,0,20))
        rs.CapPlanarHoles(srf)
        
rs.ViewDisplayMode(rs.CurrentView(),"Shaded")