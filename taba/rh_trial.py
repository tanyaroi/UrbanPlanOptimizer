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
from config import *
        
###################################### Pre-Process #################################################################

# set scriptcontext.doc to Rhino.ActiveDoc
sc.doc = rh.RhinoDoc.ActiveDoc

# delete all previous user text
all_objs = rs.AllObjects()
for obj in all_objs:
    rh_obj = rs.coercerhinoobject(obj)
    rh_obj.Attributes.DeleteAllUserStrings()

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

        # delete all object with a surface grater or smaller from MIN_BUILDING_AREA_SQ by TOLERANCE or just smaller than MIN_BUILDING_AREA_SQ
        TOLERANCE = 2
        if rs.CurveArea(building_obj)[0] < MIN_BUILDING_AREA_SQM or abs(rs.CurveArea(building_obj)[0] - MIN_BUILDING_AREA_SQM) < TOLERANCE:
            rs.DeleteObject(building_obj)


####################################### Add attributes per building #################################################

# set current working dir
os.chdir(working_dir_path)

# Add attributes to plots
with open(proc_attributes_path,"r") as input_handle:
    rdr = csv.reader( input_handle )
        
    # read attribure labels (first row)
    attribute_labels_list = next(rdr)            
    
    # get x, y, z attributes indices
    x_idx, y_idx, z_idx = attribute_labels_list.index("Position X"), attribute_labels_list.index("Position Y"), attribute_labels_list.index("Position Z")
    
    # get all objects in plots layer        
    building_objs = rs.ObjectsByLayer(relevant_layers_dict["buildings"])

    for attributes_row in rdr:
        x_val, y_val, z_val = float(attributes_row[x_idx]), float(attributes_row[y_idx]), float(attributes_row[z_idx])
        
        related_building_pnt = rs.CreatePoint(x_val, y_val, z_val)
        
        for building_obj in building_objs:
            if rs.IsCurve(building_obj) and rs.IsCurveClosed(building_obj):
                crv = rs.coercecurve(building_obj)
                if rs.PointInPlanarClosedCurve(related_building_pnt, crv):                                               
                    for attr_label, attr_val in zip(attribute_labels_list, attributes_row):
                        
                        # if NUM_APTS_C already set, add to it
                        num_of_apts_label = "NUM_APTS_C"
                        if attr_label == num_of_apts_label:
                            num_of_apts_val = rs.GetUserText(building_obj, num_of_apts_label)
                            if num_of_apts_val != None:
                                attr_val = int(attr_val)
                                attr_val += int(num_of_apts_val)
                        
                        rs.SetUserText(building_obj, attr_label, attr_val)

###################################### Remove buildings without attributes #########################################

# get all objects in plots layer        
building_objs = rs.ObjectsByLayer(relevant_layers_dict["buildings"])

attribute_labels_list = []
with open(proc_attributes_path,"r") as input_handle:
    rdr = csv.reader( input_handle )
    attribute_labels_list = next(rdr)

for building_obj in building_objs:
    if rs.IsCurve(building_obj) and rs.IsCurveClosed(building_obj):
        some_attrib = rs.GetUserText(building_obj, attribute_labels_list[0])
        if some_attrib == None:
            rs.DeleteObject(building_obj)


###################################### Add attributes per plot #####################################################


# get objects by layer
building_objs = rs.ObjectsByLayer(relevant_layers_dict["buildings"])        
plot_objs = rs.ObjectsByLayer(relevant_layers_dict["plots"])


# read attribure labels (first row)
attribute_labels_list = []  
with open(proc_attributes_path,"r") as input_handle:
    rdr = csv.reader( input_handle )
    attribute_labels_list = next(rdr)

for building_obj in building_objs:
    if rs.IsCurve(building_obj) and rs.IsCurveClosed(building_obj):
        crv = rs.coercecurve(building_obj)
        
        #building_center_pt = rs.CurveAreaCentroid(building_obj)[0]
        building_center_pt = crv.GetBoundingBox(True).Center
        
        for plot_obj in plot_objs:
            if rs.PointInPlanarClosedCurve(building_center_pt, plot_obj):                
                for attr_label in set(attribute_labels_list).intersection(plot_attribs_list): #todo: intersection redundant
                    
                    # get building attribute
                    plot_attr_val = int(rs.GetUserText(building_obj, attr_label))
                    
                    # if NUM_APTS_C already set, add to it
                    num_of_apts_label = "NUM_APTS_C"
                    if attr_label == num_of_apts_label:
                        num_of_apts_val = rs.GetUserText(plot_obj, num_of_apts_label)
                        if num_of_apts_val != None:
                            plot_attr_val += int(num_of_apts_val)
                    
                    rs.SetUserText(plot_obj, attr_label, plot_attr_val)

###################################### Remove plots without attributes #########################################

# get all objects in plots layer        
plot_objs = rs.ObjectsByLayer(relevant_layers_dict["plots"])

for plot_obj in plot_objs:
    if rs.IsCurve(plot_obj) and rs.IsCurveClosed(plot_obj):
        some_attrib = rs.GetUserText(plot_obj, plot_attribs_list[0])
        if some_attrib == None:
            rs.DeleteObject(plot_obj)

###################################### Extrude buildings by NUM_FLOORS #############################################

# Extrude all buildings according to NUM_FLOORS attribute multiplied by FLOOR_HEIGHT constant
# get all objects in building layer        
building_objs = rs.ObjectsByLayer(relevant_layers_dict["buildings"])
for building_obj in building_objs:
    if rs.IsCurve(building_obj) and rs.IsCurveClosed(building_obj) and rs.CurveArea(building_obj)[0] > MIN_BUILDING_AREA_SQM:
        crv = rs.coercecurve(building_obj)                
        num_of_floors = rs.GetUserText(building_obj, "NUM_FLOORS")
        building_height = FLOOR_HEIGHT_M * int(num_of_floors)
        srf = rs.ExtrudeCurveStraight(crv,(0,0,0),(0,0,building_height))
        rs.CapPlanarHoles(srf)
        
rs.ViewDisplayMode(rs.CurrentView(),"Shaded")