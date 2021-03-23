import csv
import os
from config import *


def process(in_path, out_path):
    # For python 3.9.1: with open("outputs\\output.csv", "r", newline='', encoding='utf-8',  errors='ignore') as output_handle:
    with open(in_path, "r") as input_handle:
        # For python 3.9.1: with open("outputs\\attributes_output.csv", "w", newline='', encoding='utf-8',  errors='ignore') as attributes_output_handle:
        with open(out_path, "wb") as output_handle:
            
            rdr = csv.reader(input_handle)
            wrt = csv.writer(output_handle)

            # read first row (all file labels)
            all_labels_list = next(rdr)
            
            # create target labels list
            target_labels_list = attr_filter_dict.keys()
            
            # if any target attribute is missing no use to continue
            if(not set(target_labels_list).issubset(all_labels_list)):
                return False
            
            # find target columns in labels_list
            target_columns = [all_labels_list.index(target_label) for target_label in target_labels_list]
            target_columns.sort()

            # write first row
            wrt.writerow([all_labels_list[column] for column in target_columns]) 
            
            # filter and write remaining rows
            for row in rdr:
                chosen = True
                for attr_key, attr_val in attr_filter_dict.items():
                    if attr_val not in row[all_labels_list.index(attr_key)]:
                        chosen = False
                if chosen:
                    wrt.writerow([row[column] for column in target_columns])


        return True

# set current working directory
os.chdir(working_dir_path)

# process raw csv
process(composite_path, proc_attributes_path)