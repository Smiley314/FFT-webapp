#! /Users/melissabenefer/PycharmProjects/Test/venv/bin/python

import yate
import glob
import cgitb

cgitb.enable()

data_files = glob.glob("data/*.csv")

print(yate.start_response())
print(yate.include_header("List of sample data"))
print(yate.start_form("generate_data.py"))
print(yate.para("Select a file from the list to work with:"))

for each_file in data_files:
    file_name = each_file.replace("data/", "")
    print(yate.radio_button("which_file", file_name))
print(yate.end_form("Select"))

print(yate.include_footer({"Home": "/index.html"}))
