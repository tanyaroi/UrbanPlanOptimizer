import csv
import os

working_dir_path = "D:\\Google Drive\\Work\\Hired\\2020 - HQ Architects\\PyGH\\taba\\"
target_labels_path = "config\\target_labels.csv"
composite_path = "inputs\\composite.csv"
proc_composite_path = "inputs\\proc_composite.csv"
proc_polylines_path = "inputs\\proc_polylines.csv"
proc_attributes_path = "inputs\\proc_attributes.csv"

# set current working directory
os.chdir(working_dir_path)


# load target_labels_list from file
target_labels_list = ()
with open(target_labels_path,"r") as target_labels_handle:
    rdr = csv.reader( target_labels_handle )
    target_labels_list = next(rdr)
    

# filter input.csv by predefined labels and write to output.csv
# For python 3.9.1: with open("external_inputs\\input.csv","r", newline='', encoding='utf-8',  errors='ignore') as input_handle:
with open(composite_path, "r") as input_handle:
    rdr = csv.reader( input_handle )
    # For python 3.9.1: with open("outputs\\output.csv","w", newline='', encoding='utf-8',  errors='ignore') as output_handle:
    with open(proc_composite_path, "wb") as output_handle:
        wtr = csv.writer( output_handle )

        # read first row (aka labels row)
        labels_list = next(rdr)

        # find target indices in labels_list
        target_indices = [labels_list.index(target_label) for target_label in target_labels_list]
        
        # write first row to "output.csv" which happens to be the labels row
        wtr.writerow([labels_list[index] for index in target_indices])

        # write filtered columns to output.csv
        for row in rdr:
            print ("reading line #:", rdr.line_num) 
            wtr.writerow([row[index] for index in target_indices])

# For python 3.9.1: with open("outputs\\output.csv", "r", newline='', encoding='utf-8',  errors='ignore') as output_handle:
with open(proc_composite_path, "r") as output_handle:
    # For python 3.9.1: with open("outputs\\polylines_output.csv", "w", newline='', encoding='utf-8',  errors='ignore') as polylines_output_handle:
    with open(proc_polylines_path, "wb") as polylines_output_handle:
        # For python 3.9.1: with open("outputs\\attributes_output.csv", "w", newline='', encoding='utf-8',  errors='ignore') as attributes_output_handle:
        with open(proc_attributes_path, "wb") as attributes_output_handle:
            
            rdr = csv.reader(output_handle)
            poly_wrt = csv.writer(polylines_output_handle)
            attr_wrt = csv.writer(attributes_output_handle)

            # read first row (aka labels row) and write as first row of both poly_output and attribute_output
            labels_list = next(rdr)
            poly_wrt.writerow(labels_list)
            attr_wrt.writerow(labels_list)
            
            # look for hebrew string
            attributes_search_list = ["\xd7\x9d\xd7\x99\xd7\xa8\xd7\x95\xd7\x92\xd7\x9e"]
            polyline_search_str = "Polyline"

            for row in rdr:
                for attribute in attributes_search_list:
                    if attribute in row[labels_list.index("BLDG_CH")]:
                        attr_wrt.writerow(row)
                
                if polyline_search_str in row[labels_list.index("Name")]:
                    poly_wrt.writerow(row)