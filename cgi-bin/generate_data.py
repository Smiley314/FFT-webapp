#! /Users/melissabenefer/PycharmProjects/Test/venv/bin/python

import cgi

from validate import gen_fft
import yate
import cgitb

cgitb.enable()


from_data = cgi.FieldStorage()
file_name = from_data['which_file'].value


print(yate.start_response())
print(yate.include_header("Results of the FFT"))
gen_fft(str(file_name))
print(yate.image("new_fig.png"))
print(yate.include_footer({"Home": "/index.html", "Select another file": "generate_list.py"}))

