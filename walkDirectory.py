'''
This script walks through the directory 
and recursively lists all the files with certain extension. 
'''
import os
import sys

directory=sys.argv[1]
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".apk"):
             print(os.path.join(root, file))
             print(file)
