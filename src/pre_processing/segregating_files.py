# -*- coding: utf-8 -*-

#Imports
from os import path
from os import listdir
from os.path import isfile, join
import json

#Paths
raw_data_path = path.abspath(r'E:\\Repositories\\transfer_learning_tom_and_jerry\\data\\jerry_images\\raw_data\\')
meta_data_path = path.abspath(r'E:\\Repositories\\transfer_learning_tom_and_jerry\\data\\meta_data\\list_of_files.json')

#Creating a dictionary for saving file names
list_of_files = dict()

#Extraction list of files in the folder
files = [f for f in listdir(raw_data_path) if isfile(join(raw_data_path, f))]

#Finding all the types of files present in the data
file_extensions = []
for file in files:
    file_extensions.append(file.split('.')[-1])    
file_extensions = set(file_extensions)

#Segegating list of files based on the file extenstions
for file_extension in file_extensions:
    temp_list = []
    for file in files:
        if file.endswith(file_extension):
            temp_list.append(file)            
    list_of_files[str(file_extension)] = temp_list
list_of_files_json = json.dumps(list_of_files)

#Writing the JSON String to a json file
with open(meta_data_path , 'w') as f:
    json.dump(list_of_files_json, f)