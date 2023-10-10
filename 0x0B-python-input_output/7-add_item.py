#!/usr/bin/python3
"""	script to add all arguments to as python list 
	and then save them to a file
"""
"""importing necesarry modules"""
import sys, json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

"""load the content of the file to a res list"""
res = list(load_from_json_file("add_item.json"))

# add command line arguments to values read
for i in sys.argv:
    res.append(i)

# save the updated results to the file
save_to_json_file(res, "add_item.json")
open("kd",'')