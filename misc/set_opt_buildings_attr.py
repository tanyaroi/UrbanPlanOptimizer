relevant_layers_dict = {"buildings": "2200", "plots" : "H0010A", "opt_buildings" : "XXXXX"}
plot_attribs_list = ["STREET_COD", "BLDG_NUM", "NUM_APTS_C"]

# get all objects in plots layer
plot_objs = rs.ObjectsByLayer(relevant_layers_dict["plots"])

# get all objects in opt_buildings layer        
opt_building_objs = rs.ObjectsByLayer(relevant_layers_dict["opt_buildings"])
    
for opt_building_obj in opt_building_objs:
    if rs.IsCurve(opt_building_obj) and rs.IsCurveClosed(opt_building_obj):
        crv = rs.coercecurve(opt_building_obj)
        #building_center_pt = rs.CurveAreaCentroid(building_obj)[0]
        building_center_pt = crv.GetBoundingBox(True).Center
        
        for plot_obj in plot_objs:
            if rs.PointInPlanarClosedCurve(building_center_pt, plot_obj):
                for attr_label in plot_attribs_list:
                    # get building attribute
                    building_attr_val = int(rs.GetUserText(plot_obj, attr_label))
                    rs.SetUserText(opt_building_obj, attr_label, building_attr_val)