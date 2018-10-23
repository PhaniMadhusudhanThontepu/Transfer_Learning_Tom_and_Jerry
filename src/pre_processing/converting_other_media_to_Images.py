# -*- coding: utf-8 -*-

#Imports 
import json
import os
import shutil
import cv2

from os import path
from PIL import Image, ImageSequence

#Paths
meta_data_path = path.abspath(r'..\\..\\data\\meta_data\\')
raw_data_path = path.abspath(r'..\\..\\data\\jerry_images\\raw_data\\')
processed_images_path = path.abspath(r'..\\..\\data\\jerry_images\\processed_images\\')

#Reading JSON File
with open(meta_data_path +'list_of_files.json', 'r') as f:
    list_of_files_json = json.load(f)
        
#Converting JSON string to dict
list_of_files = json.loads(list_of_files_json)

#Taking all file extentions 
file_extenstions = list(list_of_files.keys())

#Taking a counter 
file_naming_counter = 0

def jpg_to_jpg():
    '''
    This function is used to move the files from raw data to processed Images folder
    Since no file type convertion is required only movement and renameing happens in this function
    '''
    
    #Getting the list of JPG files
    global list_of_files
    files = list_of_files['jpg']
    
    #Moving files
    for file in files:
        
        #Incrementing the counter
        global file_naming_counter
        file_naming_counter +=1
        
        old_file_name = file 
        new_file_name = str(file_naming_counter)+'.jpg'
        print(file)
        print(file_naming_counter)
        '''
        #Changing the file name
        os.chdir(raw_data_path)
         
        try:
            os.rename(old_file_name,new_file_name)
        except Exception as e:
            print(e)
        '''   
        #Moving the file
        source_path = path.join(raw_data_path,old_file_name)
        print(source_path)
        destination_path = path.join(processed_images_path,new_file_name)
        print(destination_path)
        print(path.exists(source_path))
        if path.exists(source_path):
            shutil.copy(source_path,destination_path)
           
def gif_to_jpg():
    '''
    This function is used to move the files from raw data to processed Images folder
    Since no file type convertion is required only movement and renameing happens in this function
    '''
    
    #Getting the list of JPG files
    global list_of_files
    files = list_of_files['gif']
    
    #Moving files
    for file in files:
        file_path = path.join(raw_data_path,file)
        im = Image.open(file_path)
             
        for frame in ImageSequence.Iterator(im):
            #Incrementing the counter
            global file_naming_counter
            file_naming_counter +=1
            
            try:
                frame = frame.convert('RGB')
                new_file_name = str(file_naming_counter)+'.jpg'
                destination_path = path.join(processed_images_path,new_file_name)
                if file_naming_counter%5==0:
                    frame.save(destination_path)
            except Exception as e:
                print(e)
         
def png_to_jpg():
    '''
    This function is used to move the files from raw data to processed Images folder
    Since no file type convertion is required only movement and renameing happens in this function
    '''
    
    #Getting the list of JPG files
    global list_of_files
    files = list_of_files['gif']
    
    #Moving files
    for file in files:
       
        #Incrementing the counter
        global file_naming_counter
        file_naming_counter +=1
        
        try:
            #Changing the file name
            os.chdir(raw_data_path)
            old_file_name = file 
            new_file_name = str(file_naming_counter)+'.jpg'
            im = Image.open(old_file_name)
            im = im.convert('RGB')
            destination_path = path.join(processed_images_path,new_file_name)
            im.save(destination_path)
        except Exception as e:
            print(e)
         
def jfif_to_jpg():
    '''
    This function is used to move the files from raw data to processed Images folder
    Since no file type convertion is required only movement and renameing happens in this function
    '''
    
    #Getting the list of JPG files
    global list_of_files
    files = list_of_files['jfif']
    
    #Moving files
    for file in files:
       
        #Incrementing the counter
        global file_naming_counter
        file_naming_counter +=1
        
        try:
            #Changing the file name
            os.chdir(raw_data_path)
            old_file_name = file 
            new_file_name = str(file_naming_counter)+'.jpg'
            im = Image.open(old_file_name)
            im = im.convert('RGB')
            destination_path = path.join(processed_images_path,new_file_name)
            im.save(destination_path)
        except Exception as e:
            print(e)   
            
def mp4_to_jpg():
    
    '''
    This function is used to move the files from raw data to processed Images folder
    Since no file type convertion is required only movement and renameing happens in this function
    '''
    
    #Getting the list of JPG files
    global list_of_files
    files = list_of_files['mp4']
    
    #Moving files
    for file in files:
        file_path = path.join(raw_data_path,file)
        video = cv2.VideoCapture(file_path)
        fps = int(video.get(cv2.CAP_PROP_FPS))
        
        while True:
          ret,frame = video.read()
          if ret:
              
              #Incrementing the counter
              global file_naming_counter
              file_naming_counter +=1
              
              new_file_name = str(file_naming_counter)+'.jpg'
              destination_path = path.join(processed_images_path,new_file_name)
              if file_naming_counter%fps==0:
                  cv2.imwrite(destination_path, frame)        
          else:
              break
          
         
          
def webp_to_jpg():
    
    '''
    This function is used to move the files from raw data to processed Images folder
    Since no file type convertion is required only movement and renameing happens in this function
    '''
    
    #Getting the list of JPG files
    global list_of_files
    files = list_of_files['webp']
    
    #Moving files
    for file in files:
       
        #Incrementing the counter
        global file_naming_counter
        file_naming_counter +=1
        
       
        #Changing the file name
        os.chdir(raw_data_path)
        old_file_name = file 
        new_file_name = str(file_naming_counter)+'.jpg'
        im = Image.open(old_file_name)
        im = im.convert('RGB')
        destination_path = path.join(processed_images_path,new_file_name)
        im.save(destination_path)
        
        
for file_extenstion in file_extenstions:
    #print(file_extenstion)
    if file_extenstion == 'jpg':
        #pass
        jpg_to_jpg()
    elif file_extenstion == 'gif':
        #pass
        gif_to_jpg()
    elif file_extenstion == 'png':
        #pass
        png_to_jpg()
    elif file_extenstion == 'jfif':
        #pass
        jfif_to_jpg()
    elif file_extenstion == 'mp4':
        #pass
        mp4_to_jpg()
    else:
        print('This file format cannot be converted into images :- ',file_extenstion)