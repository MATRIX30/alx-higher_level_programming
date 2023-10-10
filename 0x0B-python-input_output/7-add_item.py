#!/usr/bin/python3
import sys
import json
import os
"""	script to add all arguments to as python list
    and then save them to a file
"""

"""importing necesarry modules"""


# import importlib
# save_to_json_file = importlib.import_module("5-save_to_json_file")
# load_from_json_file = importlib.import_module("6-load_from_json_file")

flag = 0

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


# check if file exist if not create one with 'w' mode
if not os.path.exists("add_item.json"):
    open("add_item.json", "w").close()
    flag = 1

# verify if file was not present in the first place and was just created
if flag == 1:
    res = []
else:
    res = list(load_from_json_file("add_item.json"))


# add command line arguments to values read to python list
for i in range(1, len(sys.argv)):
    res.append(sys.argv[i])

# save the updated results to the file
save_to_json_file(res, "add_item.json")
