from os import path
import csv

inputs_dir = "inputs"
config_dir = "config"

working_dir_path = "D:\\Google Drive\\Work\\Hired\\2020 - HQ Architects\\PyGH\\taba\\"
composite_path = path.join(inputs_dir, "composite.csv")
proc_attributes_path = path.join(inputs_dir, "proc_attributes.csv")

relevant_layers_dict = {
    "buildings": "2200",
    "plots" : "H0010A",
    "opt_buildings" : "XXXXX",
    "roads" : "2420"
}

plot_attribs_list = [
    "STREET_COD", 
    "BLDG_NUM",
    "NUM_APTS_C"
]


#  target labels dict
attr_filter_dict = {
    "Name" : "",
    "BLDG_CH" : "\xd7\x9d\xd7\x99\xd7\xa8\xd7\x95\xd7\x92\xd7\x9e", 
    "BLDG_NUM" : "",
    "NUM_APTS_C" : "",
    "NUM_FLOORS" : "",
    "Position X" : "",
    "Position Y" : "",
    "Position Z" : "",
    "STREET_COD" : ""
}


MIN_BUILDING_AREA_SQM = 50
FLOOR_HEIGHT_M = 3