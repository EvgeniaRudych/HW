# In the homework directory you can find the directory arg_parser_homework where you can find 2020_june_mini.csv file.
#
# 1. Create a script with arguments:
#
# exp; required: false; default: min(exp)
# current_job_exp; required: false; default: max(current_job_exp)
# sex; required: false
# city; required: false
# position; required: false
# age; required: false
# path_to_source_files; required: true;
# destination_path; required: false; default: .
# destination_filename; required: false; default: f"2020_june_mini.csv".
# The script should read the .csv file and get the information based on your input and generate a new .csv
# file with that info
#
# Example of input:
# -exp 3 -sex female -position DevOps -city Kyiv --path_to_source_files . ...
import csv
import argparse
parser = argparse.ArgumentParser(description='My homework 12 for cursor ')
args = parser.parse_args()

parser.add_argument(--"experince", required=False, default=max(current_job_exp), help="Experience")
parser.add_argument("--current_job_exp", required=False, default=0, help="Experience on current job")
parser.add_argument("--sex", "-s", required=False, help="Sex")
parser.add_argument("--city", required=False, help="City")
parser.add_argument("--position", "-p", required=False, help="Position")
parser.add_argument("--age", "-a", required=False, help="Age")
parser.add_argument("--path_to_source_files", required=True, help="Path to source file")
parser.add_argument("--destination_path", required=False, default=".", help="Path for new file")
parser.add_argument("--destination_filename", required=False, default="2020_june_mini.csv", help="Name of new file")
args = parser.parse_args()

