import csv
import os
import rhinoscriptsyntax as rs


os.chdir(r"D:\\Google Drive\\Work\\Hired\\2020 - HQ Architects\\PyGH\\taba\\")


# load target_labels_list from file
target_labels_list = ()
with open("custom_inputs\\point_target_labels.csv","r") as target_labels_handle:
    rdr = csv.reader( target_labels_handle )
    target_labels_list = next(rdr)


# filter attributes_output.csv by predefined labels and write to output.csv
# For python 3.9.1: with open("outputs\\attributes_output.csv","r", newline='', encoding='utf-8',  errors='ignore') as input_handle:
with open("outputs\\attributes_output.csv","r") as input_handle:
    rdr = csv.reader( input_handle )
    # For python 3.9.1: with open("outputs\\output.csv","w", newline='', encoding='utf-8',  errors='ignore') as output_handle:
    with open("outputs\\points_output.csv","wb") as output_handle:
        wtr = csv.writer( output_handle )

        # read first row (aka labels row)
        labels_list = next(rdr)

        # create points list
        point_list = []
        
        for row in rdr:
            point_x = row[labels_list.index("Position X")]
            point_y = row[labels_list.index("Position Y")]
            point_z = row[labels_list.index("Position Z")]
            print(point_x, point_y,point_z)
            pnt = rs.CreatePoint(point_x, point_y, point_z)
            point_list.append(pnt)
        print(point_list)