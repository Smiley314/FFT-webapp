#! /Users/melissabenefer/PycharmProjects/Test/venv/bin/python

import cgi
import yate
import cgitb

cgitb.enable()

print(yate.start_response())
print(yate.upload())
from_data = cgi.FieldStorage()

print(yate.para(str(from_data)))