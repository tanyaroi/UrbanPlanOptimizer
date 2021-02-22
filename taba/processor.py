import csv
import os

os.chdir(r"D:\\Google Drive\\Work\\Hired\\2020 - HQ Architects\\Python\\taba\\")


# load target_labels_list from file
target_labels_list = ()
with open("custom_inputs\\target_labels.csv","r") as target_labels_handle:
    rdr = csv.reader( target_labels_handle )
    target_labels_list = next(rdr)


# filter input.csv by predefined labels and write to output.csv
# For python 3.9.1: with open("external_inputs\\input.csv","r", newline='', encoding='utf-8',  errors='ignore') as input_handle:
with open("external_inputs\\input.csv","r") as input_handle:
    rdr = csv.reader( input_handle )
    # For python 3.9.1: with open("outputs\\output.csv","w", newline='', encoding='utf-8',  errors='ignore') as output_handle:
    with open("outputs\\output.csv","wb") as output_handle:
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
with open("outputs\\output.csv", "r") as output_handle:
    # For python 3.9.1: with open("outputs\\polylines_output.csv", "w", newline='', encoding='utf-8',  errors='ignore') as polylines_output_handle:
    with open("outputs\polylines_output.csv", "wb") as polylines_output_handle:
        # For python 3.9.1: with open("outputs\\attributes_output.csv", "w", newline='', encoding='utf-8',  errors='ignore') as attributes_output_handle:
        with open("outputs\\attributes_output.csv", "wb") as attributes_output_handle:
            
            rdr = csv.reader(output_handle)
            poly_wrt = csv.writer(polylines_output_handle)
            attr_wrt = csv.writer(attributes_output_handle)

            # read first row (aka labels row) and write as first row of both poly_output and attribute_output
            labels_list = next(rdr)
            poly_wrt.writerow(labels_list)
            attr_wrt.writerow(labels_list)

            for row in rdr:
                chosen_wrt = poly_wrt if row[labels_list.index("Name")] == "Polyline" else attr_wrt 
                chosen_wrt.writerow(row)